import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ✅ TOKEN
TOKEN = "8609710969:AAFeYU681TDYC2youGJ6TEmlzfyZvERUG-s"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main_keyboard():
    keyboard = [
        [KeyboardButton("🆕 Bot yaratish"), KeyboardButton("📋 Botlarim")],
        [KeyboardButton("💰 Balans"), KeyboardButton("👥 Referal")],
        [KeyboardButton("🌐 Web ilova"), KeyboardButton("❓ Yordam")],
        [KeyboardButton("⚙️ Sozlamalar"), KeyboardButton("🛠 Maker Bo'lim")],
        [KeyboardButton("✉️ Xabar")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Xush kelibsiz!\n\n"
        "📌 Makefy Bot | MAKER bot\n"
        "🚀 20 Gbit/s tezkor Web Platforma\n\n"
        "🔹 Bu loyiha orqali Telegram botlaringizni web ilovamiz orqali yarating!\n"
        "🔹 Quyidagi tugmalardan foydalaning:\n\n"
        "Login: No\n"
        "Parol:",
        reply_markup=main_keyboard()
    )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "🆕 Bot yaratish":
        await update.message.reply_text(
            "🤖 Yangi bot yaratish\n\n"
            "Bot nomi va tokenini kiriting:",
            reply_markup=main_keyboard()
        )
    
    elif text == "📋 Botlarim":
        await update.message.reply_text(
            "📋 Sizning botlaringiz:\n\n"
            "Hali bot yaratilmagan.",
            reply_markup=main_keyboard()
        )
    
    elif text == "💰 Balans":
        await update.message.reply_text(
            "💰 Balans: 0 so'm\n"
            "💳 To'lov qilish: [link]",
            reply_markup=main_keyboard()
        )
    
    elif text == "👥 Referal":
        await update.message.reply_text(
            "👥 Referal dasturi\n\n"
            "🔗 Havolangiz: https://t.me/makefy_bot?start=ref_123\n"
            "👤 Do'stingiz kelganda: +100 so'm",
            reply_markup=main_keyboard()
        )
    
    elif text == "🌐 Web ilova":
        await update.message.reply_text(
            "🌐 Web ilova\n\n"
            "Botni to'liq boshqarish uchun:\n"
            "🔗 https://makefy.com/dashboard",
            reply_markup=main_keyboard()
        )
    
    elif text == "❓ Yordam":
        await update.message.reply_text(
            "❓ Yordam\n\n"
            "📞 Admin: @makefy_admin\n"
            "📧 Email: support@makefy.com",
            reply_markup=main_keyboard()
        )
    
    elif text == "⚙️ Sozlamalar":
        await update.message.reply_text(
            "⚙️ Sozlamalar\n\n"
            "🔹 Til: O'zbekcha\n"
            "🔹 Xabarlar: Yoqilgan",
            reply_markup=main_keyboard()
        )
    
    elif text == "🛠 Maker Bo'lim":
        await update.message.reply_text(
            "🛠 Maker Bo'lim\n\n"
            "🔹 Faqat adminlar uchun!\n"
            "🔹 Bot sozlamalari va statistikalar.",
            reply_markup=main_keyboard()
        )
    
    elif text == "✉️ Xabar":
        await update.message.reply_text(
            "✉️ Xabar yozish\n\n"
            "Adminlarga xabar yuboring:",
            reply_markup=main_keyboard()
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))
    
    print("🤖 Makefy Bot ishga tushdi...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
