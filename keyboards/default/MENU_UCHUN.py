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



#
#
#
#
# menular1 = obeykt.selecet_barcha_menu1()
# j1 = 0
# index1 = 0
# keys1 = []
# for menu1 in menular1:
#     if j1 % 2 == 0 and j1 != 0:
#         index1+=1
#     if j1 % 2 ==0:
#         keys.append([KeyboardButton(text=f"{menu1[1]}",)])
#     else:
#         keys1[index1].append(KeyboardButton(text=f"{menu1[1]}",))
#     j1 += 1
#
#
#
# keys1.append([KeyboardButton(text='CANTACT ADMIN')])
# menu_butons2 = ReplyKeyboardMarkup(keyboard=keys,resize_keyboard=True)
#


#
tasq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="TASDIQLASH"),
            KeyboardButton(text="INKOR ETISH")
        ]
    ],
    resize_keyboard=True
)
#
# tasq2 = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="CONFIRMATION"),
#             KeyboardButton(text="REFUSAL")
#         ]
#     ],
#     resize_keyboard=True
# )