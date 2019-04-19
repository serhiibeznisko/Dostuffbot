from telegram import KeyboardButton, ReplyKeyboardMarkup


def commands_keyboard(commands):
    keyboard = [
        [KeyboardButton(c.text)]
        for c in commands
    ]
    keyboard.append([KeyboardButton('Menu')])
    keyboard.append([KeyboardButton('Add command')])
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


START_KB = [[
    KeyboardButton('Commands'),
    KeyboardButton('Send notification'),
    KeyboardButton('Scheduled notification'),
]]


START_M = ReplyKeyboardMarkup(START_KB, resize_keyboard=True)