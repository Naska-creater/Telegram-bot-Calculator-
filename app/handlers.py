from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()


class Register(StatesGroup):
    name = State()
    age = State()
    number = State()

class Calculate(StatesGroup):
    text = State()

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer('Привет, я Бот-калькулятор!')#reply_markup=kb.main)
    await message.reply('Чтобы я начать нажми:',reply_markup=kb.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи')

@router.message(F.text == 'Включить калькулятор')
async def calculator(message: Message, state: FSMContext):
    await state.set_state(Calculate.text)
    await message.answer('Введите выражение для расчёта')

@router.message(Calculate.text)
async def calculator_text(message: Message, state: FSMContext):
    try:
        res = eval(message.text)
        await state.set_state (Calculate.text)
        await message.answer (f'Ответ: {res}')
    except NameError:
        await message.answer('Ошибка ввода, попробуйте ещё раз!')

# @router.callback_query(F.data == 't-shirt')
# async def t_shirt(callback: CallbackQuery):
#     await callback.answer('Вы выбрали футболку',show_alert=True)
#     await callback.message.answer('Вы выбрали футболку')

@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите своё имя')

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state (Register.age)
    await message.answer ('Введите Ваш возраст')

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Отправьте Ваш номер телефона', reply_markup=kb.get_number)

@router.message(Register.number, F.contact)
async def register_number(message:Message,state:FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Ваше имя: {data["name"]}\nВаш возраст: {data["age"]}\nНомер: {data["number"]}\n')
    await state.clear()
