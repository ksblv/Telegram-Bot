import telebot
import random
from telebot import types

# Загружаем список поговорок
file = open('facts.txt', 'r', encoding='UTF-8')
facts  = file.read().split('\n')
file.close()
# Создаем бота
bot = telebot.TeleBot('5681197522:AAG18F0ArwMg2oIKjJB2gm0EyVHlrwhRXJQ')
# Команда start
@bot.message_handler(commands=["start"])
def start(message, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Факт")
        item2=types.KeyboardButton("Связаться со мной")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Привет! Нажми  "Факт" для получения интересного факта о концерне BMW',  reply_markup=markup)
            
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Факт' :
            answer = random.choice(facts)
    elif message.text.strip() == 'Связаться со мной':
        answer = 't.me/ksblv'
    else:
        answer = 'Я тебя не понимаю('
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
    
# Запускаем бота
bot.polling(none_stop=True, interval=0)
