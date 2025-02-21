import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from config import API_TOKEN

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создаем экземпляры Bot и Dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Функция для обработки команды /start
@dp.message(Command('start'))
async def start_command(message: types.Message):
    # Создаем клавиатуру с двумя кнопками
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='Привет')],
        [KeyboardButton(text='Пока')]
    ])

    # Отправляем сообщение с клавиатурой
    await message.answer("Выберите действие:", reply_markup=keyboard)

# Функция для обработки нажатий на кнопки
@dp.message()
async def button_handler(message: types.Message):
    if message.text == 'Привет':
        await message.answer(f"Привет, {message.from_user.first_name}!")
    elif message.text == 'Пока':
        await message.answer(f"До свидания, {message.from_user.first_name}!")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
