import telebot
from telebot import types
import random
import config

bot = telebot.TeleBot(config.token)

# keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Сгенерировать персонажа 🦸")
item2 = types.KeyboardButton("Сгенерировать сюжет 📖")
markup.add(item1, item2)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, f'Привет, правила тебе обьяснит кто-то другой, а пока держи это сообщение. Бот создан @DaniilSemizhonov', parse_mode='html', reply_markup=markup)
	message_text = f'Данные вашего персонажа: \nПрофессия: \nБиологические характеристики: \nЗдоровье: \nХобби:' \
				   f'\nБагаж:\nФакты:\nОсобые условия:'
	bot.send_message(message.chat.id, message_text, parse_mode='html')

@bot.message_handler(content_types=['text'])
def check_text(message):
	if message.text == 'Сгенерировать персонажа 🦸':
		message_text=f'Данные вашего персонажа: \nПрофессия: <b>{random.choice(config.proffecional_list)}</b> ' \
					f'\nБиологические характеристики: <b>{random.choice(config.age_list)}</b> ' \
					f'\nЗдоровье: <b>{random.choice(config.health_list)}</b> \nХобби: <b>{random.choice(config.hobby_list)}</b> ' \
					f'\nБагаж: <b>{random.choice(config.things_list)}</b> \nФакты: <b>{random.choice(config.achievements_list)}</b> ' \
					f'\nОсобые условия: <b>{random.choice(config.condition_list)}</b> ' \
					f'\nУдачной игры:3'
		bot.send_message(message.chat.id, message_text, parse_mode='html')
	elif message.text == 'Сгенерировать сюжет 📖':
		if message.chat.type == 'private':
			message_text = f'Сюжет игры: <b>{random.choice(config.story_list)}</b> ' \
							f'\nУсловия бункера: <b>{random.choice(config.bunker_list)}</b> \nУдачной игры:3'
			bot.send_message(message.chat.id, message_text, parse_mode='html')
		else:
			bot.send_message(message.chat.id, 'Лучше напиши мне в <a href="https://t.me/BoardBunkerBot">личку</a>', parse_mode='html')
	else:
		pass

bot.infinity_polling()