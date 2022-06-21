import telebot
from telebot import types
import random
import config

bot = telebot.TeleBot(config.token)

# keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Сгенерировать персонажа")
item2 = types.KeyboardButton("Сгенерировать сюжет")
markup.add(item1, item2)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f'Вы {random.choice(config.character_list)} смеритесь с этим', parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def check_text(message):
	if message.chat.type == 'private':
		if message.text == 'Сгенерировать персонажа':
			message_text=f'Данные вашего персонажа: \nПрофессия: <b>{random.choice(config.proffecional_list)}</b> ' \
						 f'\nБиологические характеристики: <b>{random.choice(config.age_list)}</b> ' \
						 f'\nЗдоровье: {random.choice(config.health_list)} \nХобби: <b>{random.choice(config.hobby_list)}</b> ' \
						 f'\nБагаж: <b>{random.choice(config.things_list)}</b> \nФакты: <b>{random.choice(config.achievements_list)}</b> ' \
						 f'\nОсобые условия: <b>{random.choice(config.condition_list)}</b> ' \
						 f'\nУдачной игры:3'
			bot.send_message(message.chat.id, message_text, parse_mode='html')#reply_markup=types.ReplyKeyboardRemove()
		elif message.text == 'Сгенерировать сюжет':
			message_text = f'Сюжет игры: <b>{random.choice(config.story_list)}</b> ' \
						   f'\nУсловия бункера: <b>{random.choice(config.bunker_list)}</b> \nУдачной игры:3'
			bot.send_message(message.chat.id, message_text, parse_mode='html')
		else:
			bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

bot.infinity_polling()