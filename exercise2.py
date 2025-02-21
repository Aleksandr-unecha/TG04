import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from config import API_TOKEN

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создаем экземпляры Bot и Dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработка команды /links
@dp.message(Command('links'))
async def show_links(message: types.Message):
    # Создаем инлайн-клавиатуру с тремя кнопками
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Новости', url='https://ria.ru/'),
            InlineKeyboardButton(text='Музыка', url='https://vk.com/vkmusic'),
            InlineKeyboardButton(text='Видео', url='https://vkvideo.ru/'),
        ]
    ])

    await message.reply("Выберите ссылку:", reply_markup=inline_kb)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())