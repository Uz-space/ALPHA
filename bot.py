import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ✅ TOKENNI TO'G'RIDAN-TO'G'RI YOZING
TOKEN = "8609710969:AAFeYU681TDYC2youGJ6TEmlzfyZvERUG-s"  # O'z tokenizni yozing

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ✅ Asosiy tugmalar (doimiy)
def main_keyboard():
    keyboard = [
        [KeyboardButton("🆕 Bot yaratish")],
        [KeyboardButton("📋 Botlarim"), KeyboardButton("💰 Balans")],
        [KeyboardButton("👥 Referal"), KeyboardButton("🌐 Web ilova")],
        [KeyboardButton("❓ Yordam"), KeyboardButton("⚙️ Sozlamalar")],
        [KeyboardButton("🛠 Maker Bo'lim")],
        [KeyboardButton("✉️ Xabar")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ✅ /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Xush kelibsiz!\n\n"
        "📌 Makefy Bot | MAKER bot\n"
        "🚀 20 Gbit/s tezkor Web Platforma\n\n"
        "🔹 Bu loyiha orqali Telegram botlaringizni web ilovamiz orqali yarating!\n"
        "🔹 Quyidagi tugmalardan foydalaning:",
        reply_markup=main_keyboard()
    )

# ✅ Tugmalar uchun handler
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "🆕 Bot yaratish":
        await update.message.reply_text("🤖 Yangi bot yaratish bo'limi.", reply_markup=main_keyboard())
    
    elif text == "📋 Botlarim":
        await update.message.reply_text("📋 Sizning botlaringiz ro'yxati.", reply_markup=main_keyboard())
    
    elif text == "💰 Balans":
        await update.message.reply_text("💰 Sizning balansingiz: 0 so'm", reply_markup=main_keyboard())
    
    elif text == "👥 Referal":
        await update.message.reply_text("👥 Referal havolangiz: https://t.me/...", reply_markup=main_keyboard())
    
    elif text == "🌐 Web ilova":
        await update.message.reply_text("🌐 Web ilovaga o'tish: [link]", reply_markup=main_keyboard())
    
    elif text == "❓ Yordam":
        await update.message.reply_text("❓ Yordam: admin bilan bog'lang.", reply_markup=main_keyboard())
    
    elif text == "⚙️ Sozlamalar":
        await update.message.reply_text("⚙️ Sozlamalar bo'limi.", reply_markup=main_keyboard())
    
    elif text == "🛠 Maker Bo'lim":
        await update.message.reply_text("🛠 Maker bo'limi (faqat adminlar uchun).", reply_markup=main_keyboard())
    
    elif text == "✉️ Xabar":
        await update.message.reply_text("✉️ Xabar yozish bo'limi.", reply_markup=main_keyboard())

# ✅ Botni ishga tushirish
def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))
    
    print("🤖 Bot ishga tushdi...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
