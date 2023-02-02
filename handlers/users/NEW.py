# import heapq
#
# from aiogram import types
#
# from loader import dp,bot
#
#
#
# @dp.message_handler(text="iPHONE")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#
#
#     rasm = 'https://t.me/lite_PML_PRIVATE/3'
#     await bot.send_photo(chat_id=user_id,photo=rasm,caption="IPHONE 14 PRO MAX  ")
#     rasm = 'https://t.me/lite_PML_PRIVATE/4'
#     await bot.send_photo(chat_id=user_id,photo=rasm,caption="IPHONE 13 PRO MAX  ")
#     rasm = 'https://t.me/lite_PML_PRIVATE/5'
#     await bot.send_photo(chat_id=user_id,photo=rasm,caption="IPHONE 12 PRO MAX  ")
#
#
# @dp.message_handler(text="XIAOMI")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#
#     rasm = 'https://t.me/lite_PML_PRIVATE/6'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption=" XIAOMI 12 PRO ULTRA 5G ")
#     rasm = 'https://t.me/lite_PML_PRIVATE/7'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="POCO M4 PRO 5G  ")
#     rasm = 'https://t.me/lite_PML_PRIVATE/8'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption=" XIAOMI NOTE 11 PRO ")
#
#
#
#
# @dp.message_handler(text="SAMSUNG")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/10'
#     await bot.send_photo(chat_id=user_id,photo=rasm,caption="SAMSUNG S22 ULTRA")
#     rasm = 'https://t.me/lite_PML_PRIVATE/11'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="SAMSUNG S21 ULTRA")
#     rasm = 'https://t.me/lite_PML_PRIVATE/12'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="SAMSUNG S10 5G")
#
#
#
# @dp.message_handler(text="REALMI")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/13'
#     await bot.send_photo(chat_id=user_id,photo=rasm,caption="REALMI I7 5G")
#     rasm = 'https://t.me/lite_PML_PRIVATE/14'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="REALMI I9 5G")
#     rasm = 'https://t.me/lite_PML_PRIVATE/15'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="REALMI I8 PRO 5G")
#
#
#
# @dp.message_handler(text="IPHONE")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#
#
#     rasm = 'https://t.me/lite_PML_PRIVATE/3'
#     await bot.send_photo(chat_id=user_id,photo=rasm,caption="IPHONE 14 PRO MAX  ")
#     rasm = 'https://t.me/lite_PML_PRIVATE/4'
#     await bot.send_photo(chat_id=user_id,photo=rasm,caption="IPHONE 13 PRO MAX  ")
#     rasm = 'https://t.me/lite_PML_PRIVATE/5'
#     await bot.send_photo(chat_id=user_id,photo=rasm,caption="IPHONE 12 PRO MAX  ")
#
#
# @dp.message_handler(text="XIAOMIS")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#
#     rasm = 'https://t.me/lite_PML_PRIVATE/6'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption=" XIAOMI 12 PRO ULTRA 5G ")
#     rasm = 'https://t.me/lite_PML_PRIVATE/7'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="POCO M4 PRO 5G  ")
#     rasm = 'https://t.me/lite_PML_PRIVATE/8'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption=" XIAOMI NOTE 11 PRO ")
#
#
#
#
# @dp.message_handler(text="SAMSUNGS")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/10'
#     await bot.send_photo(chat_id=user_id,photo=rasm,caption="SAMSUNG S22 ULTRA")
#     rasm = 'https://t.me/lite_PML_PRIVATE/11'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="SAMSUNG S21 ULTRA")
#     rasm = 'https://t.me/lite_PML_PRIVATE/12'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="SAMSUNG S10 5G")
#
#
#
# @dp.message_handler(text="REALME")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/13'
#     await bot.send_photo(chat_id=user_id,photo=rasm,caption="REALMI I7 5G")
#     rasm = 'https://t.me/lite_PML_PRIVATE/14'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="REALMI I9 5G")
#     rasm = 'https://t.me/lite_PML_PRIVATE/15'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="REALMI I8 PRO 5G")
#
#
#
#
#
#
# @dp.message_handler(text="HOCO BS37")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/16'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="HOCO BS37")
#
# @dp.message_handler(text="HOCO BS07")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/17'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="HOCO BS07")
#
#
#
#
# @dp.message_handler(text="SONY MHC-V90DW")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/18'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="SONY MHC-V90DW")
#
#
#
#
#
#
# @dp.message_handler(text="HI FI SHARF PS-929")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/19'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="HI FI SHARF PS-929")
#
# @dp.message_handler(text="HOCOS BS37")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/16'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="HOCO BS37")
#
# @dp.message_handler(text="HOCOS BS07")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/17'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="HOCO BS07")
#
# @dp.message_handler(text="SONY. MHC-V90DW")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/18'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="SONY MHC-V90DW")
#
# @dp.message_handler(text="HI FI SHARFF PS-929")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/19'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="HI FI SHARF PS-929")
#
#
# @dp.message_handler(text="ARTEL SMART TV")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/20'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="ARTEL SMART TV")
#
#
# @dp.message_handler(text="PRIMER SMART TV")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/21'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="PRIMER SMART TV")
#
#
# @dp.message_handler(text="SAMSUNG TV")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/22'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="SAMSUNG TV")
#
#
# @dp.message_handler(text="XIAOMI TV")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/23'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="XIAOMI TV")
#
#
#
#
# @dp.message_handler(text="ARTEL SMARTS TV")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/20'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="ARTEL SMART TV")
#
#
# @dp.message_handler(text="PRIMER SMARTS TV")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/21'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="PRIMER SMART TV")
#
#
# @dp.message_handler(text="SAMSUNGS TV")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/22'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="SAMSUNG TV")
#
#
# @dp.message_handler(text="XIAOMIS TV")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/23'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="XIAOMI TV")
#
#
#
# @dp.message_handler(text="APPLE WATCH SERIES 7")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/24'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="APPLE WATCH SERIES 7")
#
#
#
# @dp.message_handler(text="APPLE WATCH SE")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/25'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="APPLE WATCH SE")
#
#
# @dp.message_handler(text="APPLE WATCH SERIES 6")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/26'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="APPLE WATCH SERIES 6")
#
#
# @dp.message_handler(text="MIBRO AIR SMART")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/27'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="MIBRO AIR SMART")
#
#
#
# @dp.message_handler(text="APPLE WATCHS SERIES 7")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/24'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="APPLE WATCH SERIES 7")
#
#
#
# @dp.message_handler(text="APPLE WATCHS SE")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/25'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="APPLE WATCH SE")
#
#
# @dp.message_handler(text="APPLE WATCHS SERIES 6")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/26'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="APPLE WATCH SERIES 6")
#
#
# @dp.message_handler(text="MIBRO AIR SMARTS")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/27'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="MIBRO AIR SMART")
#
# @dp.message_handler(text="MACos COMPUTERS")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/28'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="MACBOOK PRO")
#
#
# @dp.message_handler(text="MACos KOMPYUTERLAR")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/28'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="MACBOOK PRO")
#
#
# @dp.message_handler(text="ASUS KOMPYUTERLAR")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/29'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="ASUS ROG ZEF")
#
#
# @dp.message_handler(text="LENOVO KOMPYUTERLAR")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/30'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="LENOVO")
#
#
#
# @dp.message_handler(text="MSI KOMPYUTERLAR")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/31'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="MSI TITAN GT77")
#
#
# @dp.message_handler(text="ACER KOMPYUTERLAR")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/32'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="ACER NITRO 5")
#
#
# @dp.message_handler(text="HP KOMPYUTERLAR")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/33'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="HP")
#
#
# @dp.message_handler(text="MACos KOMPYUTERLAR")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/28'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="MACBOOK PRO")
#
#
# @dp.message_handler(text="ASUS COMPUTERS")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/29'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="ASUS ROG ZEF")
#
#
# @dp.message_handler(text="LENOVO COMPUTERS")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/30'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="LENOVO")
#
#
#
# @dp.message_handler(text="MSI COMPUTERS")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/31'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="MSI TITAN GT77")
#
#
# @dp.message_handler(text="ACER COMPUTERS")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/32'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="ACER NITRO 5")
#
#
# @dp.message_handler(text="HP COMPUTERS")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/33'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="HP")
#
#
# @dp.message_handler(text="IGRAVOY QULOQCHINLAR")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/35'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="SVEN UP")
#
# @dp.message_handler(text="GAMING HEADSET")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/35'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="SVEN UP")
#
#
# @dp.message_handler(text="KINO KO'RISH UCHUN QULOQCHINLAR")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/36'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="SONY WH")
#
#
#
# @dp.message_handler(text="HEADPHONES FOR MOVIE WATCHING")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/36'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="SONY WH")
#
#
# @dp.message_handler(text="IGRAVOY USB SICHQONCHA")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/37'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="RGB")
#
#
# @dp.message_handler(text="GEMING MOUSE USB")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/37'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="RGB")
#
# @dp.message_handler(text="OFIS ISHLARI UCHUN SICHQONCHA")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/38'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="OFISNOY")
#
# @dp.message_handler(text="FOR THE OFFICE MOUSE")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/38'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="OFFICE")
#
# @dp.message_handler(text="IGRAVOY TOP KLYVATURIALAR")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/39'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="RGB IGRAVOY")
#
#
# @dp.message_handler(text="GEMING KLVIATURES")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/39'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="RGB GEMING")
#
# @dp.message_handler(text="OFIS ISHLARI UCHUN KLYVATURIA")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/40'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="MEXANIK")
#
# @dp.message_handler(text="OFFICE KLVIATURES")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/40'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="MEHANICK")
#
#
#
# @dp.message_handler(text="IPHONE 14 PRO MAX UCHUN")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/40'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="IPHONE")
#
#
# @dp.message_handler(text="SAMSUNG S22 ULTRA UCHUN")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/40'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="SAMSUNG")
#
#
#
# @dp.message_handler(text="XIAOMI 12 ULTRA UCHUN")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/40'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="XIAOMI")
#
#
# @dp.message_handler(text="REALMI Y25 UCHUN")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/40'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="REALMI")
#
# @dp.message_handler(text="REALMI Y25 UCHUN")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/40'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="REALMI")
#
# @dp.message_handler(text="REALMI Y25 UCHUN")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/40'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="REALMI")
#
# @dp.message_handler(text="REALMI Y25 UCHUN")
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     rasm = 'https://t.me/lite_PML_PRIVATE/40'
#     await bot.send_photo(chat_id=user_id, photo=rasm, caption="REALMI")
