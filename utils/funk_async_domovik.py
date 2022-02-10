import types

from main import db, bot
from keyboards.default.markup import *
from keyboards.inline.inline_keyboards import *
from keyboards.default.markup_domovik import *

from keyboards.default.markup import keyboard


async def give_all_target(message: types.Message):
    await message.reply(text='Правила размещения и конфедициальность', reply_markup=keyboard_offers)


async def give_all_target_house(message: types.Message):
    await message.reply(text='Правила размещения и конфедициальность', reply_markup=keyboard)


async def give_all_target_vacancy(message: types.Message):
    await message.answer(f'Привет, быстрее начни мной пользоваться!', reply_markup=keyboard_vac)


async def give_all_jkh(message: types.Message):
    await message.reply(text='Правила размещения и конфедициальность', reply_markup=btn_go_jkh)


async def give_my_card(message: types.Message):
    for un in db.give_subscriber_card(message.from_user.id):
        _, _, _, name, last_name, city, region, district, number_house, street, entrance, floor, apartment, number_phone, car, _ = un
        await message.reply(
            text=f'Имя {name} Фамилия {last_name} \nНомер телефона {number_phone} \nМашина {car} \nОбласть {region} \nГород {city} '
                 f' \nУлица {street} \nНомер дома {district} \nНомер подъезда {entrance} \nЭтаж {floor} \nКвартира {apartment}')
#
# async def for_give_feedback(message: types.Message):
#     # db.give_feedback(tg_id, user_text)
#     await start_feedback(message)


async def all_laws_jkh(message: types.Message):
    await message.answer(f"Ссылка на портал о законах ЖКХ\nhttps://gkx.by/baza-znanij/normativno-pravovye-dokumenty/ofitsialnye-dokumenty")
# https://gkx.by/baza-znanij/normativno-pravovye-dokumenty/ofitsialnye-dokumenty