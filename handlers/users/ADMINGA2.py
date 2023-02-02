# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from keyboards.default.MENU_UCHUN import tasq2
# from loader import dp, bot
# from states.MUROJQT import Forma, Forma1
#
#
# # Echo bot
# @dp.message_handler(text="CONTACT ADMIN")
# async def bot_echo(message: types.Message):
#     await message.answer(f"ENTER YOUR NAME")
#     await Forma1.ism_qabul1.set()
#
#
# @dp.message_handler(state=Forma1.ism_qabul1)
# async def bot_echo(message: types.Message,state:FSMContext):
#     ism = message.text
#     await state.update_data({"name1":ism})
#     await message.answer(f"ENTER LAST NAME")
#     await Forma1.fam1.set()
#
#
# @dp.message_handler(state=Forma1.fam1)
# async def bot_echo(message: types.Message,state:FSMContext):
#     fam1 = message.text
#     await state.update_data({"familya1":fam1})
#     await message.answer(f"ENTER YOUR AGE")
#     await Forma1.yosh_qabul1.set()
#
# @dp.message_handler(state=Forma1.yosh_qabul1)
# async def bot_echo(message: types.Message,state:FSMContext):
#     yosh = message.text
#     await state.update_data({"yoshm1":yosh})
#     await message.answer(f"ENTER YOUR NUMBER ")
#     await Forma1.tel_qabul1.set()
#
#
# @dp.message_handler(state=Forma1.tel_qabul1)
# async def bot_echo(message: types.Message,state:FSMContext):
#     tel = message.text
#     await state.update_data({"telm1":tel})
#     await message.answer(f"INCLUDE US WHAT YOU HAVE TO ADDRESS")
#     await Forma1.murojat_qabul1.set()
#
#
#
# @dp.message_handler(state=Forma1.murojat_qabul1)
# async def bot_echo(message: types.Message,state:FSMContext):
#     math = message.text
#     await state.update_data({"math1":math})
#
#     user_id = message.from_user.id
#
#
#     malumto =  await state.get_data()
#     ism = malumto.get('name1')
#     fam = malumto.get('familya1')
#     yosh = malumto.get('yoshm1')
#     nomer = malumto.get('telm1')
#     murojat = malumto.get('math1')
#     text = f"ISMI : {ism}\n" \
#            f"FAMILYASI : {fam}\n" \
#            f"YOSHI : {yosh}\n" \
#            f"NOMERI :{nomer}\n" \
#            f"MUROJATI : {murojat}\n"
#     await bot.send_message(chat_id=user_id,text=text,reply_markup=tasq2)
#     await Forma1.tasdiqlash1.set()
#
#
# @dp.message_handler(state=Forma1.tasdiqlash1,text='REFUSAL')
# async def bot_echo(message: types.Message,state:FSMContext):
#
#     await message.answer(f"REFUSAL",reply_markup=menu_butons2)
#     await state.finish()
#
# @dp.message_handler(state=Forma1.tasdiqlash1,text='CONFIRMATION')
# async def bot_echo(message: types.Message,state:FSMContext):
#     await message.answer(f"CONFIRMATION",reply_markup=menu_butons2)
#
#
#     malumto = await state.get_data()
#     user_id = message.from_user.id
#     ism = malumto.get('name1')
#     fam = malumto.get('familya1')
#     yosh = malumto.get('yoshm1')
#     nomer = malumto.get('telm1')
#     murojat = malumto.get('math1')
#
#     text = f"NAME : {ism}\n" \
#            f"SURNAME : {fam}\n" \
#            f"AGE : {yosh}\n" \
#            f"NUMBERS :{nomer}\n" \
#            f"APPLICATION : {murojat}\n"
#     await bot.send_message(chat_id='5183726145',text=text)
#     await bot.send_message(chat_id=user_id,text='CONFIRMATION',reply_markup=menu_butons2)
#     await state.finish()
#
