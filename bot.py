import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ✅ TOKENNI TO'G'RI YOZING
TOKEN = "7268818327:AAFeYU681TDYC2youGJ6TEmlzfyZvERUG-s"  # Shu tokenni ishlating!

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main_keyboard():
    keyboard = [
        [InlineKeyboardButton("🆕 Bot yaratish", callback_data="create_bot")],
        [InlineKeyboardButton("📋 Botlarim", callback_data="my_bots"), 
         InlineKeyboardButton("💰 Balans", callback_data="balance")],
        [InlineKeyboardButton("👥 Referal", callback_data="referal"), 
         InlineKeyboardButton("🌐 Web ilova", callback_data="web_app")],
        [InlineKeyboardButton("❓ Yordam", callback_data="help"), 
         InlineKeyboardButton("⚙️ Sozlamalar", callback_data="settings")],
        [InlineKeyboardButton("🛠 Maker Bo'lim", callback_data="maker")],
        [InlineKeyboardButton("✉️ Xabar", callback_data="message")]
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

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data == "create_bot":
        await query.edit_message_text(
            "🤖 Yangi bot yaratish\n\n"
            "Bot nomi va tokenini kiriting:",
            reply_markup=main_keyboard()
        )
    elif data == "my_bots":
        await query.edit_message_text(
            "📋 Sizning botlaringiz:\n\n"
            "Hali bot yaratilmagan.",
            reply_markup=main_keyboard()
        )
    elif data == "balance":
        await query.edit_message_text(
            "💰 Balans: 0 so'm\n"
            "💳 To'lov qilish: [link]",
            reply_markup=main_keyboard()
        )
    elif data == "referal":
        await query.edit_message_text(
            "👥 Referal dasturi\n\n"
            "🔗 Havolangiz: https://t.me/makefy_bot?start=ref_123\n"
            "👤 Do'stingiz kelganda: +100 so'm",
            reply_markup=main_keyboard()
        )
    elif data == "web_app":
        await query.edit_message_text(
            "🌐 Web ilova\n\n"
            "Botni to'liq boshqarish uchun:\n"
            "🔗 https://makefy.com/dashboard",
            reply_markup=main_keyboard()
        )
    elif data == "help":
        await query.edit_message_text(
            "❓ Yordam\n\n"
            "📞 Admin: @makefy_admin\n"
            "📧 Email: support@makefy.com",
            reply_markup=main_keyboard()
        )
    elif data == "settings":
        await query.edit_message_text(
            "⚙️ Sozlamalar\n\n"
            "🔹 Til: O'zbekcha\n"
            "🔹 Xabarlar: Yoqilgan",
            reply_markup=main_keyboard()
        )
    elif data == "maker":
        await query.edit_message_text(
            "🛠 Maker Bo'lim\n\n"
            "🔹 Faqat adminlar uchun!\n"
            "🔹 Bot sozlamalari va statistikalar.",
            reply_markup=main_keyboard()
        )
    elif data == "message":
        await query.edit_message_text(
            "✉️ Xabar yozish\n\n"
            "Adminlarga xabar yuboring:",
            reply_markup=main_keyboard()
        )

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 Makefy Bot ishga tushdi...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
