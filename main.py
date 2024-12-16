import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

TOKEN = os.getenv('TOKEN')
bot = Bot(token='')
dp = Dispatcher()
logging.basicConfig(
    level=logging.INFO,
    filename='loggs.log',
    format = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s"
    )

@dp.message(Command(commands=['start']))
async def start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Hello, {user_name}! Nice to see you here! Enter the name you want to transliterate"
    logging.info(f'{user_name}, {user_id} -- запустил бота')
    await bot.send_message(chat_id=user_id, text=text)

#Транслитерация
def translate(text: str) -> str:
    Ru_to_Eng = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': 'ie', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'iu', 'я': 'ia'
    }

    out = ''
    out = ''.join(Ru_to_Eng.get(char, char) for char in text.lower())
    return' '.join(i.capitalize() for i in out.split())


@dp.message()
async def send_mess(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name} {user_id}: написал сообщение {text}')
    await message.answer(text=translate(text))

if __name__ == '__main__':
    dp.run_polling(bot)

