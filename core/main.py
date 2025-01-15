import telebot
import os
from telebot import types
from telebot import apihelper


API_TOKEN = os.environ.get("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton("Sign In")
    markup.add(btn1)
    bot.reply_to(message, "select Sign In please", reply_markup=markup)

# singin_info = {}

# def sign_in_name(message):
#    bot.reply_to(message, "enter your name:")
#    bot.register_next_step_handler(message, sign_in_number)

# def sign_in_number(message):
#    singin_info["name"] = message.text
#    bot.reply_to(message, "enter your number:")
#    bot.register_next_step_handler(message, sign_in_code)

# def sign_in_code(message):
#    singin_info["number"] = message.text
#    bot.reply_to(message, "enter your code:")
#    bot.register_next_step_handler(message, sign_in_end)

# def sign_in_end(message):
#    singin_info["code"] = message.text
#    bot.reply_to(message, "sign in hase done!")
#    with open("./sign_in.txt", "a") as file:
#       for key in singin_info:
#             file.write(singin_info+"\n")









bot.infinity_polling()