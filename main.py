from email import message
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import *
import markup as nav
import emoji
from flask import Flask

# Set Token in file named info.py
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

class Form(StatesGroup):
    name = State()

class Kampus(StatesGroup):
    number = State()

teachers = {'отенко' : 'info',
            'чубик' : 'inf'}

kampuses = {'1': 'link','2':'link2'}

kampuses_photo = {'1': 'link_for_photo','2':'link_for_photo2'}

@dp.message_handler(commands=['start'])
async def startCommand(message: types.Message):
    await message.reply(emoji.emojize("""
    Hello, student LPNU :mortar_board: !!! Welcome to ICTA-Explorer :microscope: !!!
    Please, tell your colleagues about our bot :speech_balloon: . 
    \n Choose your way
    """, language='alias'), reply_markup=nav.mainMenu)


@dp.message_handler()
async def helpCommand(message: types.Message):
    # Main functions reply
    if message.text == "help":
        await bot.send_message(message.from_user.id, "It's a resource that we are offering for you", reply_markup=nav.mainMenu)
    elif message.text == 'Student NULP':
        await bot.send_message(message.from_user.id, """
        It's a link to  your virtual profile in the lpnu system :\n https://student.lpnu.ua/  """, reply_markup=nav.mainMenu)
        await message.answer_photo('https://drive.google.com/file/d/1yL81Fgs2JdYL_A4sCSCAcA0KevXlCCv7/view?usp=share_link')
    elif message.text == 'VNS':
        await bot.send_message(message.from_user.id, """It's a link to  your workflow where you will be passed your exams and hometasks :\n http://vns.lpnu.ua/
        """, reply_markup=nav.mainMenu)
        await message.answer_photo("https://img.sur.ly/thumbnails/620x343/v/vns.lpnu.ua.png")
    elif message.text == 'Hostels':
        await bot.send_message(message.from_user.id, """Select hostel:""", reply_markup=nav.hostelsMenu)
    elif message.text == 'Kampus':
        await message.reply("Enter kampus number:")
        await Kampus.number.set()   
    elif message.text == 'Teacher':
        await message.reply("Enter teachers' name:")
        await Form.name.set() 
    elif message.text == 'Stickers':
        await bot.send_message(message.from_user.id, emoji.emojize("""
    \n EA Stickers :bomb: In progress
    \nLOLITECH :girl:  https://t.me/addstickers/LOLITEH\n RNB :boy: https://t.me/addstickers/Cyberbombb\n:mens:GACHI:mens: https://t.me/addstickers/video_gachi 
    \nCyberteachers :computer: https://t.me/addstickers/KIBERprepoDY \nCyberchildren:baby: https://t.me/addstickers/cyberfucks 
    """, language='alias'),  reply_markup=nav.mainMenu)
    # Reply Hostels
    #SUCCESS
    elif message.text == 'Hostel 1':
        await bot.send_message(message.from_user.id, "Google Maps:https://goo.gl/maps/kS4kVeBDCJCf1NuD7", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1uDuze4G27t4P_2mqayQJOjpyj_lP50ie/view?usp=share_link')
    #SUCCESS
    elif message.text == 'Hostel 3':
        await bot.send_message(message.from_user.id, "Google Maps:https://goo.gl/maps/BCraNEtDvzfgKUSt8", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/139gRCGvt1vLY_aeKIzA8BMA-WfI_oCLn/view?usp=share_link')
    elif message.text == 'Hostel 4':
        await bot.send_message(message.from_user.id, "Google Maps:https://goo.gl/maps/WddWygr2QFQoeMcu6", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1o1_RZID6xzs5aToG72deakgVkuWNbbuc/view?usp=share_link')
    elif message.text == 'Hostel 5':
        await bot.send_message(message.from_user.id, "Google Maps:https://goo.gl/maps/gNP8QfDfdnKWAweq7", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://media.lpnu.ua/system/files/styles/photo_watermark/private/photo/2017/dec/04/02/gurt08252016082.jpg?itok=t0aPCq9j')
    #SUCCESS
    elif message.text == 'Hostel 7':
        await bot.send_message(message.from_user.id, "Google Maps:https://goo.gl/maps/ZA4utEcnfwBggo3aA", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1zWXKZPkhGvV0XvV-3TuetA3-CceYPrM0/view?usp=share_link')
    #SUCCESS
    elif message.text == 'Hostel 8':
        await bot.send_message(message.from_user.id, "Google Maps:https://goo.gl/maps/2y1r1uuiVYpSGK9d9", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1rJ6yXd1pQ0oHCl4QNeYdM5gKqSc6Bs1x/view?usp=share_link')
    #SUCCESS
    elif message.text == 'Hostel 9':
        await bot.send_message(message.from_user.id, "Google Maps:https://goo.gl/maps/B86BPKjg145PGVVi7", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1s7TVr_vYRVBlpkp4dMw9Lt9E1I8XYr1B/view?usp=share_link')
    #SUCCESS
    elif message.text == 'Hostel 10':
        await bot.send_message(message.from_user.id, "Google Maps:https://goo.gl/maps/xALfBX2jrkefvVHWA", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1JzUvWeQot6_CNPkQSUxqnusyNUo9faTx/view?usp=share_link')
    #SUCCESS
    elif message.text == 'Hostel 11':
        await bot.send_message(message.from_user.id, "Google Maps:https://goo.gl/maps/ehdJsCiE2ieQP1Vf7", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1hKqXRtvBM3eKExWDuSo3gdrb89I4o9bS/view?usp=share_link')
    #SUCCESS
    elif message.text == 'Hostel 12':
        await bot.send_message(message.from_user.id, "Google Maps:https://goo.gl/maps/Dk2wE8FHxCygCB6B9", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1ySxjXeKmMr7JQDxtHjZkg2OZQPutYiE2/view?usp=share_link')
    #SUCCESS
    elif message.text == 'Hostel 14':
        await bot.send_message(message.from_user.id, "Google Maps:https://goo.gl/maps/v913LkuT74wApnmt6", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1LkT56iP6b5h6qyVUiJ-_wE_K8H6AazPP/view?usp=share_link')
    elif message.text == 'Hostel 15':
        await bot.send_message(message.from_user.id, "Google Maps:https://goo.gl/maps/vxpFCjJvuYKZWvqK8", reply_markup=nav.hostelsMenu)
        await message.answer_photo('http://photos.wikimapia.org/p/00/02/85/58/90_full.jpg')
    #SUCCESS
    elif message.text == 'Hostel 17':
        await bot.send_message(message.from_user.id, "Google Maps:https://goo.gl/maps/vxpFCjJvuYKZWvqK8", reply_markup=nav.hostelsMenu)
        await message.answer_photo('https://drive.google.com/file/d/1dP_eBtlf4MGA0IfC51UyRCVYAKW5XpKq/view?usp=share_link')
    elif message.text == 'Main menu':
        await bot.send_message(message.from_user.id, """Back to main menu!""", reply_markup=nav.mainMenu)
    # Social Networks reply
    elif message.text == 'Social Networks':
        await bot.send_message(message.from_user.id, emoji.emojize(
            """
<a href="https://facebook.com/lvivpolytechnic">Facebook</a> :mortar_board:
<a href="https://instagram.com/lpnu_official">Instagram</a> :camera: 
<a href="https://www.linkedin.com/school/lviv-polytechnic-national-university">Linkedin</a> :smile_cat: 
<a href="https://twitter.com/LvPolytechnic">Twitter</a>:bird: 
<a href="https://t.me/lpnu_official">Telegram NULP</a> : 
<a href="https://tiktok.com/@lpnu_official">Tik Tok</a> :video_camera: 
<a href="https://youtube.com/channel/UCYC38Wwv1IsozuymZitUKrw">You Tube</a> :movie_camera: 
<a href="https://t.me/nulp_wiki">Wiki NULP</a>:globe_with_meridians: 
<a href="https://t.me/profikta">Telegram IKTA</a> :gift_heart: 
<a href="https://t.me/students_nulp">Колегія та профком студентів і аспірантів НУ “ЛП”</a> :mortar_board: 
<a href="https://t.me/nulp_ikta">Телеграм чат студентів ІКТА</a> :school_satchel: 
<a href="https://facebook.com/lvivpolytechnic">Чати спеціальностей</a>:
    <a href="https://t.me/nulp_mt">МТ</a>:signal_strength: 
    <a href="https://t.me/nulp_kb">КБ</a> :computer: 
    <a href="https://t.me/nulp_ki">КІ</a> :iphone: 
    <a href="https://t.me/iot_nulp2021">ІР</a> :earth_americas: 
""", language='alias'),parse_mode="HTML" ,reply_markup=nav.mainMenu)


@dp.message_handler(state=Form.name)
async def teachersSearch(message: types.Message, state: FSMContext):
    # Finish our conversation
    second_name = str(message.text)
    info = teachers.get(second_name.lower())
    await message.reply(info)
    await state.finish()


@dp.message_handler(state=Kampus.number)
async def kampusesSearch(message: types.Message, state: FSMContext):
    # Finish our conversation
    number = message.text
    link = kampuses.get(number)
    link_photo = kampuses_photo.get(number)
    await message.reply(link_photo)
    await message.reply(link)
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
