import telebot
# подключи библиотеку python Packages telebot
import datetime
import time
import threading
import random

# Создаем бота с использованием правильного метода TeleBot
bot = telebot.TeleBot("7281452422:AAGkE9wjqIJmLvnXGNKTAhL6FZJhkaKGJgU")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, text='Привет.Моё имя МИНЗИФА. Я чат-бот, который будет напоминать тебе пить водичку!')
    reminder_thread=threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

# Обработчик команды /start
@bot.message_handler(commands=['fact'])
def fact_message(message):
    bot.reply_to(message, text='Привет. МИНЗИФА. Я чат-бот, который будет напоминать тебе пить водичку!')
    list=['Вода поддерживает работу мозга: даже небольшое обезвоживание — всего 1-2% от массы тела — может ухудшить концентрацию, память и когнитивные функции. Регулярное питье воды помогает мозгу работать на полную мощность.',

'Вода регулирует температуру тела: через потоотделение вода помогает поддерживать нормальную температуру тела. Когда вы теряете воду через пот, важно её восполнять, чтобы избежать перегрева и поддерживать здоровье организма.',

'Вода выводит токсины: вода помогает почкам выводить отходы и токсины через мочу. Недостаток воды может привести к накоплению токсинов, что негативно сказывается на здоровье, поэтому питье достаточного количества воды — это ключ к очищению организма.']

    random_fact = random.choice(list)

    bot.reply_to(message, text=f'Лови факт о воде: {random_fact}')

def send_reminders(chat_id):
    first_rem = ("02:15")
    second_rem = ("06:00")
    end_rem = ("07:00")
    rem8 = ("08:00")
    rem9 = ("09:00")
    rem10 = ("10:00")
    rem11 = ("11:00")
    rem12 = ("12:00")
    rem13 = ("13:00")
    rem14 = ("14:00")
    rem15 = ("15:00")
    rem16 = ("16:00")
    rem17 = ("17:00")
    rem18 = ("18:00")
    rem19 = ("19:00")
    rem20 = ("20:00")
    rem21 = ("21:00")
    rem22 = ("22:00")
    rem23 = ("23:05")
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem or now ==  second_rem or now == end_rem:
            bot.send_message(chat_id, text= "Напоминание: Выпей стакан воды")
            time.sleep(61)
        time.sleep(1)

# Правильное использование метода polling
bot.polling(non_stop=True)

