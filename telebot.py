import telebot
from telebot import types
import random

bot = telebot.TeleBot("YOUR TOKEN")

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Рандомное число"))
    markup.add(types.KeyboardButton("Рандомный напиток"))
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.lower() == "рандомный напиток")
def random_drink(message):
    drinks = ["Кумыс", "Кола", "Спрайт", "Чай", "Сок"]
    random_drink = random.choice(drinks)
    bot.send_message(message.chat.id, f"Рандомный напиток: {random_drink}")

@bot.message_handler(func=lambda message: message.text.lower() == "рандомное число")
def random_number(message):
    random_number = random.randint(1, 100)
    bot.send_message(message.chat.id, f"Рандомное число: {random_number}")

bot.polling(none_stop=True)