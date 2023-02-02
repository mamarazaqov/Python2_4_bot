from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
QISHKI_KIYIM = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ARTEL SMART TV"),
            KeyboardButton(text="PRIMER SMART TV")
        ],
        [
            KeyboardButton(text="SAMSUNG TV"),
            KeyboardButton(text="XIAOMI TV")
        ],
        [
            KeyboardButton(text="CHIQISH")
        ]
    ],
    resize_keyboard=True
)

QISHKI_KIYIM2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ARTEL SMARTS TV"),
            KeyboardButton(text="PRIMER SMARTS TV")
        ],
        [
            KeyboardButton(text="SAMSUNGS TV"),
            KeyboardButton(text="XIAOMIS TV")
        ],
        [
            KeyboardButton(text="BACK")
        ]
    ],
    resize_keyboard=True
)