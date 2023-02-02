from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, KeyboardButton, ReplyKeyboardMarkup


from loader import dp, obeykt, bot

from keyboards.default.MENU_UCHUN import menu_butons
#
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    fam = message.from_user.last_name
    username = message.from_user.username
    user_id = message.from_user.id
    try:
        obeykt.user_qoshish(ism=ism,tg_id=user_id,fam=fam,username=username)
    except Exception:
        pass


    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=enuz)


# from keyboards.default.OYOQ_KIYIMLAR import OYOQ_KIYIM_BUTTONS,OYOQ_KIYIM_BUTTONS2
#
#
# @dp.message_handler(text="📱TELEFONLAR📱")
# async def bot_start(message: types.Message):
#     await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=OYOQ_KIYIM_BUTTONS)
#
# @dp.message_handler(text="CHIQISH")
# async def bot_start(message: types.Message):
#     await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=menu_butons)
#
#
#
# from keyboards.default.BOSH_KIYIMLAR import bosh_kiyim,bosh_kiyim2
#
# @dp.message_handler(text="📻KALONKALAR📻")
# async def bot_start(message: types.Message):
#     await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=bosh_kiyim)
#

@dp.message_handler(text="CHIQISH")
async def bot_start(message: types.Message):
    await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=menu_butons)

#
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!")
#
#
# from keyboards.default.QISHKI_KIYIMLA import QISHKI_KIYIM,QISHKI_KIYIM2
#
# @dp.message_handler(text="🖥TELEVIZORLAR🖥")
# async def bot_start(message: types.Message):
#     await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=QISHKI_KIYIM)
#
#
#
# from keyboards.default.SUMKALAR import SUMKALA,SUMKALA2
#
#
# @dp.message_handler(text="💻KOMPYUTERLAR💻")
# async def bot_start(message: types.Message):
#     await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=SUMKALA)
#

from keyboards.default.SPORT import SPORT,SPORT2

# @dp.message_handler(text="⌚QOL SOATLAR⌚")
# async def bot_start(message: types.Message):
#     await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=SPORT)
#


#
# @dp.message_handler(text="🎧GAJETLAR🎧")
# async def bot_start(message: types.Message):
#     await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=BOLALAR)

from keyboards.inline.enuz import enuz
@dp.callback_query_handler(text="til1")
async def bot_start(message: CallbackQuery):
    await message.message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=menu_butons)

# @dp.callback_query_handler(text="til2")
# async def bot_start(message: CallbackQuery):
#     await message.message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=menu_butons2)
@dp.callback_query_handler(text="www")
async def bot_start(message: CallbackQuery):
    await message.message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=enuz)

# @dp.message_handler(text="🎧GONJETS🎧")
# async def bot_start(message: types.Message):
#     await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=BOLALAR2)
#
#

# @dp.message_handler(text="BACK")
# async def bot_start(message: types.Message):
#     await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=menu_butons2)
#
#
#


#
# @dp.message_handler(text="📱TELEPHONES📱")
# async def bot_start(message: types.Message):
#     await message.answer(f"CHOOSE ONE OF THE SECTIONS {message.from_user.full_name}!",reply_markup=OYOQ_KIYIM_BUTTONS2)
#
#
# @dp.message_handler(text="📻TO LISTEN TO MUSIC📻")
# async def bot_start(message: types.Message):
#     await message.answer(f"CHOOSE ONE OF THE SECTIONS {message.from_user.full_name}!",reply_markup=bosh_kiyim2)
#
#
#
# @dp.message_handler(text="🖥TV SETS🖥")
# async def bot_start(message: types.Message):
#     await message.answer(f"CHOOSE ONE OF THE SECTIONS {message.from_user.full_name}!",reply_markup=QISHKI_KIYIM2)
#
#
# @dp.message_handler(text="📱TELEFONLAR📱")
# async def bot_start(message: types.Message):
#     await message.answer(f"CHOOSE ONE OF THE SECTIONS {message.from_user.full_name}!",reply_markup=QISHKI_KIYIM)
#
# @dp.message_handler(text="⌚WRIST WATCH⌚")
# async def bot_start(message: types.Message):
#     await message.answer(f"CHOOSE ONE OF THE SECTIONS {message.from_user.full_name}!",reply_markup=SPORT2)
#
#
#
# @dp.message_handler(text="💻COMPUTERS💻")
# async def bot_start(message: types.Message):
#     await message.answer(f"CHOOSE ONE OF THE SECTIONS {message.from_user.full_name}!",reply_markup=SUMKALA2)
#
# from keyboards.default.quloqchin import quloqchin,quloqchin2
# @dp.message_handler(text="QULOQCHINLAR BO'LIMI")
# async def bot_start(message: types.Message):
#     await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=quloqchin)
#
#
# @dp.message_handler(text="HEADPHONE SECTION")
# async def bot_start(message: types.Message):
#     await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=quloqchin2)
#
#
# @dp.message_handler(text="KLYVATURIA VA SICHQONCHA BO'LIMI")
# async def bot_start(message: types.Message):
#     await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=sichqon)
#
#
#
# @dp.message_handler(text="KLAVIATURA AND MOUSE DEPARTMENT")
# async def bot_start(message: types.Message):
#     await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=sichqon2)
#
#
#
#
# @dp.message_handler(text="CHOYSTIKLAR BO'LIMI")
# async def bot_start(message: types.Message):
#     await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!", reply_markup=joystik)
#
# @dp.message_handler(text="CHOYSTIKS DEPARTMENT")
# async def bot_start(message: types.Message):
#     await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!", reply_markup=joystik2)

@dp.message_handler(commands="reklama",chat_id='5183726145')
async def bot_start(message: types.Message):
    try:
        userlar = obeykt.selecet_XAMMA_user()
        print(userlar)
        for user in userlar:
            print(user)
            await bot.send_message(chat_id=user[4],text='salom')

    except Exception:
        pass



menular = obeykt.selecet_barcha_menu()

@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(messeage: types.Message):
    text = messeage.text
    maxsulotlar = obeykt.select_maxsulotlar(tur=text)
    j = 0
    index = 0
    keys = []
    for menu in maxsulotlar:
        if j % 2 == 0 and j != 0:
            index += 1
        if j % 2 == 0:
            keys.append([KeyboardButton(text=f"{menu[1]}", )])
        else:
            keys[index].append(KeyboardButton(text=f"{menu[1]}", ))
        j += 1

    keys.append([KeyboardButton(text='CHIQISH')])
    maxsulot_butons = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    user_id = messeage.from_user.id
    await bot.send_message(chat_id=user_id,text='MAXSULTNI TANLANG',reply_markup=maxsulot_butons)





menular = obeykt.selecet_barcha_maxsulotlar()

@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(messeage: types.Message):
    text = messeage.text
    maxsulot = obeykt.select_maxsulot(nomi=text)
    max_nomi =maxsulot[1]
    max_rasm = maxsulot[4]
    max_text = maxsulot[3]
    max_narx = maxsulot[2]
    user_id = messeage.from_user.id
    malumot = f"NOMI: {max_nomi}\n" \
              f"NARXI: {max_narx}\n" \
              f"MALUMOTI: {max_text}\n"
    await  bot.send_photo(chat_id=user_id,photo=max_rasm,caption=malumot)