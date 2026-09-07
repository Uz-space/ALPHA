import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.types import InputRichMessage, InputRichBlockTable

# ✅ TOKEN
TOKEN = "8609710969:AAFeYU681TDYC2youGJ6TEmlzfyZvERUG-s"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ─── ALPHA ma'lumotlari ──────────────────────────────────────────────────────
ALPHA_DATA = {
    "title": "ALPHA",
    "domain": "sctg.xyz",
    "plan": "Trial",
    "accounts": 0,
    "total_claims": 0,
}

# ─── Tugmalar (faqat ko'rinish, ishlamaydi) ─────────────────────────────────
def main_keyboard():
    keyboard = [
        [InlineKeyboardButton("🆕 Bot yaratish", callback_data="no")],
        [InlineKeyboardButton("💰 Balans", callback_data="no"), 
         InlineKeyboardButton("📋 Botlarim", callback_data="no")],
        [InlineKeyboardButton("⚙️ Sozlamalar", callback_data="no"), 
         InlineKeyboardButton("❓ Yordam", callback_data="no")]
    ]
    return InlineKeyboardMarkup(keyboard)

# ─── ALPHA jadvali ────────────────────────────────────────────────────────────
def build_alpha_table():
    return InputRichBlockTable(
        cells=[
            [{"text": ALPHA_DATA["title"], "is_header": True, "align": "center"}],
            [{"text": f"🌐 {ALPHA_DATA['domain']}", "align": "center"}],
            [{"text": f"📋 {ALPHA_DATA['plan']}", "align": "center"}],
            [{"text": f"👥 Akkauntlar: {ALPHA_DATA['accounts']}", "align": "center"}],
            [{"text": f"📊 Jami olish: {ALPHA_DATA['total_claims']}", "align": "center"}],
        ],
        is_bordered=True,
        is_striped=True,
    )

# ─── /start ──────────────────────────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    alpha_table = build_alpha_table()
    
    rich_message = InputRichMessage(
        blocks=[
            alpha_table,
        ]
    )
    
    await update.message.reply_text(
        "🔹 Bu loyiha orqali Telegram botlaringizni web ilovamiz orqali yarating!\n\n"
        "Login: No\n"
        "Parol:",
        reply_markup=main_keyboard()
    )

# ─── Tugmalar bosilganda (hech narsa qilmaydi) ─────────────────────────────
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer("⛔ Bu tugma ishlamaydi!", show_alert=False)

# ─── Botni ishga tushirish ──────────────────────────────────────────────────
def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 Makefy Bot ishga tushdi...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
