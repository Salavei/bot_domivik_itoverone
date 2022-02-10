from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def keyboards_fsm_domovik_user() -> InlineKeyboardMarkup:
    """Подтверждение fsm"""
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'Подтвверждаю', callback_data=f'pryve'),
            ]
        ]
    )
    return keyboard


async def keyboards_fsm_domovik_car() -> InlineKeyboardMarkup:
    """Подтверждение fsm машины"""
    keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(f'Есть машина', callback_data=f'Yes_car'),
                InlineKeyboardButton(f'Нет машины', callback_data=f'No_car'),
            ]
        ]
    )
    return keyboard
