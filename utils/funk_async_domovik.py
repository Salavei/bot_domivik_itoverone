import types

from main import db, bot
from keyboards.default.markup import *
from keyboards.inline.inline_keyboards import *
from keyboards.default.markup_domovik import *

from keyboards.default.markup import keyboard


async def give_all_target(message: types.Message):
    await message.reply(text='Все предложения для Вас', reply_markup=keyboard_offers)


async def give_all_target_house(message: types.Message):
    await message.reply(text='Предложения по недвижемости', reply_markup=keyboard)


async def give_all_target_vacancy(message: types.Message):
    await message.reply(f'Предложения по вакансиям', reply_markup=keyboard_vac)


async def give_all_jkh(message: types.Message):
    await message.reply(text='Раздел ЖКХ', reply_markup=btn_go_jkh)


async def give_my_card(message: types.Message):
    for un in db.give_subscriber_card(message.from_user.id):
        _, _, _, _, name, last_name, city, region, district, number_house, street, entrance, floor, apartment, number_phone, car = un
        await message.reply(
            text=f'Имя {name} Фамилия {last_name} \nНомер телефона {number_phone} \nМашина {car} \nОбласть {region} \nГород {city} '
                 f' \nУлица {street} \nНомер дома {district} \nНомер подъезда {entrance} \nЭтаж {floor} \nКвартира {apartment}')


async def give_neighbors_card(message: types.Message):
    street, number_house = db.take_my_cards(message.from_user.id)
    for un in db.take_all_cards_neighbors(street, number_house):
        _, _, _, _, name, last_name, city, region, district, number_house, street, entrance, floor, apartment, number_phone, car = un
        await message.reply(
            text=f'Имя {name}\nНомер телефона {number_phone}\nУлица {street}\nНомер дома {district}\nНомер подъезда {entrance}\nЭтаж {floor}')


async def geo(message: types.Message):
    await message.reply("Карта вашего района")


async def all_laws_jkh(message: types.Message):
    await message.answer(
        f"Ссылка на портал о законах ЖКХ\nhttps://gkx.by/baza-znanij/normativno-pravovye-dokumenty/ofitsialnye-dokumenty")

