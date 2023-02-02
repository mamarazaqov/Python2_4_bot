from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
enuz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'ZBEK TILI",callback_data="til1"),
            InlineKeyboardButton(text="INGILIZ TILI",callback_data="til2")
        ]
    ],

)