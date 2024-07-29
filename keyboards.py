# pylint: disable=line-too-long

# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

class Register:
    keyboard = ReplyKeyboardMarkup()
    button_register = KeyboardButton("Авторизоваться")
    keyboard.row(button_register)
    # keyboard.add(register)

class MainMenu:
    keyboard = ReplyKeyboardMarkup()
    games_table = KeyboardButton("🗂 Таблица игр")
    team_promo = KeyboardButton("📇 Презентация Сияния")
    food_data = KeyboardButton("🍔 База едален")
    button_notifications_on = KeyboardButton("✅ Включить рассылку о мероприятиях")
    button_notifications_off = KeyboardButton("❌ Отменить рассылку о мероприятиях")
    useful_links = KeyboardButton("🔗 Полезные ссылки")
    keyboard.row(games_table, team_promo)
    keyboard.row(useful_links, food_data)
    keyboard.row(button_notifications_on, button_notifications_off)


class MainMenuForAdmins:
    keyboard = ReplyKeyboardMarkup()
    button_send_message = KeyboardButton("Сделать рассылку")
    button_delete_users = KeyboardButton("Удаление пользователей")
    keyboard.row(button_send_message)
    keyboard.row(button_delete_users)

class Confirm:
    keyboard = ReplyKeyboardMarkup()
    button_yes = KeyboardButton("Да")
    button_no = KeyboardButton("Нет")
    keyboard.row(button_yes, button_no)