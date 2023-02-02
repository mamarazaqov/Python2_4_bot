from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
quloqchin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="IGRAVOY QULOQCHINLAR"),
            KeyboardButton(text="KINO KO'RISH UCHUN QULOQCHINLAR")
        ],
        [
            KeyboardButton(text="CHIQISH")
        ]
    ],
    resize_keyboard=True
)
quloqchin2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="GAMING HEADSET"),
            KeyboardButton(text="HEADPHONES FOR MOVIE WATCHING")
        ],
        [
            KeyboardButton(text="BACK")
        ]
    ],
    resize_keyboard=True
)