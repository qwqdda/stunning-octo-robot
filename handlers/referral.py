from aiogram import types, Dispatcher

async def referral_handler(message: types.Message):
    uid = message.from_user.id
    await message.answer(f"رابط إحالتك:\nhttps://t.me/YOUR_BOT_USERNAME?start={uid}")

def register_referral(dp: Dispatcher):
    dp.register_message_handler(referral_handler, commands=["referral"])
