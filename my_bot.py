from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
from TOKEN import TOKEN

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Використай /remind <секунди> <повідомлення>")

# Команда /remind <секунди> <текст>
async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Формат: /remind <секунди> <повідомлення>")
        return

    try:
        delay = int(context.args[0])
        message = ' '.join(context.args[1:])
        user_id = update.message.chat_id

        await update.message.reply_text(f"Нагадування заплановано через {delay} секунд")

        # Затримка і надсилання
        await asyncio.sleep(delay)
        await context.bot.send_message(chat_id=user_id, text=f"⏰ Нагадування: {message}")
    except ValueError:
        await update.message.reply_text("Невірний формат. Вкажи число секунд!")

# Основна функція запуску бота
def main():
    BOT_TOKEN = TOKEN

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("remind", remind))

    print("Бот запущено...")
    app.run_polling()

if __name__ == "__main__":
    main()
