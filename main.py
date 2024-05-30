import time
from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.types import BotCommand
from aiogram.utils import executor
import genre
from lru_cache import LRUCache
from settings import Genre


bot = Bot(token='6197765863:AAGGCdx6usGqPmdl9TwenEcjM5vODhptyVk')
if not bot:
    exit("Error: no token provided")
dp = Dispatcher(bot)
lru_global = LRUCache()
slay = {Genre.fantasy: 0, Genre.horror: 0, Genre.crime: 0, Genre.comedy: 0, Genre.history: 0, Genre.action: 0, Genre.animation: 0, Genre.anime: 0, Genre.mystery: 0, Genre.adventure: 0}


async def get_film_list(call: types.CallbackQuery, genre_name: str, num_items: int = 5, offset: int = 0, lru: LRUCache = None):
    try:
        if lru is None:
            fl = genre.get_films(genre_name)
        else:
            fl = lru.get_data(genre_name, genre.get_films)
        for i, f in enumerate(fl[offset:offset+num_items]):
            ret_text = ""
            ret_text += f"{i + offset + 1}. [{f['name']}]({f['href']})\t"
            ret_text += f"({f['year']}, {f['country']})\n"
            await call.message.answer(ret_text, parse_mode='Markdown')
    except Exception as e:
        await call.message.answer("Произошла ошибка при получении списка фильмов.")


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    buttons = []
    genre_list = Genre.get_dir()
    for g in genre_list:
        buttons.append(types.InlineKeyboardButton(text=genre_list[g], callback_data=g))
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await message.answer('Приветствую тебя в кино-боте! \n '
                         'Команды, которыми ты можешь пользоваться: \n '
                         '/start - начни общение с ботом\n '
                         '/help - если нужна помощь, эта команда поможет решить любой вопрос')
    await message.answer(message.from_user.first_name + " выбери подходящий жанр фильма", reply_markup=keyboard)
    main_menu_commands = [
        BotCommand(command='/start',
                    description="начни общение с ботом"),
        BotCommand(command='/help',
                    description="эта команда поможет решить любой вопрос"),
    ]

    await bot.set_my_commands(main_menu_commands)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("1.Начни диалог с ботом, написав /start""\n"
                        "2.Выбери кнопку и найди нужный фильм ")


@dp.callback_query_handler(text=Genre.fantasy)
async def get_list_films(call: types.CallbackQuery):
    start = time.time()
    await get_film_list(call, Genre.fantasy, lru=lru_global, offset=slay[Genre.fantasy])
    slay[Genre.fantasy] += 5
    await call.answer()
    end = time.time()
    print(end - start)


@dp.callback_query_handler(text=Genre.horror)
async def get_list_films(call: types.CallbackQuery):
    start = time.time()
    await get_film_list(call, Genre.horror, lru=lru_global, offset=slay[Genre.horror])
    slay[Genre.horror] += 5
    await call.answer()
    end = time.time()
    print(end - start)


@dp.callback_query_handler(text=Genre.crime)
async def get_list_films(call: types.CallbackQuery):
    start = time.time()
    await get_film_list(call, Genre.crime, lru=lru_global, offset=slay[Genre.crime])
    slay[Genre.crime] += 5
    await call.answer()
    end = time.time()
    print(end - start)


@dp.callback_query_handler(text=Genre.comedy)
async def get_list_films(call: types.CallbackQuery):
    start = time.time()
    await get_film_list(call, Genre.comedy, lru=lru_global, offset=slay[Genre.comedy])
    slay[Genre.comedy] += 5
    await call.answer()
    end = time.time()
    print(end - start)


@dp.callback_query_handler(text=Genre.history)
async def get_list_films(call: types.CallbackQuery):
    start = time.time()
    await get_film_list(call, Genre.history, lru=lru_global, offset=slay[Genre.history])
    slay[Genre.history] += 5
    await call.answer()
    end = time.time()
    print(end - start)


@dp.callback_query_handler(text=Genre.action)
async def get_list_films(call: types.CallbackQuery):
    start = time.time()
    await get_film_list(call, Genre.action, lru=lru_global, offset=slay[Genre.action])
    slay[Genre.action] += 5
    await call.answer()
    end = time.time()
    print(end - start)


@dp.callback_query_handler(text=Genre.animation)
async def get_list_films(call: types.CallbackQuery):
    start = time.time()
    await get_film_list(call, Genre.animation, lru=lru_global, offset=slay[Genre.animation])
    slay[Genre.animation] += 5
    await call.answer()
    end = time.time()
    print(end - start)


@dp.callback_query_handler(text=Genre.anime)
async def get_list_films(call: types.CallbackQuery):
    start = time.time()
    await get_film_list(call, Genre.anime, lru=lru_global, offset=slay[Genre.anime])
    slay[Genre.anime] += 5
    await call.answer()
    end = time.time()
    print(end - start)


@dp.callback_query_handler(text=Genre.mystery)
async def get_list_films(call: types.CallbackQuery):
    start = time.time()
    await get_film_list(call, Genre.mystery, lru=lru_global, offset=slay[Genre.mystery])
    slay[Genre.mystery] += 5
    await call.answer()
    end = time.time()
    print(end - start)


@dp.callback_query_handler(text=Genre.adventure)
async def get_list_films(call: types.CallbackQuery):
    start = time.time()
    await get_film_list(call, Genre.adventure, lru=lru_global, offset=slay[Genre.adventure])
    slay[Genre.adventure] += 5
    await call.answer()
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
