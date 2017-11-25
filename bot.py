import logging, ephem, datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, BaseFilter

import settings

class CalcFilter(BaseFilter):
    def filter(self, message):
        return message.text.endswith('=')

class PlanetFilter(BaseFilter):  #необходимо было добавить фильтр по планетам - иначе все входящие сообщения от пользователя попадали под Filter.text
    def filter(self, message):
        return message.text in planet_dict

calc_filter = CalcFilter()
planet_filter = PlanetFilter()

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

planet_dict = {
            'mars': ephem.Mars,
            'марс': ephem.Mars,
            'venus': ephem.Venus,
            'венера': ephem.Venus,
            'earth': "Earth_error",
            'земля': "Earth_error",
            'mercury': ephem.Mercury,
            'меркурий': ephem.Mercury,
            'jupiter': ephem.Jupiter,
            'юпитер': ephem.Jupiter,
            'saturn': ephem.Saturn,
            'сатурн': ephem.Saturn,
            'uranus': ephem.Uranus,
            'уран': ephem.Uranus,
            'neptune': ephem.Neptune,
            'нептун': ephem.Neptune,
        }

def start_bot(bot, update):
    mytext = """Привет {}! 
Я простой бот и умею делать несколько вещей:
1) Я могу ответить в каком созвездии сейчас находится платена солнечной системы. Пришли мне название планеты на английском или русском языке.
2) Я умею считать. Пришли мне математическое выражение и поставь на конце знак '='. ('+' - сложение, '-' - вычитание, '*' - умножение, '/' - деление, '**' - возведение в степень, '**(1/n)' - корень n-ой степени.)
3) Я могу посчитать количество слов в сообщении. Пришли мне сообщение в формате: /wordcount "Ваше сообщение" """.format(update.message.chat.first_name)
    logging.info('Полльзователь {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(mytext)

def chat_planet(bot, update):
    user_message = update.message.text.lower()
 #   if user_message.endswith('='):
  #      math_expression = tuple(user_message)
   #     update.message.reply_text(math_expression)
    #elif user_message in planet_dict:
    Planet = planet_dict.get(user_message)
    logging.info(user_message)
    if Planet == "Earth_error":
        update.message.reply_text("""Земля вместе с Солнцем относится к галактике Млечный путь, но находится не в центре, а на окраине. Ни в каком созвездии не находится, cозвездия придумали люди что бы как-то упорядочить ВИДИМЫЕ С ЗЕМЛИ звезды.""")
    else:
        update.message.reply_text(ephem.constellation(Planet(datetime.datetime.now())))

def chat_calc(bot, update):
    try:
        user_expression_calc = update.message.text.lower()
        chat_calc_fnc = user_expression_calc[:-1]
        update.message.reply_text(eval(chat_calc_fnc))
    except ZeroDivisionError:
        update.message.reply_text('Ошибка! На ноль делить нельзя!')
    except SyntaxError:
        update.message.reply_text('Ошибка! Для выполнения расчета необходимы 2 числа и знак операции!')


def wordcount(bot, update):
    user_phrase = update.message.text.lower()
    if user_phrase.startswith('/wordcount "') == False:
        update.message.reply_text('Ошибка! Необходимо ввести комманду следующим образом: /wordcount "Ваша фраза"')
    elif user_phrase.endswith('"') == False:
        update.message.reply_text('Ошибка! Необходимо ввести комманду следующим образом: /wordcount "Ваша фраза"')
    else:
        user_phrase_quotes = user_phrase[12:-2]
        if user_phrase_quotes.strip() == '':
            update.message.reply_text('Ошибка! Вы не ввели фразу! Необходимо ввести комманду следующим образом: /wordcount "Ваша фраза"')
        else:
            user_phrase_list = user_phrase_quotes.split()
            user_phrase_list_filt = [phrase for phrase in user_phrase_list if phrase not in '"!,? ']
            update.message.reply_text(user_phrase_list_filt)
            update.message.reply_text(len(user_phrase_list_filt))
     

def main():
    updrt = Updater(settings.TELEGRAM_API_KEY)

    updrt.dispatcher.add_handler(CommandHandler('start', start_bot))
    updrt.dispatcher.add_handler(CommandHandler('wordcount', wordcount))
    updrt.dispatcher.add_handler(MessageHandler(planet_filter, chat_planet))
    updrt.dispatcher.add_handler(MessageHandler(calc_filter, chat_calc))

    updrt.start_polling()
    updrt.idle()

if __name__ == '__main__':
    logging.info('Bot started')
    main()
