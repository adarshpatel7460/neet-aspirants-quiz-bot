from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = 8849077595:AAHPhZMYrX2fMVmaH1P_gfa0Xq8xWAKJhLI

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to NEET Aspirants Quiz Bot!\n\nType /quiz to start."
    )

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_poll(
        question="Human heart has how many chambers?",
        options=["2", "3", "4", "5"],
        type="quiz",
        correct_option_id=2,
        explanation="The human heart has 4 chambers."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("quiz", quiz))

print("Bot is running...")
app.run_polling()
