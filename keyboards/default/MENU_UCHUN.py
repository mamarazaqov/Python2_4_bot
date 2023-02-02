from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import obeykt



menular = obeykt.selecet_barcha_menu()
j = 0
index = 0
keys = []
for menu in menular:
    if j % 2 == 0 and j != 0:
        index+=1
    if j % 2 ==0:
        keys.append([KeyboardButton(text=f"{menu[1]}",)])
    else:
        keys[index].append(KeyboardButton(text=f"{menu[1]}",))
    j += 1




keys.append([KeyboardButton(text='ADMINGA MUROJAT')])
menu_butons = ReplyKeyboardMarkup(keyboard=keys,resize_keyboard=True)







tasq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="TASDIQLASH"),
            KeyboardButton(text="INKOR ETISH")
        ]
    ],
    resize_keyboard=True
)

tasq2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="CONFIRMATION"),
            KeyboardButton(text="REFUSAL")
        ]
    ],
    resize_keyboard=True
)