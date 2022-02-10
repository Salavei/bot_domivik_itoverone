from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button = InlineKeyboardMarkup()


async def keyboards_announcements_rent(id_an, allow) -> InlineKeyboardMarkup:
    """Остановка/Активация и Удаления объявлений для пользователя"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'{allow}', callback_data=f'rent_stop_start_an_{id_an}'),
                InlineKeyboardButton('❌ Удалить', callback_data=f'ddd_rent_dell_an_{id_an}'),
            ]
        ]
    )
    return keyboard



async def keyboards_announcements(id_an, allow) -> InlineKeyboardMarkup:
    """Остановка/Активация и Удаления объявлений для пользователя"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'{allow}', callback_data=f'stop_start_an_{id_an}'),
                InlineKeyboardButton('❌ Удалить', callback_data=f'ssssssdell_an_{id_an}'),
            ]
        ]
    )
    return keyboard


async def requests_keyboards_announcements(id_an) -> InlineKeyboardMarkup:
    """Оставить заявку на объявлении аренды"""
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'Оставить заявку', callback_data=f'rient_requests_an_{id_an}'),
            ]
        ]
    )
    return keyboard

async def sell_requests_keyboards_announcements(id_an) -> InlineKeyboardMarkup:
    """Оставить заявку на объявлении продажи"""
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'Оставить заявку', callback_data=f'soell_requests_an_{id_an}'),
            ]
        ]
    )
    return keyboard

async def make_choice_announcements(*args) -> InlineKeyboardMarkup:
    """инлайн при создании объявления"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton('Продажа', callback_data='sell'),
                InlineKeyboardButton('Аренда', callback_data='rent_create'),
            ]
        ]
    )
    return keyboard

async def choice_seller(*args) -> InlineKeyboardMarkup:
    """инлайн при создании объявления"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton('Собственник', callback_data='owner'),
                InlineKeyboardButton('Агент', callback_data='agent'),
            ]
        ]
    )
    return keyboard

#admin keyboard

async def rent_admin_keyboards_announcements(id_an) -> InlineKeyboardMarkup:
    """Одобрить и Отклонить объявления для админа"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'✅ Одобрить', callback_data=f'rent_admin_start_an_{id_an}'),
                InlineKeyboardButton('❌ Отклонить', callback_data=f'dell_rent_admin_an_{id_an}'),
            ]
        ]
    )
    return keyboard

async def sell_admin_keyboards_announcements(id_an) -> InlineKeyboardMarkup:
    """Одобрить и Отклонить объявления для админа"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'✅ Одобрить', callback_data=f'seeel_admin_start_an_{id_an}'),
                InlineKeyboardButton('❌ Отклонить', callback_data=f'an_admin_dell_{id_an}'),
            ]
        ]
    )
    return keyboard






### ВАКАНСИИИИ

async def get_announce_edit(id, allow) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'{allow}', callback_data=f'stop_start_an_{id}'),
            ]

        ]
    )
    return keyboard

async def get_announce_create() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton('⚙️ Создать', callback_data='create'),
            ]

        ]
    )
    return keyboard

async def get_resumes_edit_keyboard(start_stop_state,id_resume) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f'{start_stop_state}', callback_data=f'start_stop_{id_resume}',), #Остановить/Активировать
                InlineKeyboardButton('⚙️ Изменить', callback_data='edit_one'),
             ]
        ]
    )
    return keyboard

async def get_resumes_none() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton('⚙️ Создать', callback_data='edit_one'),
             ]
        ]
    )
    return keyboard


async def get_announcement_admin() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton('✅ Одобрить', callback_data='confirm'),
             ]
        ]
    )
    return keyboard

async def get_confirm_admin_resume(id_resume) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton('✅ Одобрить', callback_data=f'confirm_r_admin_{id_resume}'),
                InlineKeyboardButton('❌ Отклонить', callback_data=f'reject_r_admin_{id_resume}')
             ]
        ]
    )
    return keyboard

async def get_confirm_announcement_admin(id_announcement) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton('✅ Одобрить', callback_data=f'confirm_a_admin_{id_announcement}'),
                InlineKeyboardButton('❌ Отклонить', callback_data=f'reject_a_admin_{id_announcement}')
             ]
        ]
    )
    return keyboard


async def add_announcement() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton('👔 Работа', callback_data='work'),
                InlineKeyboardButton('🦺 Подработка', callback_data='so_work'),
             ]
        ]
    )
    return keyboard


###################################