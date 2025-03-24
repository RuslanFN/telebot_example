import telebot
from telebot import types
from dotenv import load_dotenv
from os import getenv
from data.info import space_dict

markup = types.InlineKeyboardMarkup()
markup.add(types.InlineKeyboardButton(text='Список команд', callback_data='help'))


load_dotenv()
TOKEN = getenv('BOT_TOKEN')
app = telebot.TeleBot(token=TOKEN, parse_mode='MARKDOWN')




@app.message_handler(commands=['start'])
def start_message(message):
    app.send_message(chat_id=message.chat.id, text=space_dict['help'], parse_mode='MARKDOWN', reply_markup=markup)


@app.callback_query_handler(func=lambda call: call.data == 'help')
def start_message(call):
    app.send_message(chat_id=call.message.chat.id, text=space_dict['help'], parse_mode='MARKDOWN')


@app.message_handler(commands=['stars'])
def get_stars(message):
    with open('data/img/stars.jpg', 'rb') as photo:
        app.send_photo(chat_id=message.chat.id, photo=photo, caption=space_dict['stars'], parse_mode='MARKDOWN', reply_markup=markup)

@app.message_handler(commands=['planets'])
def get_planats(message):
    with open('data/img/solar_system.jpg', 'rb') as photo:
        app.send_photo(chat_id=message.chat.id, photo=photo, caption=space_dict['planets'], parse_mode='MARKDOWN', reply_markup=markup)

@app.message_handler(commands=['black_holes'])
def get_stars_black_holes(message):
    with open('data/img/black_hole.jpg', 'rb') as photo:
        app.send_photo(chat_id=message.chat.id, photo=photo, caption=space_dict['black_holes'], parse_mode='MARKDOWN', reply_markup=markup)

app.infinity_polling()
