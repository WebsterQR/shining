from time import sleep

import config
import constants
import database
import helpers
import keyboards

# bot = telebot.TeleBot(config.Telegram.TOKEN)
bot = config.bot


@bot.message_handler(commands=['help', 'start'])
def start(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=constants.TextTemplates.message_before_auth,
        reply_markup=keyboards.Register.keyboard
    )


@bot.message_handler(content_types=["text"])
def parse_text_register(message):  # noqa: C901
    if message.text == "Авторизоваться":
        if not database.check_user_already_exist(message.chat.id):
            first_name = message.from_user.first_name if message.from_user.first_name else ""
            last_name = message.from_user.last_name if message.from_user.last_name else ""
            database.add_user(chat_id=message.chat.id,
                              name=first_name + " " + last_name,
                              login=message.from_user.username)
            answer = constants.TextTemplates.message_after_auth
        else:
            answer = constants.TextTemplates.message_already_auth

        reply_keyboard = keyboards.MainMenuForAdmins \
            if message.from_user.username in config.ADMIN_USERS else keyboards.MainMenu
        bot.send_message(chat_id=message.chat.id, text=answer, reply_markup=reply_keyboard.keyboard)

    if message.text == "Сделать рассылку":
        answer = "Укажи текст который нужно отправить"
        msg = bot.send_message(chat_id=message.chat.id, text=answer)
        bot.register_next_step_handler(msg, send_mailing)

    if message.text == "Удаление пользователей":
        helpers.delete_users_dialog(bot, message)
    if message.text == "🗂 Таблица игр":
        bot.send_message(chat_id=message.chat.id, text=constants.TextTemplates.message_games_table,
                         parse_mode='MarkdownV2', reply_markup=keyboards.MainMenu.keyboard)
    if message.text == "📇 Презентация Сияния":
        bot.send_message(chat_id=message.chat.id, text=constants.TextTemplates.message_team_promo,
                         parse_mode='MarkdownV2', reply_markup=keyboards.MainMenu.keyboard)
    if message.text == "🔗 Полезные ссылки":
        bot.send_message(chat_id=message.chat.id, text=constants.TextTemplates.message_useful_links,
                         parse_mode='MarkdownV2', reply_markup=keyboards.MainMenu.keyboard,
                         disable_web_page_preview=True)
    if message.text == "🍔 База едален":
        bot.send_message(chat_id=message.chat.id, text=constants.TextTemplates.message_food,
                         parse_mode='MarkdownV2', reply_markup=keyboards.MainMenu.keyboard)
    if message.text == "✅ Включить рассылку о мероприятиях":
        is_already_notified = database.check_user_notifications_value(chat_id=message.chat.id)
        if is_already_notified:
            bot.send_message(chat_id=message.chat.id, text=constants.TextTemplates.notifications_already_enabled,
                             reply_markup=keyboards.MainMenu.keyboard)
        else:
            database.switch_notifications_flag(chat_id=message.chat.id, new_value=True)
            bot.send_message(chat_id=message.chat.id, text=constants.TextTemplates.notifications_enabled,
                             reply_markup=keyboards.MainMenu.keyboard)
    if message.text == "❌ Отменить рассылку о мероприятиях":
        is_already_notified = database.check_user_notifications_value(chat_id=message.chat.id)
        if not is_already_notified:
            bot.send_message(chat_id=message.chat.id, text=constants.TextTemplates.notifications_already_disabled,
                             reply_markup=keyboards.MainMenu.keyboard)
        else:
            ans = bot.send_message(chat_id=message.chat.id,
                                   text=constants.TextTemplates.message_notifications_off_confirm,
                                   reply_markup=keyboards.Confirm.keyboard)
            bot.register_next_step_handler(ans, confirm_notifications_off)


def send_mailing(message):
    need_collect_answers, event_name = database.create_event()
    all_users_chat_ids = database.get_all_users()
    if config.TEST_MODE:
        all_users_chat_ids = [176063054]
    author = message.from_user.username
    for chat_id in all_users_chat_ids:
        print(all_users_chat_ids)
        if not need_collect_answers:
            bot.send_message(chat_id=chat_id,
                             text=constants.TextTemplates.template_for_mailing.format(author=author,
                                                                                      message=message.text),
                             reply_markup=keyboards.MainMenu.keyboard)
        else:
            answer = bot.send_message(chat_id=chat_id,
                             text=constants.TextTemplates.template_for_mailing.format(author=author, event_name=event_name, message=message.text), reply_markup=keyboards.Participate.keyboard)
            # bot.send_message(chat_id=chat_id, text=constants.TextTemplates.send_answer_to,
            #                  reply_markup=keyboards.Participate.keyboard)
            participate_answer = bot.register_next_step_handler(answer, collect_answers, event_name)

def collect_answers(message, event_name):
    if message.text == "Участвую":
        bot.send_message(chat_id=message.chat.id, text=constants.TextTemplates.participate_yes,
                         parse_mode='MarkdownV2', reply_markup=keyboards.MainMenu.keyboard)
        database.add_event_participation(participate=True, event_name=event_name, chat_id=message.chat.id)
    if message.text == "Не участвую":
        bot.send_message(chat_id=message.chat.id, text=constants.TextTemplates.participate_no,
                         parse_mode='MarkdownV2', reply_markup=keyboards.MainMenu.keyboard)
    # bot.send_message(chat_id=message.chat.id, text=event_name, reply_markup=keyboards.MainMenu.keyboard)


def confirm_notifications_off(message):
    if message.text == "Да":
        bot.send_message(chat_id=message.chat.id, text=constants.TextTemplates.notifications_disabled,
                         reply_markup=keyboards.MainMenu.keyboard)
        database.switch_notifications_flag(chat_id=message.chat.id, new_value=False)
    else:
        bot.send_message(chat_id=message.chat.id, text=constants.TextTemplates.notifications_not_disabled,
                         reply_markup=keyboards.MainMenu.keyboard)


while True:
    try:
        bot.infinity_polling(none_stop=True)
    except Exception as _ex:
        print(_ex)
        sleep(10)
