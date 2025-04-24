from aiogram import types, Dispatcher

ads = {}

async def add_ad_handler(message: types.Message):
    await message.answer("أرسل رابط موقعك للإعلان:")
    ads[message.from_user.id] = {"step": "awaiting_url"}

async def handle_ad_url(message: types.Message):
    if message.from_user.id in ads and ads[message.from_user.id]["step"] == "awaiting_url":
        ads[message.from_user.id]["url"] = message.text
        ads[message.from_user.id]["step"] = "completed"
        await message.answer("تم حفظ رابط موقعك! سيتم مراجعة الإعلان وتفعيله بعد الدفع.")

def register_ad(dp: Dispatcher):
    dp.register_message_handler(add_ad_handler, commands=["add_ad"])
    dp.register_message_handler(handle_ad_url)
