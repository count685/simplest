import logging, ephem, datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def start_bot(bot, update):
    mytext = """Привет {}! 
    Я простой бот и могу ответить в каком созвездии сейчас находится платена солнечной системы. 
    Пришли мне название планеты на английском языке""".format(update.message.chat.first_name)
    logging.info('Полльзователь {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(mytext)

def chat(bot, update):
    planet_name = update.message.text.lower()
    logging.info(planet_name)
    if planet_name == 'mars':
        update.message.reply_text(ephem.constellation(ephem.Mars(datetime.datetime.now())))
    elif planet_name == 'mercury':
        update.message.reply_text(ephem.constellation(ephem.Mercury(datetime.datetime.now())))
    elif planet_name == 'venus':
        update.message.reply_text(ephem.constellation(ephem.Venus(datetime.datetime.now())))
    elif planet_name == 'earth':
        update.message.reply_text("""Земля вместе с Солнцем относится к галактике Млечный путь, 
но находится не в центре, а на окраине. Ни в каком созвездии не находится, 
созвездия придумали люди что бы как-то упорядочить ВИДИМЫЕ С ЗЕМЛИ звезды.""")
    elif planet_name == 'jupiter':
        update.message.reply_text(ephem.constellation(ephem.Jupiter(datetime.datetime.now())))
    elif planet_name == 'saturn':
        update.message.reply_text(ephem.constellation(ephem.Saturn(datetime.datetime.now())))
    elif planet_name == 'uranus':
        update.message.reply_text(ephem.constellation(ephem.Uranus(datetime.datetime.now())))
    elif planet_name == 'neptune':
        update.message.reply_text(ephem.constellation(ephem.Neptune(datetime.datetime.now())))
    elif planet_name == 'марс':
        update.message.reply_text(ephem.constellation(ephem.Mars(datetime.datetime.now())))
    elif planet_name == 'меркурий':
        update.message.reply_text(ephem.constellation(ephem.Mercury(datetime.datetime.now())))
    elif planet_name == 'венера':
        update.message.reply_text(ephem.constellation(ephem.Venus(datetime.datetime.now())))
    elif planet_name == 'земля':
        update.message.reply_text("""Земля вместе с Солнцем относится к галактике Млечный путь, 
но находится не в центре, а на окраине. Ни в каком созвездии не находится, 
созвездия придумали люди что бы как-то упорядочить ВИДИМЫЕ С ЗЕМЛИ звезды.""")
    elif planet_name == 'юпитер':
        update.message.reply_text(ephem.constellation(ephem.Jupiter(datetime.datetime.now())))
    elif planet_name == 'сатурн':
        update.message.reply_text(ephem.constellation(ephem.Saturn(datetime.datetime.now())))
    elif planet_name == 'уран':
        update.message.reply_text(ephem.constellation(ephem.Uranus(datetime.datetime.now())))
    elif planet_name == 'нептун':
        update.message.reply_text(ephem.constellation(ephem.Neptune(datetime.datetime.now())))

def main():
    updrt = Updater(settings.TELEGRAM_API_KEY)

    updrt.dispatcher.add_handler(CommandHandler('start', start_bot))
    updrt.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updrt.start_polling()
    updrt.idle()

if __name__ == '__main__':
    logging.info('Bot started')
    main()

