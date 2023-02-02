from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.MENU_UCHUN import tasq, menu_butons
from loader import dp, bot
from states.MUROJQT import Forma

# Echo bot
@dp.message_handler(text="ADMINGA MUROJAT")
async def bot_echo(message: types.Message):
    await message.answer(f"ISMNI KIRITING")
    await Forma.ism_qabul.set()


@dp.message_handler(state=Forma.ism_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    ism = message.text
    await state.update_data({"name":ism})
    await message.answer(f"FAMILYANI KIRITING")
    await Forma.fam.set()


@dp.message_handler(state=Forma.fam)
async def bot_echo(message: types.Message,state:FSMContext):
    fam1 = message.text
    await state.update_data({"familya":fam1})
    await message.answer(f"YOSHINGIZNI KIRITING")
    await Forma.yosh_qabul.set()

@dp.message_handler(state=Forma.yosh_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    yosh = message.text
    await state.update_data({"yoshm":yosh})
    await message.answer(f"NOMERINGIZNI KIRITING KIRITING")
    await Forma.tel_qabul.set()


@dp.message_handler(state=Forma.tel_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    tel = message.text
    await state.update_data({"telm":tel})
    await message.answer(f"BIZGA QANDAY MUROJATINGIZ BOR KIRITING")
    await Forma.murojat_qabul.set()



@dp.message_handler(state=Forma.murojat_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    math = message.text
    await state.update_data({"math":math})

    user_id = message.from_user.id


    malumto =  await state.get_data()
    ism = malumto.get('name')
    fam = malumto.get('familya')
    yosh = malumto.get('yoshm')
    nomer = malumto.get('telm')
    murojat = malumto.get('math')
    text = f"ISMI : {ism}\n" \
           f"FAMILYASI : {fam}\n" \
           f"YOSHI : {yosh}\n" \
           f"NOMERI :{nomer}\n" \
           f"MUROJATI : {murojat}\n"
    await bot.send_message(chat_id=user_id,text=text,reply_markup=tasq)
    await Forma.tasdiqlash.set()


@dp.message_handler(state=Forma.tasdiqlash,text='INKOR ETISH')
async def bot_echo(message: types.Message,state:FSMContext):

    await message.answer(f"BEKOR QILNDI",reply_markup=menu_butons)
    await state.finish()

@dp.message_handler(state=Forma.tasdiqlash,text='TASDIQLASH')
async def bot_echo(message: types.Message,state:FSMContext):
    await message.answer(f"ADMINGA YUBORILDI",reply_markup=menu_butons)


    malumto = await state.get_data()
    user_id = message.from_user.id
    ism = malumto.get('name')
    fam = malumto.get('familya')
    yosh = malumto.get('yoshm')
    nomer = malumto.get('telm')
    murojat = malumto.get('math')

    text = f"ISMI : {ism}\n" \
           f"FAMILYASI : {fam}\n" \
           f"YOSHI : {yosh}\n" \
           f"NOMERI :{nomer}\n" \
           f"MUROJATI : {murojat}\n"
    await bot.send_message(chat_id='5183726145',text=text)
    await bot.send_message(chat_id=user_id,text='ADMINGA YUBORILDI',reply_markup=menu_butons)
    await state.finish()

