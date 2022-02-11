from main import *
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.funk_async import *
from filter.admin import IsAdmin
from utils.funk_async_domovik import *

from utils.privacy import privacy
from fsm.fsm import start_domovik, start_feedback, start_car_sub_unit, update_user_domovik


# admin


@dp.message_handler(commands=['admin'])
async def command_start(message: types.Message):
    if not await IsAdmin().check(message):
        if not db.why_get_admin(message.from_user.id):
            db.get_admin(message.from_user.id, True)
            await message.answer('⚠️ Вход в админ режим ⚠️', reply_markup=keyboard_admin)
        else:
            db.get_admin(message.from_user.id, False)
            await message.answer('❌ Выход из админ режима ❌', reply_markup=keyboard_main_domovik)
    else:
        db.get_admin(message.from_user.id, False)
        await message.answer('❌ Вы не админ, команда не будет работать ❌', reply_markup=keyboard_main_domovik)


# ОБьявления для апрува от админа

async def get_all_announcement_for_adm(message: types.Message):
    if not db.get_announcement_for_adm():
        await message.answer(f'❌ Нет объявлений для апрува ‼️')
    else:
        for unp in db.get_announcement_for_adm():
            id, type_of_services, job_title, job_description, salary, phone, allow, _, _, _ = unp
            await message.answer(
                f"Тип: {type_of_services}\nНазвание вакансии: {job_title}\nОписание вакансии: {job_description}\n💰 Заработная Плата: {salary}\n☎️ Номер телефона: {phone}",
                reply_markup=await get_confirm_announcement_admin(id))


async def get_all_resume_for_adm(message: types.Message):
    if not db.get_resume_for_adm():
        await message.answer(f'❌ Нет резюме для апрува ‼️')
    else:
        for unp in db.get_resume_for_adm():
            id_resume, name, skills, area_of_residence, phone, allow, _, _, _ = unp
            await message.answer(
                f"👤 Имя: {name}\n🪛 Навыки: {skills}\n🌍 Район проживания: {area_of_residence}\n☎️ Номер телефона: {phone}",
                reply_markup=await get_confirm_admin_resume(id_resume))


async def get_all_feedback_for_adm(message: types.Message):
    if not db.show_all_feedback():
        await message.answer(f'❌ Нет обратной связи ‼️')
    else:
        for unp in db.show_all_feedback():
            text = unp[0]
            await message.answer(
                f"🪛 {text}\n")


# end admin


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if db.check_subscriber(message.from_user.id):
        await message.answer(f'🔙🔙', reply_markup=keyboard_main_domovik)
    else:
        await message.answer(f'Добро пожаловать , пройдите регистрацию!!')
        await start_domovik(message)


async def error(message: types.Message):
    await message.delete()


async def send_privacy(message):
    await message.answer(f'{privacy}')


@dp.message_handler(content_types=['text'])
async def command_start_text(message: types.Message):
    data = {
        # Домовик
        'Мои соседи': give_neighbors_card,
        'ЖКХ': give_all_jkh,
        'Карта района': geo,
        'Карточки соседей': give_neighbors_card,
        'Моя карточка': give_my_card,
        'Вакансии': give_all_target_vacancy,
        'Редактировать о себе': update_user_domovik,
        'Справка': start_feedback,
        'Недвижимость': give_all_target_house,
        'Предложения для меня': give_all_target,
        'Законы': all_laws_jkh,
        'Подпёр авто': start_car_sub_unit,

        # Недвижимость
        'Правила размещения и конфедициальность': give_keybord,
        'Сдается': show_all_rent,
        'Заявки на аренду': rental_requests,
        'Продается': show_all_sell,
        'Мои объявления продажи': show_all_my_sell,
        'Мои объявления аренды': show_all_my_rent,
        'Заявки на покупку': purchasing_request,
        'Политика конфеденциальности': konfendentsialnost,
        'Правила размещения': rule,
        'Сроки размещения': term,
        'Создать объявление': dell_up,
        '🔙': bot_start,

        # вакансии
        'Список предложений': all_my_announcement,
        'Мои обьявления': my_announcement,
        'Мое Резюме': my_resume,
        'Все Резюме': get_all_resume,
        'Конфиденциальность': send_privacy,

    }
    data_admin = {
        'Объявления для Верификации': get_all_announcement_for_adm,
        'Резюме для Верификации': get_all_resume_for_adm,
        'Подтверждение Продажи': confirmation_of_sales,
        'Подтверждение Аренды': confirmation_of_rent,
        'Обратная связь': get_all_feedback_for_adm,

    }
    await data.get(message.text, error)(message)
    await data_admin.get(message.text, error)(message)
