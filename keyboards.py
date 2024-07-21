# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

class Register:
    keyboard = ReplyKeyboardMarkup()
    button_register = KeyboardButton("Авторизоваться")
    keyboard.row(button_register)
    # keyboard.add(register)

class MainMenu:
    keyboard = ReplyKeyboardMarkup()
    button_send_message = KeyboardButton("Сделать рассылку")
    keyboard.row(button_send_message)

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