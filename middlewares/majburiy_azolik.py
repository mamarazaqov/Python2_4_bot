from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from loader import bot
from utils.AZO_TEK import tekshirish
from data.config import kanallar
class Asosiy_chekking(BaseMiddleware):
    async def on_pre_process_update(self,xabar:types.Update,data:dict):
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return
        matn = "QUYDAGI KANALGA AZO BO'LING\n"
        royxat = []
        dastlabki_holat = True
        for k in kanallar:
            holat = await tekshirish(user_id=user_id,kanal_link=k)
            dastlabki_holat *= holat
            kanal = await bot.get_chat(k)
            if not holat:
                link = await kanal.export_invite_link()
                button = [InlineKeyboardButton(text=f"OBUNA BO'LING",url=f"{link}")]
                royxat.append(button)
        royxat.append([InlineKeyboardButton(text="TASDIQLASH",callback_data='www')])
        if not dastlabki_holat:
            await bot.send_message(chat_id=user_id,text=matn,disable_web_page_preview=True,
                                   reply_markup=InlineKeyboardMarkup(inline_keyboard=royxat))
            raise CancelHandler()
