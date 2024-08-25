# pylint: disable=line-too-long

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
        bot.send_message(chat_id=message.chat.id, text="Оставлены в чате",
                         reply_markup=keyboards.MainMenuForAdmins.keyboard)


def prepare_users_list_message():
    all_users_with_notifications = database.get_all_users_full_data(enable_notifications=True)
    print(all_users_with_notifications)
    all_users_without_notifications = database.get_all_users_full_data(enable_notifications=False)
    text_on = "✅ Список пользователей с включенными уведомлениями:"
    for user in all_users_with_notifications:
        if user[1] != "None":
            user_tag = f"@{user[1]}"
        else:
            user_tag = user[2]
        text_line = f"{user_tag}\n"
        text_on += text_line
    text_on += '\n\n'

    text_off = "❌ Список пользователей с выключенными уведомлениями:"
    for user in all_users_without_notifications:
        if user[1] != "None":
            user_tag = f"@{user[1]}"
        else:
            user_tag = user[2]
        text_line = f"{user_tag}\n"
        text_off += text_line
    text_off += '\n\n'

    count_data = (f"Всего пользователей: \n"
                  f"* {len(all_users_with_notifications)} c уведомлениями \n"
                  f"* {len(all_users_without_notifications)} без уведомлений")

    return text_on + text_off + count_data


