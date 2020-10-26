# -*- coding: utf-8 -*-
import telebot
import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
bot = telebot.TeleBot("532568136:AAGMuWfuQvRkUNPTorKMqIO3Mio8WFYi948")
#datetime.now().strftime("%A")// ДЕНЬО4ЕК
#datetime.now().time().strftime("%H:%M") // ВРЕМЯЧКО
#datetime.now().isocalendar()[1] тиждень



class para:
	day = "Понеділок"
	hour = "8:30"
	subject = "Математика"
	teacher = "Іванов"

days_dictionary = {"Monday": "Понеділок", "Tuesday": "Вівторок", "Wednesday": "Середа","Thursday": "Четвер", "Friday": "П\'ятниця","Saturday":"Субота","Sunday" :"Неділя"}
teacher_dictionary = {"Пулеко Ігор Васильович": "",
"Могельницька Людмила Францівна": "https://meet.google.com/kfj-fdcc-acm",
"Кузьменко Олександр Вікторович": "https://meet.google.com/irh-qqke-nts(Лекція)\nhttps://meet.google.com/hoj-ibhc-fed(Лабораторна)",
"Лобанчикова Надія Миколаївна": "https://meet.google.com/fwx-gbnu-cce",
"Захаров Дмитро Миколайович": "https://meet.google.com/hyb-esks-ijq",
"Дмитренко Ірина Анатоліївна": "--",
"Вакалюк Тетяна Анатоліївна": "http://meet.google.com/ket-rjmk-gfh(Лабараторна)\nhttps://meet.google.com/vqf-jbtk-ysm",
"Легенчук Сергій Федорович": "https://meet.google.com/sap-wpta-xkv"}
#heroku use UTC time and can't change timezone change default time for para to UTC
time_dictionary = {"8:30":"8:00","10:00":"9:30","11:40":"11:10","13:30":"13:00","15:00":"14:30","16:30":"16:00"}
tooday=days_dictionary[datetime.now().strftime("%A")]
week = datetime.now().isocalendar()[1]%2
if week==0: week = 2

page = requests.get('https://rozklad.ztu.edu.ua/schedule/group/ІСТм-20-1?new')
soup = BeautifulSoup(page.text,"html.parser")
tables = soup.find_all('td', {'class': 'content'})

bot.send_message(-1001408795989, 'bot has been started| curent server time ' +str(datetime.now().time().strftime("%H:%M"))+'|day '+ tooday)
		
for para_table in tables:
	para_INFO=para()
	para_INFO.day = para_table.get('day')
	para_INFO.hour = para_table.get('hour')
	para_INFO.type = para_table.find_all('div', {'class': None})[1].text
	para_INFO.subject = para_table.find('div', {'class': 'subject'}).text
	para_INFO.teacher = para_table.find('div', {'class': 'teacher'}).text
	messageForSend = para_INFO.subject + '\n' + para_INFO.teacher + '\n' + para_INFO.type.split(',')[0] + '\n' + teacher_dictionary[para_INFO.teacher] + '\n' + str(para_INFO.hour)
	#str(para_INFO.day) == str(tooday)+' '+str(week) and str(datetime.now().time().strftime("%H:%M")) == time_dictionary[str(para_INFO.hour.split('-')[0])]:
	#print( type( ))
	#print('cur time', datetime.now().time().strftime("%H:%M"))
	if str(para_INFO.day) == str(tooday)+' '+str(week) and str(datetime.now().time().strftime("%H:%M")) == time_dictionary[str(para_INFO.hour.split('-')[0])]:
		bot.send_message(-1001408795989, messageForSend)
		


@bot.message_handler(commands=['auth'])
def send_auth(message):
    pass

bot.polling()
#-1001240637697 test
#-1001408795989 prod