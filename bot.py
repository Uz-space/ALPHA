import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ✅ TOKEN
TOKEN = "8609710969:AAFeYU681TDYC2youGJ6TEmlzfyZvERUG-s"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main_keyboard():
    keyboard = [
        [InlineKeyboardButton("🆕 Bot yaratish", callback_data="no")],
        [InlineKeyboardButton("💰 Balans", callback_data="no"), 
         InlineKeyboardButton("📋 Botlarim", callback_data="no")],
        [InlineKeyboardButton("⚙️ Sozlamalar", callback_data="no"), 
         InlineKeyboardButton("❓ Yordam", callback_data="no")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Xush kelibsiz!\n\n"
        "📌 Makefy Bot | MAKER bot\n"
        "🚀 20 Gbit/s tezkor Web Platforma\n\n"
        "🔹 Bu loyiha orqali Telegram botlaringizni web ilovamiz orqali yarating!\n\n"
        "Login: No\n"
        "Parol:",
        reply_markup=main_keyboard()
    )

# ✅ Hech nima qilmaydigan handler (faqat "hech nima" deb javob qaytaradi)
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer("⛔ Bu tugma ishlamaydi!", show_alert=False)

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 Makefy Bot ishga tushdi...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
