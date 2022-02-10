from aiogram.types import KeyboardButton
from aiogram import types

# main_user button #

btnprivacy = KeyboardButton('Конфиденциальность')
btnoffers = KeyboardButton('Список предложений')
btnannouncement = KeyboardButton('Мои обьявления')
btnresume = KeyboardButton('Мое Резюме')
btn_all_resume = KeyboardButton('Все Резюме')
btn_back = KeyboardButton("🔙")
keyboard_vac = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_vac.add(btn_back, btnprivacy, btnoffers, btnannouncement, btnresume, btn_all_resume)

# admin button
admin_resume = KeyboardButton('Объявления для Верификации')
admin_announcement = KeyboardButton('Резюме для Верификации')

keyboard_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_admin.add(admin_resume, admin_announcement)

# user_button
btn_rule_konfendentsialnosts = KeyboardButton("Правила размещения и конфедициальность")
btn_konfendentsialnost = KeyboardButton("Политика конфеденциальности")
btn_rule = KeyboardButton("Правила размещения")
btn_term = KeyboardButton("Сроки размещения")
btn_dell_up = KeyboardButton("Создать объявление")
btn_back = KeyboardButton("🔙")

keyboard_rule_konfendentsialnost = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_rule_konfendentsialnost.add(btn_back, btn_konfendentsialnost, btn_rule, btn_term, btn_dell_up)
# user_button_dell_up
btn_create_an = KeyboardButton('Создать объявление')
btn_back_create_an = KeyboardButton("🔙")
keyboards_create = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboards_create.add(btn_create_an, btn_back_create_an)
# main_button
btn_is_given = KeyboardButton("Сдается")

btn_my_sell = KeyboardButton("Мои объявления продажи")
btn_my_rent = KeyboardButton("Мои объявления аренды")

btn_requisition_arend = KeyboardButton("Заявки на аренду")
btn_sell = KeyboardButton("Продается")
btn_requisition_buy = KeyboardButton("Заявки на покупку")
btn_back = KeyboardButton("🔙")



keyboard_rule_konfendentsialnost = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_rule_konfendentsialnost.add(btn_konfendentsialnost, btn_rule, btn_term, btn_dell_up, btn_back)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(btn_back, btn_rule_konfendentsialnosts, btn_is_given, btn_my_sell, btn_my_rent, btn_requisition_arend, btn_sell,
             btn_requisition_buy)

#admin button
admin_resume = KeyboardButton('Объявления для Верификации')
admin_announcement = KeyboardButton('Резюме для Верификации')
btn_confirming_sell = KeyboardButton("Подтверждение Продажи")
btn_confirming_arend = KeyboardButton("Подтверждение Аренды")

keyboard_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_admin.add(btn_confirming_sell, btn_confirming_arend, admin_resume, admin_announcement)

