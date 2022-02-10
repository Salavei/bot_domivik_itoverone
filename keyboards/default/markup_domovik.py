from aiogram.types import KeyboardButton
from aiogram import types

btn_my_neighbors = KeyboardButton("Мои соседи")
btn_jkh = KeyboardButton("ЖКХ")
btn_map_region = KeyboardButton("Карта района",  request_location=True)
btn_neighbors_card = KeyboardButton("Карточки соседей")
btn_my_card = KeyboardButton("Моя карточка")
btn_edit_me = KeyboardButton("Редактировать о себе")
btn_spravka = KeyboardButton("Справка")
btn_offers_for_me = KeyboardButton("Предложения для меня")

keyboard_main_domovik = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_main_domovik.add(btn_my_neighbors, btn_jkh, btn_map_region, btn_neighbors_card, btn_my_card,
                          btn_edit_me, btn_spravka, btn_offers_for_me)

# Кнопки предложения для меня с вакансиями

btn_back = KeyboardButton("🔙")
btn_go_house = KeyboardButton("Недвижимость")
btn_go_vacancy = KeyboardButton("Вакансии")

keyboard_offers = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_offers.add(btn_back, btn_go_house, btn_go_vacancy)


btn_laws_jkh = KeyboardButton("Законы")
btn_schedule_jkh = KeyboardButton("Расписание уборок")
btn_mouthpiece_jkh = KeyboardButton("Рупор для ЖКХ")
btn_sub_unit_the_car = KeyboardButton("Подпёр авто")
btn_back = KeyboardButton("🔙")

btn_go_jkh = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn_go_jkh.add(btn_back, btn_sub_unit_the_car, btn_laws_jkh, btn_schedule_jkh, btn_mouthpiece_jkh)