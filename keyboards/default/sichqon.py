from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
sichqon = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="IGRAVOY USB SICHQONCHA"),
            KeyboardButton(text="OFIS ISHLARI UCHUN SICHQONCHA")
        ],
        [
            KeyboardButton(text="IGRAVOY TOP KLYVATURIALAR"),
            KeyboardButton(text="OFIS ISHLARI UCHUN KLYVATURIA")
        ],
        [
            KeyboardButton(text="CHIQISH")
        ]
    ],
    resize_keyboard=True
)

sichqon2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="GEMING MOUSE USB"),
            KeyboardButton(text="FOR THE OFFICE MOUSE")
        ],
        [
            KeyboardButton(text="GEMING KLVIATURES"),
            KeyboardButton(text="OFFICE KLVIATURES")
        ],
        [
            KeyboardButton(text="BACK")
        ]
    ],
    resize_keyboard=True
)