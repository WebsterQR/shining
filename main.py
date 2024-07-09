import telebot
from telebot import types

import config
import constants
import database
import keyboards

bot = telebot.TeleBot(config.Telegram.TOKEN)


@bot.message_handler(commands=['help', 'start'])
def start(message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Привет, сияющий! Давай познакомимся. \n Нажми на кнопку Авторизоваться ниже, чтобы начать использовать бота",
        reply_markup=keyboards.Register.keyboard
    )
    #bot.register_next_step_handler(msg)


# @bot.callback_query_handler(func=lambda call: call.data == "Авторизоваться")
# def bla(call: types.CallbackQuery):
#     print('123')
@bot.message_handler(content_types=["text"])
def parse_text_register(message):
    if message.text == "Авторизоваться":
        if not database.check_user_already_exist(message.chat.id):
            database.add_user(message.chat.id, "some_name", "some_login")
            answer = "Приятно познакомиться! Теперь ты зарегистрирован"
        else:
            answer = "Оказывается, мы уже знакомы! Давай продолжим совместную работу!"
        bot.send_message(chat_id=message.chat.id, text=answer, reply_markup=keyboards.MainMenu.keyboard)

    if message.text == "Сделать рассылку":
        print('mailing')
        answer = "Укажи текст который нужно отправить"
        msg = bot.send_message(chat_id=message.chat.id, text=answer)
        bot.register_next_step_handler(msg, send_mailing)

# @bot.message_handler(content_types=["text"])
# def parse_mailing(message):
#

def send_mailing(message):
    all_users_chat_ids = database.get_all_users()
    bot.send_message(message.chat.id, text=str(all_users_chat_ids))
    for chat_id in all_users_chat_ids:
        bot.send_message(chat_id=chat_id, text=constants.TextTemplates.template_for_mailing.format(author="Автор", message=message.text))

bot.polling(none_stop=True, interval=0)