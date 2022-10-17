import pyowm
import telebot
owm = pyowm.OWM("2901886316f09e06c83bace140c6a73c")
mgr = owm.weather_manager()
bot = telebot.TeleBot("5738254062:AAGZM9nDktunO-pln_h6IfnMKY3q9oQTEII")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"<b>Привет, пупсик. Видимо ты боишься выглянуть в окошко и узнать какая там погода?! Чтож я помогу тебе с этим). В каком городе ты прячешься, трусишка?:</b>", parse_mode="html")
@bot.message_handler(content_types=["text"])
def get_user_text(message):
    try:
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        temp = w.temperature('celsius')['temp']
        detal = w.detailed_status

        answer = f"В твоем городишке \"{message.text}\" сейчас: {int(temp)} ℃" "\n"
        if 5 < temp < 10:
            answer += f"Прохладненько, конечно - одевай куртенку, трусишки с мехом и шапочку. Кстати не забыл ли ты оформить страховку?"
        elif 10 < temp < 15:
            answer += f"Это что за фигня?! Ты же только уехал от холода!!! КОРОЧЕ ДОСТАВАЙ КУРТЕНКУ!!!!"
        elif 15 < temp < 20:
            answer += f"Ну не плохо, не плохо. Хотя на вечерок я бы взял с собой балохончик, а то застудишь свои ушки, малыш"
        elif 20 < temp < 30:
            answer += f"Вааааа-я кайфуй братик, не просто же так сбежал))"
        elif 0 < temp < 5:
            answer += f"Билят это как так то????? Срочно ищи страну потеплее, бубенчики уже звенят!!!"
        elif 10 < temp < 0:
            answer += f"НУ И НАХ ТЫ УЕЗЖАЛ!!!???? Срочно покупай шубу!"
        elif temp < 10:
            answer += f"НУ ПИЗДЕЦ!!!! ЗИМА БЛИЗКО!!!"
    except :
        answer = (f'Ты даже город нормально не можешь написать что ли!? : {message.text}')


    bot.send_message(message.chat.id, answer)
bot.polling(none_stop=True, interval=0)
