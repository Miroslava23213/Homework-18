import telebot
from config import keys
from utils import ConvertionException, CryptoConverter

from telebot import TeleBot

bot: TeleBot = telebot.TeleBot("5304849045:AAHnYSCH4YyaSJEbckYfYlvkpjWbbjVGWCA")

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу бота, введите команду в следующем формате:\n<имя валюты> \
    <в какую перевести> \
    <количество переводимой валюты>\nУвидить список всех достпных валют:/values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

    class ConvertionException:
        pass
        @bot.message_handler(content_types=['text', ])
        def convert(message: telebot.types.Message):
            values = message.text.split(' ')

    if len(values) != 3:
        raise ConvertionException('Слишком много параметров./')

        quote, base, amount = values
        total_base = CryptoConverter.convert(base, amount)

    text = f'Цена{amount}{quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)

bot.infinity_polling()
