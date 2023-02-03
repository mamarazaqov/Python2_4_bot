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

@dp.message_handler(text="CHIQISH")
async def bot_start(message: types.Message):
    await message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=menu_butons)

#

from keyboards.inline.enuz import enuz
@dp.callback_query_handler(text="til1")
async def bot_start(message: CallbackQuery):
    await message.message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=menu_butons)

# @dp.callback_query_handler(text="til2")
# async def bot_start(message: CallbackQuery):
#     await message.message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=menu_butons2)
# @dp.callback_query_handler(text="www")
async def bot_start(message: CallbackQuery):
    await message.message.answer(f"BO'LIMLARDAN BIRINI TANLANG {message.from_user.full_name}!",reply_markup=enuz)



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






menular1 = obeykt.selecet_barcha_menu1()

@dp.message_handler(text=[menu1[1] for menu1 in menular1])
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