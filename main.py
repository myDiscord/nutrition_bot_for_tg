import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards.client_kb import gender_button, activity_button, goal_button, on_startup_button
from other import BotState, calculator, activity_message, info

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token='52686392:AAHEZ8vvsdmAt2Pu2---dpo')
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def on_startup(message: types.Message):
     await message.answer('Greetings 🙂\nSelect an action', reply_markup=on_startup_button)


@dp.callback_query_handler(text='info')
async def calculate(callback: types.CallbackQuery):
     await callback.message.answer(info, reply_markup=on_startup_button)
     await callback.answer()


@dp.callback_query_handler(text='calculate', state=None)
async def calculate(callback: types.CallbackQuery):
     await BotState.gender.set()
     await callback.message.answer('Enter your gender', reply_markup=gender_button)
     await callback.answer()


@dp.message_handler(state=BotState.gender)
async def goal_input(message: types.Message, state: FSMContext):
     await state.update_data(gender=message.text)
     await BotState.next()
     await bot.send_message(message.from_user.id, 'Select your goal', reply_markup=goal_button)


@dp.message_handler(state=BotState.goal)
async def gender_input(message: types.Message, state: FSMContext):
     await state.update_data(goal=message.text)
     await BotState.next()
     await bot.send_message(message.from_user.id, 'Enter your weight (kg)')


@dp.message_handler(state=BotState.weight)
async def weight_input(message: types.Message, state: FSMContext):
     await state.update_data(weight=message.text)
     await BotState.next()
     await bot.send_message(message.from_user.id, 'Enter your height (cm)')


@dp.message_handler(state=BotState.height)
async def height_input(message: types.Message, state: FSMContext):
     await state.update_data(height=message.text)
     await BotState.next()
     await bot.send_message(message.from_user.id, 'Enter your age')


@dp.message_handler(state=BotState.age)
async def age_input(message: types.Message, state: FSMContext):
     await state.update_data(age=message.text)
     await BotState.next()
     await bot.send_message(message.from_user.id, activity_message, reply_markup=activity_button)


@dp.message_handler(state=BotState.activity)
async def activity_input(message: types.Message, state: FSMContext):
     await state.update_data(activity=message.text)
     user_data = await state.get_data()
     await bot.send_message(message.from_user.id, calculator(user_data))
     await state.finish()
     await bot.send_message(message.from_user.id, 'Redo calculation?', reply_markup=on_startup_button)


executor.start_polling(dp, skip_updates=True)
