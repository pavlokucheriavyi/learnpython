import asyncio

from aiogram import Bot, Dispatcher, executor, types
from config import token, user_id
import json
from parser import check_news_update
from aiogram.dispatcher.filters import Text

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ['All cars', 'Last 5 cars', 'Fresh cars']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Лента машин", reply_markup=keyboard)


@dp.message_handler(Text(equals="All cars"))
async def get_all_news(message: types.Message):
    with open("news_dict.json") as file:
        news_dict = json.load(file)

    for k, v in news_dict.items():
        news = f"<b>{v['time']}</b>\n{v['title']}\n{v['link']}\n{v['price']}$"

        await message.answer(news)


@dp.message_handler(Text(equals="Last 5 cars"))
async def get_five_news(message: types.Message):
    with open("news_dict.json") as file:
        news_dict = json.load(file)

    last_five_dict = {}

    midlle_list = list(news_dict.items())[-5:]

    for k, v in midlle_list:
        last_five_dict[k] = v

    for k, v in last_five_dict.items():
        news = f"<b>{v['time']}</b>\n{v['title']}\n{v['link']}\n{v['price']}$"

        await message.answer(news)


@dp.message_handler(Text(equals="Fresh cars"))
async def get_fresh_news(message: types.Message):
    fresh_news = check_news_update()

    if len(fresh_news) >= 1:
        for k, v in fresh_news.items():
            news = f"<b>{v['time']}</b>\n{v['title']}\n{v['link']}\n{v['price']}$"

            await message.answer(news)

    else:
        await message.answer("Пока нет новых машин")


async def news_every_minute():
    while True:
        fresh_news = check_news_update()

        if len(fresh_news) >= 1:
            for k, v in fresh_news.items():
                news = f"<b>{v['time']}</b>\n{v['title']}\n{v['link']}\n{v['price']}$"

                await bot.send_message(user_id, news)

        await asyncio.sleep(15)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())
    executor.start_polling(dp)
