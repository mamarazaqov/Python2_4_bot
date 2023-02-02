from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
SPORT = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="APPLE WATCH SERIES 7"),
            KeyboardButton(text="APPLE WATCH SE")
        ],
        [
            KeyboardButton(text="APPLE WATCH SERIES 6"),
            KeyboardButton(text="MIBRO AIR SMART")
        ],
        [
            KeyboardButton(text="CHIQISH")
        ]
    ],
    resize_keyboard=True
)

SPORT2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="APPLE WATCHS SERIES 7"),
            KeyboardButton(text="APPLE WATCHS SE")
        ],
        [
            KeyboardButton(text="APPLE WATCHS SERIES 6"),
            KeyboardButton(text="MIBRO AIR SMARTS")
        ],
        [
            KeyboardButton(text="BACK")
        ]
    ],
    resize_keyboard=True
)