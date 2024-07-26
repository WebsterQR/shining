import config
import database
import keyboards

bot = config.bot

def delete_users_dialog(bot, message):
    answer = "Укажи логины пользователей, с которыми нужно прекратить общение (каждый логин в новой строке)"
    msg = bot.send_message(chat_id=message.chat.id, text=answer)
    bot.register_next_step_handler(msg, delete_users)

def delete_users(message):
    logins = message.text.split('\n')
    logins = [each.strip() for each in logins]
    names = database.get_name_by_login(logins)
    names = [each[0] for each in names]
    users_list_str = '\n* '.join(names)
    answer = f"Ты хочешь удалить следующих пользователей: \n* {users_list_str} \n Все верно?"
    msg = bot.send_message(chat_id=message.chat.id, text=answer, reply_markup=keyboards.Confirm.keyboard)
    bot.register_next_step_handler(msg, confirm_delete, logins)

def confirm_delete(message, logins):
    if message.text == "Да":
        database.delete_users(users=logins)
        bot.send_message(chat_id=message.chat.id, text="Удалено", reply_markup=keyboards.MainMenuForAdmins.keyboard)
    elif message.text == "Нет":
        bot.send_message(chat_id=message.chat.id, text="Оставлены в чате", reply_markup=keyboards.MainMenuForAdmins.keyboard)