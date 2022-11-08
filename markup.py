from gc import callbacks
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

# ---Main menu button---
btnMain = KeyboardButton(text='Main menu', callback_data="mainMenu")

# ---Main menu---
btnVns = KeyboardButton(text='VNS', callback_data="vns")
btnStudent = KeyboardButton(
    text='Student NULP', callback_data="studentprofile")
btnHostels = KeyboardButton(text='Hostels', callback_data="hostels")
btnKampus = KeyboardButton(text='Kampus', callback_data="campus")
btnSocial = KeyboardButton(text='Social Networks', callback_data="sn")
btnTeacher = KeyboardButton(text='Teacher', callback_data="teacher")
btnSticker = KeyboardButton(text='Stickers',callback_datat ="stickers")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    btnVns, btnStudent, btnHostels, btnKampus, btnSocial,btnTeacher,btnSticker)

btnHelp = KeyboardButton(text='Help', callback_data='help')
keyboard2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(btnHelp)

# ---Hostels menu---
btnHostel1 = KeyboardButton(text='Hostel 1', callback_data='hostle_1')
btnHostel3 = KeyboardButton(text='Hostel 3', callback_data='hostle_3')
btnHostel4 = KeyboardButton(text='Hostel 4', callback_data='hostle_4')
btnHostel5 = KeyboardButton(text='Hostel 5', callback_data='hostle_5')
btnHostel7 = KeyboardButton(text='Hostel 7', callback_data='hostle_7')
btnHostel8 = KeyboardButton(text='Hostel 8', callback_data='hostle_8')
btnHostel9 = KeyboardButton(text='Hostel 9', callback_data='hostle_9')
btnHostel10 = KeyboardButton(text='Hostel 10', callback_data='hostle_10')
btnHostel11 = KeyboardButton(text='Hostel 11', callback_data='hostle_11')
btnHostel12 = KeyboardButton(text='Hostel 12', callback_data='hostle_12')
btnHostel14 = KeyboardButton(text='Hostel 14', callback_data='hostle_14')
btnHostel15 = KeyboardButton(text='Hostel 15', callback_data='hostle_15')
btnHostel17 = KeyboardButton(text='Hostel 17', callback_data='hostle_17')
hostelsMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    btnHostel1, btnHostel3, btnHostel4, btnHostel5, btnHostel7, btnHostel8, btnHostel9, btnHostel10, btnHostel11, btnHostel12, btnHostel14, btnHostel15, btnHostel17, btnMain)
