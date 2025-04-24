from aiogram import types, Dispatcher

async def start_handler(message: types.Message):
    await message.answer("مرحباً بك في بوت إعلانات المواقع!\nاستخدم الأوامر التالية:\n/add_ad - إضافة إعلان\n/balance - رصيدك\n/withdraw - سحب\n/referral - رابط الإحالة")

def register_start(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
