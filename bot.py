import config
import requests
import telebot
import time
from time import sleep

bot = telebot.TeleBot(config.token)
bot.send_message(config.my_chat_id, "monitoring up")
r = requests.get(config.url)
st=config.string
while True:
 st2=r.content
 if(st != st2):
    bot.send_message(config.my_chat_id, "< " + config.url + ">" + ' is broken and ' + config.string + ' not found' )
    time.sleep(60)
 sleep(1)

if __name__ == '__main__':
    main()