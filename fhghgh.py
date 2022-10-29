
from aiogram import Bot, Dispatcher, executor, types
from logging import basicConfig, INFO

bot = Bot(token="5772534721:AAEBWi3R6EE6x7tWJibYLKHsM3bnF0cQZrE")
dp = Dispatcher(bot)
basicConfig(level=INFO)

@dp.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    await msg.answer(f'Я бот компании "Region78". {msg.from_user.first_name}')

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'Аутстаффинг':
       await msg.    answer('Аутстаффинг — способ организации работы с разными сотрудниками, при котором агентство-аутстаффер оформляет специалистов к себе в штат. Способности такого специалиста уже проверены, его не нужно искать и проверять. ')
@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'Аутсорсинг':
       await msg.    answer('Аутсорсинг: что это такое? Термин произошел от английского сокращения фразы «outer-source-using». В вольном переводе она означает использование ресурсов, привлеченных со стороны, извне. В российском деловом обиходе аутсорсинг – привлечение организацией сторонних компаний для выполнения каких-либо функций.')
@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'Цены за услуги':
       await msg.    answer('Привет!')
@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'Вакансии':
       await msg.    answer('Токарь-универсал'
                            'з/п:'
                            'Токарь'
                            'з/п:'
                            'Оператор наладчик станков с ПУ'
                            'з/п:'
                            'Слесарь МСР'
                            'з/п:'
                            'Токарь-карусельщик'
                            'з/п:'
                            'Оператор металлизации'
                            'з/п:'
                            'Токарь-фрезеровщик'
                            'з/п:')
   if _name_ =="region78":
    executor.start_polling(dp)