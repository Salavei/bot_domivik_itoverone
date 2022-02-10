from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from main import *
import datetime
from keyboards.inline.inline_keyboards import *
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from main import *

from handlers.callback.callback_handler import *


class FSMrequest_sell(StatesGroup):
    name_request = State()
    number_request = State()


@dp.callback_query_handler(lambda c: 'soell_requests_an_' in c.data)
async def request_sell_start(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['id_an_sell'] = callback_query.data.split('_')[-1]
    await FSMrequest_sell.name_request.set()
    await callback_query.message.edit_text('Введите Ваше имя:')


@dp.message_handler(state=FSMrequest_sell.name_request)
async def request_sell_load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMrequest_sell.next()
    await message.answer('☎️ Номер телефона:')


@dp.message_handler(lambda message: not message.text[1:].isdigit(), state=FSMrequest_sell.number_request)
async def request_sell_load_phone_invalid_dd(message: types.Message):
    return await message.reply("⚠️ Номер должен быть формата: +375297642930!!")


@dp.message_handler(lambda message: message.text[1:].isdigit(), state=FSMrequest_sell.number_request)
async def request_sell_load_phone_dd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await message.answer('✅ Заявка оставлена')
    db.add_request_sell(data['id_an_sell'], data['phone'], data['name'])
    await state.finish()


class FSMrequest_rent(StatesGroup):
    name_request = State()
    number_request = State()


@dp.callback_query_handler(lambda c: 'rient_requests_an_' in c.data)
async def request_rent_start(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['id_an_rent'] = callback_query.data.split('_')[-1]
    await FSMrequest_rent.name_request.set()
    await callback_query.message.edit_text('Введите Ваше имя:')


@dp.message_handler(state=FSMrequest_rent.name_request)
async def request_rent_load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMrequest_rent.next()
    await message.answer('☎️ Номер телефона:')


@dp.message_handler(lambda message: not message.text[1:].isdigit(), state=FSMrequest_rent.number_request)
async def request_rent_load_phone_invalid(message: types.Message):
    return await message.reply("⚠️ Номер должен быть формата: +375297642930!!")


@dp.message_handler(lambda message: message.text[1:].isdigit(), state=FSMrequest_rent.number_request)
async def request_rent_load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await message.answer('✅ Заявка оставлена')
    db.add_request_rent(data['id_an_rent'], data['phone'], data['name'])
    await state.finish()


class FSMsell(StatesGroup):
    price = State()
    number_of_rooms = State()
    street = State()
    rent_description = State()
    phone = State()
    placed = State()
    photo = State()
    print('Start sell')


@dp.callback_query_handler(lambda c: 'sell' in c.data)
async def sell_start(callback_query: types.CallbackQuery):
    await FSMsell.price.set()
    await callback_query.message.edit_text('Введите стоимость:')


@dp.message_handler(state=FSMsell.price)
async def write_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await FSMsell.next()
    await message.answer('Введие колличество комнат:')


@dp.message_handler(state=FSMsell.number_of_rooms)
async def write_number_of_rooms(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_of_rooms'] = message.text
    await FSMsell.next()
    await message.answer('Введите район и адрес:')


@dp.message_handler(state=FSMsell.street)
async def write_street(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['street'] = message.text
    await FSMsell.next()
    await message.answer('Описание:')


@dp.message_handler(state=FSMsell.rent_description)
async def write_rent_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['rent_description'] = message.text
    await FSMsell.next()
    await message.answer('Ваш номер телефона:')


@dp.message_handler(lambda message: not message.text[1:].isdigit(), state=FSMsell.phone)
async def write_phone_invalid(message: types.Message):
    return await message.answer("⚠️ Номер должен быть формата: +375297642930!!")


@dp.message_handler(lambda message: message.text[1:].isdigit(), state=FSMsell.phone)
async def write_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await FSMsell.next()
    await message.answer('Выберите кто выкладывает объявление:', reply_markup=await choice_seller())


@dp.callback_query_handler(lambda call: "owner" or "agent" in call.data, state=FSMsell.placed)
async def write_placed(call: types.CallbackQuery, state: FSMContext):
    choice = {
        'owner': True,
        'agent': False,
    }
    async with state.proxy() as data:
        data['placed'] = choice.get(call.data)
    await FSMsell.next()
    await call.message.answer('Загрузите фото квартиры:')


@dp.message_handler(content_types=['photo'], state=FSMsell.photo)
async def write_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMsell.next()
    await message.answer('✅ Обьявление добавлено')
    db.add_announcements_sell(data['price'], data['number_of_rooms'], data['street'], data['rent_description'],
                              data['phone'], data['photo'], placed=data['placed'],
                              date_time=str(datetime.datetime.now()),
                              tg_id=message.from_user.id, )
    await state.finish()


class FSMrent(StatesGroup):
    price = State()
    number_of_rooms = State()
    street = State()
    rent_description = State()
    phone = State()
    placed = State()
    photo = State()
    print('Start rent')


@dp.callback_query_handler(lambda c: 'rent_create' in c.data)
async def rent_start(callback_query: types.CallbackQuery):
    await FSMrent.price.set()
    await callback_query.message.edit_text('Введите стоимость:')


@dp.message_handler(state=FSMrent.price)
async def rent_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await FSMrent.next()
    await message.answer('Тип комнаты(проходная, отдельная, подселение):')


@dp.message_handler(state=FSMrent.number_of_rooms)
async def rent_number_of_rooms(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_of_rooms'] = message.text
    await FSMrent.next()
    await message.answer('Введите район и адрес:')


@dp.message_handler(state=FSMrent.street)
async def rent_street(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['street'] = message.text
    await FSMrent.next()
    await message.answer('Описание:')


@dp.message_handler(state=FSMrent.rent_description)
async def rent_rent_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['rent_description'] = message.text
    await FSMrent.next()
    await message.answer('Ваш номер телефона:')


@dp.message_handler(lambda message: not message.text[1:].isdigit(), state=FSMrent.phone)
async def rent_phone_invalid(message: types.Message):
    return await message.answer("⚠️ Номер должен быть формата: +375297642930!!")


@dp.message_handler(lambda message: message.text[1:].isdigit(), state=FSMrent.phone)
async def rent_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await FSMrent.next()
    await message.answer('Выберите кто выкладывает объявление:', reply_markup=await choice_seller())


@dp.callback_query_handler(lambda call: "owner" or "agent" in call.data, state=FSMrent.placed)
async def rent_placed(call: types.CallbackQuery, state: FSMContext):
    choice = {
        'owner': True,
        'agent': False,
    }
    async with state.proxy() as data:
        data['placed'] = choice.get(call.data)
    await FSMrent.next()
    await call.message.answer('Загрузите фото комнаты:')


@dp.message_handler(content_types=['photo'], state=FSMrent.photo)
async def rent_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMrent.next()
    await message.answer('✅ Обьявление добавлено')
    db.add_announcements_rent(data['price'], data['number_of_rooms'], data['street'], data['rent_description'],
                              data['phone'], data['photo'], placed=data['placed'],
                              date_time=str(datetime.datetime.now()),
                              tg_id=message.from_user.id, )
    await state.finish()


class FSMdomovik(StatesGroup):
    confirm = State()
    first_name = State()
    last_name = State()
    city = State()
    region = State()
    district = State()
    number_house = State()
    street = State()
    entrance = State()
    floor = State()
    apartment = State()
    number_phone = State()
    car = State()

    print('Start domovik')


async def start_domovik(message: types.Message):
    await FSMdomovik.confirm.set()
    await message.answer('Подтвердите:')


@dp.message_handler(state=FSMdomovik.confirm)
async def name_write_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['confirm'] = message.text
    await FSMdomovik.next()
    await message.answer('Введие Имя:')


@dp.message_handler(state=FSMdomovik.first_name)
async def first_name_write_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
    await FSMdomovik.next()
    await message.answer('Введите вашу фамилию:')


@dp.message_handler(state=FSMdomovik.last_name)
async def last_name_write_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
    await FSMdomovik.next()
    await message.answer('Введите вашу город:')


@dp.message_handler(state=FSMdomovik.city)
async def city_write_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await FSMdomovik.next()
    await message.answer('Введите вашу область:')


@dp.message_handler(state=FSMdomovik.region)
async def region_write_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text
    await FSMdomovik.next()
    await message.answer('Введите ваш район:')


@dp.message_handler(state=FSMdomovik.district)
async def district_write_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['district'] = message.text
    await FSMdomovik.next()
    await message.answer('Введите номер дома:')


@dp.message_handler(state=FSMdomovik.number_house)
async def number_house_write_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_house'] = message.text
    await FSMdomovik.next()
    await message.answer('Введите название улицы:')


@dp.message_handler(state=FSMdomovik.street)
async def street_write_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['street'] = message.text
    await FSMdomovik.next()
    await message.answer('Введите ваш подъезд:')


@dp.message_handler(state=FSMdomovik.entrance)
async def entrance_write_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['entrance'] = message.text
    await FSMdomovik.next()
    await message.answer('Введите ваш этаж')


@dp.message_handler(state=FSMdomovik.floor)
async def floor_write_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['floor'] = message.text
    await FSMdomovik.next()
    await message.answer('Введите номер квартиры')


@dp.message_handler(state=FSMdomovik.apartment)
async def apartment_write_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['apartment'] = message.text
    await FSMdomovik.next()
    await message.answer('Введите номер телефона')


@dp.message_handler(state=FSMdomovik.number_phone)
async def number_phone_write_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number_phone'] = message.text
    await FSMdomovik.next()
    await message.answer('Введите номер машины')


@dp.message_handler(state=FSMdomovik.car)
async def car_write_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['car'] = message.text
    await message.answer('✅ Вы зарегестрировались')
    print('message.from_user.id', message.from_user.id)
    db.add_subscriber(message.from_user.id, data['confirm'], data['first_name'], data['last_name'], data['city'],
                      data['region'], data['district'], data['number_house'], data['street'],
                      data['entrance'], data['floor'], data['apartment'], data['number_phone'], data['car'])
    await state.finish()


class FSMAannouncement(StatesGroup):
    type_of_services = State()
    job_title = State()
    job_description = State()
    salary = State()
    phone = State()
    print('Start объявления')


@dp.callback_query_handler(lambda c: c.data == 'create')
async def cm_start1(callback_query: types.CallbackQuery):
    await FSMAannouncement.type_of_services.set()
    await callback_query.message.edit_text('Выберите тип работы')
    await callback_query.message.edit_reply_markup(reply_markup=await add_announcement())


@dp.callback_query_handler(lambda call: "work" or "so_work" in call.data, state=FSMAannouncement.type_of_services)
async def choice_work_user(call: types.CallbackQuery, state: FSMContext):
    choice = {
        'work': '👔 Работа',
        'so_work': '🦺 Подработка'
    }
    await state.update_data(type_of_services=choice[call.data])
    await FSMAannouncement.next()
    await call.message.edit_text(text="Введите название вакансии")


@dp.message_handler(state=FSMAannouncement.job_title)
async def load_job_title_invalid(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['job_title'] = message.text
    await FSMAannouncement.next()
    await message.answer('Введите описание вакансии')


@dp.message_handler(state=FSMAannouncement.job_description)
async def load_job_description(message: types.Message, state: FSMContext):
    if len(message.text) <= 55:
        async with state.proxy() as data:
            data['job_description'] = message.text
        await FSMAannouncement.next()
        await message.answer('💰 ЗП(подсказка: "20 в день, 10 в час, 600 за 21 день")')
    else:
        await message.answer('❌ Слишком большое описание.Не более 55 символов')


@dp.message_handler(state=FSMAannouncement.salary)
async def load_salary(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['salary'] = message.text
    await FSMAannouncement.next()
    await message.answer('☎️ Номер телефона')


@dp.message_handler(lambda message: not message.text[1:].isdigit(), state=FSMAannouncement.phone)
async def load_phone_invalid(message: types.Message):
    return await message.reply("⚠️ Номер должен быть формата: +375297642930!!")


@dp.message_handler(lambda message: message.text[1:].isdigit(), state=FSMAannouncement.phone)
async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await message.answer('✅ Обьявление добавлено')
    db.add_announcements(data['type_of_services'], data['job_title'], data['job_description'], data['salary'],
                         data['phone'], user_id=message.from_user.id)
    await state.finish()


class FSMresume(StatesGroup):
    name = State()
    skills = State()
    area_of_residence = State()
    phone = State()
    print('Start Резюме')


@dp.callback_query_handler(lambda c: c.data == 'edit_one')
async def cm_start(callback_query: types.CallbackQuery):
    await FSMresume.name.set()
    await callback_query.message.edit_text(text="👤 Введите Ваше Имя:")


@dp.message_handler(state=FSMresume.name)
async def load_type_work(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMresume.next()
    await message.answer('🪛 Опишите Ваши навыки:')


@dp.message_handler(state=FSMresume.skills)
async def load_job_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['skills'] = message.text
    await FSMresume.next()
    await message.answer('🌍 Ваш район проживания:')


@dp.message_handler(state=FSMresume.area_of_residence)
async def load_job_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['area_of_residence'] = message.text
    await FSMresume.next()
    await message.answer('☎️ Ваш номер телефона:')


@dp.message_handler(lambda message: not message.text[1:].isdigit(), state=FSMresume)
async def load_phone_invalid(message: types):
    return await message.reply("⚠️ Номер должен быть формата: +375297642930!!")


@dp.message_handler(lambda message: message.text[1:].isdigit(), state=FSMresume.phone)
async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await message.answer('✅ Резюме добавлено')
    data_d = {
        True: db.update_resume_my,
        False: db.add_resume
    }
    # TypeError: object sqlite3.Cursor can't be used in 'await' expression
    bool_db = bool(db.get_resume_my(message.from_user.id))
    await data_d[bool_db](data['name'], data['skills'], data['area_of_residence'],
                          data['phone'], user_id=message.from_user.id)
    await state.finish()


class FSMfeedback(StatesGroup):
    text = State()


async def start_feedback(message: types.Message):
    await FSMfeedback.text.set()
    await message.answer('Оставьте Ваш отзыв или напишите о недоработке:')


@dp.message_handler(state=FSMfeedback.text)
async def write_feedback(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
    await message.answer('✅ Спасибо!!')
    db.give_feedback(message.from_user.id, data['text'])
    await state.finish()


class FSMcar_sub_unit(StatesGroup):
    number_car = State()


async def start_car_sub_unit(message: types.Message):
    await FSMcar_sub_unit.number_car.set()
    await message.answer('Напишите номер машины:')


@dp.message_handler(state=FSMcar_sub_unit.number_car)
async def write_feedback(message: types.Message, state: FSMContext):
    if db.try_search_car_owner(message.text):
        await bot.send_message(db.successful_search_car_owner(message.text)[0], text='Вы подперли машину')
        await message.answer(f'Написали владельцу автомобиля!!')
    else:
        await message.answer('Машины не существует')
    await state.finish()
