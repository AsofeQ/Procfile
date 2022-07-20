import requests
import telebot
import random
from telebot import types
from time import sleep
import os
from flask import Flask
from threading import Thread
import random


app = Flask('')

@app.route('/')
def home():
	return 'I am tofe x - Running'

def run():
  app.run(
		host='0.0.0.0',
		port=random.randint(2000,9000)
	)

def keep_alive():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=run)
	t.start()
os.system("pip3 install requests")
os.system("pip3 install random")
os.system("pip3 install time")
os.system("pip3 install PyTelegramBotAPI==3.6.7")

from flask import Flask
server=Flask(__name__)
import json,os
keep_alive()
###-----###
#video.title
#video.views
#video.likes
#video.streams
###-----###
RUN = "Started ✔️"
token	= "5427304351:AAEUwt_Q86zScdQH2KST2nFvRweSjuVd07U"
bot = telebot.TeleBot("5427304351:AAEUwt_Q86zScdQH2KST2nFvRweSjuVd07U")
r = requests.session()
@bot.message_handler(commands=['start'])
def send_welcome(message):
    mess = message.text
    Key = types.InlineKeyboardMarkup()
    call  = types.InlineKeyboardButton(text = "Our channel", url = "https://t.me/Py_iq") 
    Key.add(call)
    bjj = message.chat.id
    start = bot.send_message(message.chat.id, f"welcome in youtube dl bot", reply_markup=Key)
    send_url(message)
@bot.message_handler(content_types=["sticker", "pinned_message", "photo", "audio", "document"])
def just_send_url(message):
	bot.send_message(message.chat.id, "رجاء قم بأرسال الرابط فقط!" ,)
@bot.message_handler(func=(lambda message: True))#Tofe_x #trprogram
def send_url(message):
			mes = message.text
			if "https://youtu.be/" or "http://www.youtube.com/watch?v" in mes:
				req =  f"https://api.snappea.com/v1/video/details?url={mes}"
				r_u = requests.get(req)
				ree = (r_u.json())
				r_r =(ree["statusCode"])
				if r_r	==	0:
					tsts = bot.send_message(message.chat.id, text	= "يتم التحميل ، يرجى الانتظار")
					kj = (tsts.message_id)
					bj = message.chat.id
					download =(ree["videoInfo"]["downloadInfoList"][2]["partList"][0]["urlList"][0])
					dow = requests.get(f"{download}").content
					name =(ree["videoInfo"]["title"])
					with open(f"{name}.mp3", "wb") as f:
							f.write(dow)
					done = open(f"{name}.mp3","rb")
					bot.edit_message_text("تم التحميل" , message.chat.id , tsts.message_id)
					bot.send_audio(message.chat.id, done)
					os.remove(f"{name}.mp3")		
				else:
						pass
			else:
					bot.send_message(message.chat.id, text	= "حاول مجددا")
print(RUN)
bot.polling()