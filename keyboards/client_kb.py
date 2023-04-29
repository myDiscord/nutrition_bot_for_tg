from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

b1 = KeyboardButton('/Start')
b2 = KeyboardButton('/About')
b3 = KeyboardButton('Man 👨')
b4 = KeyboardButton('Woman 👩')
b5 = KeyboardButton('1️⃣')
b6 = KeyboardButton('2️⃣')
b7 = KeyboardButton('3️⃣')
b8 = KeyboardButton('4️⃣')
b9 = KeyboardButton('5️⃣')
b10 = KeyboardButton('Weight Loss')
b11 = KeyboardButton('Maintain form')
b12 = KeyboardButton('Grow Mass')


on_startup_button = InlineKeyboardMarkup(row_width=2).row(
     InlineKeyboardButton(text='About the bot', callback_data='info'), InlineKeyboardButton(text='Start', callback_data='calculate'))

gender_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
gender_button.row(b3, b4)
activity_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
activity_button.row(b5, b6, b7, b8, b9)
goal_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
goal_button.row(b10, b11, b12)