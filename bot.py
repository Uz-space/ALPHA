import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import (
    InputRichMessage, 
    InputRichBlockTable, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton
)
from aiogram.enums import ButtonStyle

TOKEN = "8609710969:AAFeYU681TDYC2youGJ6TEmlzfyZvERUG-s"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

ALPHA_DATA = {
    "title": "ALPHA",
    "domain": "sctg.xyz",
    "plan": "Trial",
    "accounts": 0,
    "total_claims": 0,
}

def main_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🆕 Bot yaratish", callback_data="no")],
        [InlineKeyboardButton(text="💰 Balans", callback_data="no"), 
         InlineKeyboardButton(text="📋 Botlarim", callback_data="no")],
        [InlineKeyboardButton(text="⚙️ Sozlamalar", callback_data="no"), 
         InlineKeyboardButton(text="❓ Yordam", callback_data="no")]
    ])
    return keyboard

# ─── ALPHA jadvali ────────────────────────────────────────────────────────────
def build_alpha_table():
    return InputRichBlockTable(
        cells=[
            [
                {"text": ALPHA_DATA["title"], "is_header": True, "align": "center"}
            ],
            [
                {"text": f"🌐 {ALPHA_DATA['domain']}", "align": "center"}
            ],
            [
                {"text": f"📋 {ALPHA_DATA['plan']}", "align": "center"}
            ],
            [
                {"text": f"👥 Akkauntlar: {ALPHA_DATA['accounts']}", "align": "center"}
            ],
            [
                {"text": f"📊 Jami olish: {ALPHA_DATA['total_claims']}", "align": "center"}
            ],
        ],
        is_bordered=True,
        is_striped=True,
    )

@dp.message(CommandStart())
async def start(message: types.Message):
    rich_message = InputRichMessage(
        blocks=[build_alpha_table()]
    )
    
    # Rich Message jo'natish
    await message.answer_rich(
        rich_message=rich_message,
        reply_markup=main_keyboard()
    )

# ─── Tugmalar bosilganda ──────────────────────────────────────────────────────
@dp.callback_query(lambda c: c.data == "no")
async def no_button(callback: types.CallbackQuery):
    await callback.answer("⛔ Bu tugma ishlamaydi!", show_alert=False)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
