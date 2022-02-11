from cgitb import text
from telebot import TeleBot, types
from config import TOKEN
from youtube import view_video
from time import sleep
import asyncio

main_loop = asyncio.get_event_loop()
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    link_button=types.KeyboardButton("Ссылка на видео")
    find_button = types.KeyboardButton("Поиск по слову")
    markup.add(find_button, link_button)
    bot.send_message(message.chat.id,'Выберите как хотите найти видео',reply_markup=markup)
@bot.message_handler(content_types=['text'])
def echo(message):
    if message.text == "Ссылка на видео":
        msg = bot.send_message(message.chat.id, "Введите ссылку на видео")
        bot.register_next_step_handler(msg, find_video)
        bot.send_message(message.chat.id, "qweqwe")

def find_video(message):
    link = message.text
    view_video(link, 30)
    bot.send_message(message.chat.id, "123123")
    
if __name__ == '__main__': # чтобы код выполнялся только при запуске в виде сценария, а не при импорте модуля
    try:
       bot.polling(none_stop=True) # запуск бота
    except Exception as e:
       print(e) # или import traceback; traceback.print_exc() для печати полной инфы
       sleep(1)
