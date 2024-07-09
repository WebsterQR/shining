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