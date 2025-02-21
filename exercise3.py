import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import API_TOKEN

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создаем экземпляры Bot и Dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработка команды /dynamic
@dp.message(Command("dynamic"))
async def dynamic_buttons(message: Message):
    # Создаем инлайн-клавиатуру с одной кнопкой
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Показать больше", callback_data="show_more")
    inline_kb = keyboard_builder.as_markup()

    await message.reply("Нажмите кнопку:", reply_markup=inline_kb)

# Обработка нажатия кнопки "Показать больше"
@dp.callback_query(lambda c: c.data == "show_more")  # Фильтр по значению callback_data
async def show_more_options(callback: CallbackQuery):
    # Удаляем старую кнопку и добавляем две новых
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Опция 1", callback_data="option1")
    keyboard_builder.button(text="Опция 2", callback_data="option2")
    new_inline_kb = keyboard_builder.as_markup()

    await callback.message.edit_reply_markup(reply_markup=new_inline_kb)

# Обработка выбора опций
@dp.callback_query(lambda c: c.data in ["option1", "option2"])  # Фильтр по списку значений callback_data
async def selected_option(callback: CallbackQuery):
    if callback.data == "option1":
        text = "Вы выбрали Опцию 1"
    elif callback.data == "option2":
        text = "Вы выбрали Опцию 2"

    await callback.message.answer(text)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())