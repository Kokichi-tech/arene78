from aiogram import Bot, Dispatcher, executor, types
from logging import basicConfig, INFO

bot = Bot(token="5508138489:AAGVQua946Qzz2pYxzlucxinayeO2vn9Wbo")
dp = Dispatcher(bot)
basicConfig(level=INFO)

vaks = ('Токарь-универсал', 'Токарь', 'Оператор наладчик станков с ПУ', 'Слесарь МСР', 'Токарь-карусельщик',
        'Оператор металлизации', 'Токарь-фрезеровщик')
a = ''

for i in range(0, len(vaks)):
    a = a + vaks[i] + '\n' + 'з/п:' + '\n'


@dp.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    await msg.answer(f'Я бот компании "Region78". {msg.from_user.first_name}')


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text == 'Аутстаффинг':
        await bot.send_message(msg.from_user.id,
                               'Аутстаффинг — способ организации работы с разными сотрудниками, при котором агентство-аутстаффер '
                               'оформляет специалистов к себе в штат. Способности такого специалиста уже проверены, его не нужно искать '
                               'и проверять. ')
    if msg.text == 'Аутсорсинг':
        await bot.send_message(msg.from_user.id,
                               'Аутсорсинг: что это такое? Термин произошел от английского сокращения фразы «outer-source-using». В '
                               'вольном переводе она означает использование ресурсов, привлеченных со стороны, извне. В российском '
                               'деловом обиходе аутсорсинг – привлечение организацией сторонних компаний для выполнения каких-либо '
                               'функций.')
    if msg.text == 'Цены за услуги':
        await bot.send_message(msg.from_user.id, 'Привет!')
    if msg.text == 'Вакансии':
        await bot.send_message(msg.from_user.id, a)


if __name__ == '__main__':
    executor.start_polling(dp)
