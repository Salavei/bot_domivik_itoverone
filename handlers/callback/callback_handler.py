from main import *
from aiogram import types


###Оставить заявку на объявлении

@dp.callback_query_handler(lambda call: 'requests_an_' in call.data)
async def requests_an_user(call: types.CallbackQuery):
    #тут будет то, куда будет идти заявка
    await call.message.answer(text="Заявка отправлена")

###Пользователь активирует и деактивирует объявления
@dp.callback_query_handler(lambda call: 'rent_stop_start_an_' in call.data)
async def stop_start_an_rent_user(call: types.CallbackQuery):
    print(call.data.split('_')[-1])
    db.confirm_announcements_rent_user(call.data.split('_')[-1], not db.start_my_announcements_rent(call.data.split('_')[-1]))
    await call.message.edit_text(text="☑️")


@dp.callback_query_handler(lambda call: 'stop_start_an_' in call.data)
async def stop_start_an_sell_user(call: types.CallbackQuery):
    print(call.data.split('_')[-1])
    db.confirm_announcements_sell_user(call.data.split('_')[-1], not db.start_my_announcements_sell(call.data.split('_')[-1]))
    await call.message.edit_text(text="☑️")

#Пользователь удаляет объявления

@dp.callback_query_handler(lambda call: 'ddd_rent_dell_an_' in call.data)
async def user_an_rent_dell(call: types.CallbackQuery):
    db.dell_an_rent_user(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️Удалено")

@dp.callback_query_handler(lambda call: 'ssssssdell_an_' in call.data)
async def user_an_sell_dell_sell(call: types.CallbackQuery):
    db.dell_an_sell_user(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️Удалено")
######Админ удаляет объявления
@dp.callback_query_handler(lambda call: 'dell_rent_admin_an_' in call.data)
async def admin_an_rent_dell(call: types.CallbackQuery):
    db.dell_an_rent_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️Отклонено")

@dp.callback_query_handler(lambda call: 'an_admin_dell_' in call.data)
async def admin_an_sell_dell(call: types.CallbackQuery):
    db.dell_an_sell_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️Отклонено")

#######Админ одобряет объявления
@dp.callback_query_handler(lambda call: 'seeel_admin_start_an_' in call.data)
async def admin_start_an_sell(call: types.CallbackQuery):
    print('sell', call.data.split('_')[-1])
    db.confirm_announcements_sell_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️Одобрено️")

@dp.callback_query_handler(lambda call: 'rent_admin_start_an_' in call.data)
async def admin_start_an_rent(call: types.CallbackQuery):
    print('rent', call.data.split('_')[-1])
    db.confirm_announcements_rent_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="☑️Одобрено")








# Вакансии


@dp.callback_query_handler(lambda call: 'start_stop_' in call.data)
async def approve_start_end_my_resume(call: types.CallbackQuery):
    db.update__my_resume(call.data.split('_')[-1], not db.start_my_resume(call.data.split('_')[-1]))
    await call.message.edit_text(text="☑️")


@dp.callback_query_handler(lambda call: 'stop_start_an_' in call.data)
async def approve_announcement_user(call: types.CallbackQuery):
    db.update_announcements(call.data.split('_')[-1], not db.check_announcements(call.data.split('_')[-1]))
    await call.message.edit_text(text="☑️")


# ADMIN CALLBACK
@dp.callback_query_handler(lambda call: 'confirm_r_admin_' in call.data)
async def approve_resume_admin(call: types.CallbackQuery):
    db.confirm_resume_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="Резюме одобрено 👍")


@dp.callback_query_handler(lambda call: 'reject_r_admin_' in call.data)
async def reject_resume_admin(call: types.CallbackQuery):
    db.reject_db_resume_admin(call.data.split('_')[-1])
    await call.message.edit_text(text='Резюме откланено 👎')

@dp.callback_query_handler(lambda call: 'confirm_a_admin_' in call.data)
async def approve_announcement_admin(call: types.CallbackQuery):
    db.confirm_announcements_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="Объявление одобрено 👍")


@dp.callback_query_handler(lambda call: 'reject_a_admin_' in call.data)
async def reject_announcement_admin(call: types.CallbackQuery):
    db.reject_db_announcement_admin(call.data.split('_')[-1])
    await call.message.edit_text(text="Объявление откланено 👎")

##################################