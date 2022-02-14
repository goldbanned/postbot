import warnings #чтобы убрать предупреждения
from random import randint as ran #рандомайзер
from selenium import webdriver #сам selenium
from time import sleep #ожидание
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime
import os
bot = Bot(token='5057146163:AAGKhrdpYLTae6VqranqRt0zvZMHimAV1O4')
dp = Dispatcher(bot)
channel_id = '-1001547411552'
today = datetime.datetime.today()


async def process_start_command(message: types.Message):
    #await bot.send_message(channel_id, 'Parser csgorun.gg by @gold_banned')
    
    warnings.filterwarnings("ignore") #чтобы убрать предупреждения
    from selenium.webdriver.firefox.options import Options #доп функции
    
    options = webdriver.ChromeOptions() #переменная с функциями
    options.add_argument('--headless') #невидимое окно (можешь убрать, так ты будешь видеть процесс работы)
    #driver = webdriver.Firefox(options=options, executable_path=r"geckodriver.exe") #прога для запуска firefoxа
    options.binary_location = os.environ.get('GOOGLE_CHROME_SHIM', None)
    driver = webdriver.Chrome(options=options, executable_path="chromedriver") #прога для запуска chromа
    driver.get('https://csgorun.gg') #запуск сайта
    last_game = '' #последний кф
    driver.find_element_by_class_name("switcher__content").click() #нажимаем на подтверждение 18 лет
    while True: #бесконечный цикл
        offset = datetime.timedelta(hours=3)
        today = datetime.datetime.now(datetime.timezone(offset, name='МСК'))
        if driver.find_element_by_class_name("graph-label").text[:-2] != last_game: #если последняя игра не равняется переменной с последней сохраненной игрой то
            if driver.find_element_by_class_name("graph-label").get_attribute('style')[23:-1] == "2B3D6D":
                await bot.send_message(channel_id,'🔵 ' + driver.find_element_by_class_name("graph-label").text + ' '+ str(today.strftime("%H:%M:%S %d.%m.%Y")) + r" #B")
            if driver.find_element_by_class_name("graph-label").get_attribute('style')[23:-1] == "4e2d6a":
                await bot.send_message(channel_id, "🟣 " + driver.find_element_by_class_name("graph-label").text + ' '+ str(today.strftime("%H:%M:%S %d.%m.%Y")) + r" #P")
            if driver.find_element_by_class_name("graph-label").get_attribute('style')[23:-1] == "492a49":
                await bot.send_message(channel_id, "🔴 " + driver.find_element_by_class_name("graph-label").text + ' '+ str(today.strftime("%H:%M:%S %d.%m.%Y")) + r" #R")
            if driver.find_element_by_class_name("graph-label").get_attribute('style')[23:-1] == "255559":
                await bot.send_message(channel_id, "🟢 " + driver.find_element_by_class_name("graph-label").text + ' '+ str(today.strftime("%H:%M:%S %d.%m.%Y")) + r" #G")
            if driver.find_element_by_class_name("graph-label").get_attribute('style')[23:-1] == "007c91":
                await bot.send_message(channel_id, "💎 " + driver.find_element_by_class_name("graph-label").text + ' '+ str(today.strftime("%H:%M:%S %d.%m.%Y")) + r" #S")
            if driver.find_element_by_class_name("graph-label").get_attribute('style')[23:-1] == "4e3b4b":
                await bot.send_message(channel_id, "🟡 " + driver.find_element_by_class_name("graph-label").text + ' '+ str(today.strftime("%H:%M:%S %d.%m.%Y")) + r" #Y")
           
            
            last_game = driver.find_element_by_class_name("graph-label").text[:-2] #задаем переменную значением последней игрой чтобы не писал одно и тоже
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=process_start_command)
