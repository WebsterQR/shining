import telebot
from telebot import types

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
def parse_text_register(message):
    if message.text == "Авторизоваться":
        if not database.check_user_already_exist(message.chat.id):
            first_name = message.from_user.first_name if message.from_user.first_name else ""
            last_name = message.from_user.last_name if message.from_user.last_name else ""
            database.add_user(chat_id=message.chat.id, name=first_name + " " + last_name, login=message.from_user.username)
            answer = constants.TextTemplates.message_after_auth
        else:
            answer = constants.TextTemplates.message_already_auth

        reply_keyboard = keyboards.MainMenuForAdmins if message.from_user.username in config.ADMIN_USERS else keyboards.MainMenu
        bot.send_message(chat_id=message.chat.id, text=answer, reply_markup=reply_keyboard.keyboard)

    if message.text == "Сделать рассылку":
        print('mailing')
        answer = "Укажи текст который нужно отправить"
        msg = bot.send_message(chat_id=message.chat.id, text=answer)
        bot.register_next_step_handler(msg, send_mailing)

    if message.text == "Удаление пользователей":
        helpers.delete_users_dialog(bot, message)

def send_mailing(message):
    all_users_chat_ids = database.get_all_users()
    bot.send_message(message.chat.id, text=str(all_users_chat_ids))
    for chat_id in all_users_chat_ids:
        bot.send_message(chat_id=chat_id, text=constants.TextTemplates.template_for_mailing.format(author="Автор", message=message.text))



bot.polling(none_stop=True, interval=0)