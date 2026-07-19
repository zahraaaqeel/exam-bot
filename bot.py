from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8842055092:AAEFghlRf-OVaoBO-oDJ-2ENxgk3VAMgPe8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً 🌹\nأرسل ملف PDF للإجابة وسأستلمه."
    )

async def receive_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "تم استلام ملف PDF ✅"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Document.PDF, receive_pdf))

app.run_polling()
