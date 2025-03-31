from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Включить калькулятор')],
                                      [KeyboardButton(text='О нас')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')
# catalog = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text= 'Футболки', callback_data='t-shirt')],
#     [InlineKeyboardButton(text= 'Кроссовки', callback_data='sheakers')],
#     [InlineKeyboardButton(text= 'Кепки',callback_data='cap')]])


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
                                                           request_contact=True)]],
                                 resize_keyboard=True)