from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

OYOQ_KIYIM_BUTTONS = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="iPHONE"),
            KeyboardButton(text="XIAOMI")
        ],
        [
            KeyboardButton(text="SAMSUNG"),
            KeyboardButton(text="REALMI")
        ],
        [
            KeyboardButton(text="CHIQISH")
        ]
    ],
    resize_keyboard=True
)


OYOQ_KIYIM_BUTTONS2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="IPHONE"),
            KeyboardButton(text="SAMSUNGS")
        ],
        [
            KeyboardButton(text="REALME"),
            KeyboardButton(text="XIAOMIS")
        ],
        [
            KeyboardButton(text="BACK")
        ]
    ],
    resize_keyboard=True
)
