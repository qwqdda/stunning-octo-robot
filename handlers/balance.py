from aiogram import types, Dispatcher

user_balances = {}

async def balance_handler(message: types.Message):
    uid = message.from_user.id
    balance = user_balances.get(uid, 0)
    await message.answer(f"رصيدك الحالي: {balance} TON وهمي")

async def withdraw_handler(message: types.Message):
    await message.answer("للسحب، سيتم إرسال رصيدك إلى بريد FaucetPay الخاص بك لاحقاً (ميزة تحت التطوير).")

def register_balance(dp: Dispatcher):
    dp.register_message_handler(balance_handler, commands=["balance"])
    dp.register_message_handler(withdraw_handler, commands=["withdraw"])
