import json
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ---------- Logging ----------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ---------- Load Scores ----------
def load_scores():
    with open("scores.json", "r", encoding="utf-8") as f:
        return json.load(f)

# ---------- Commands ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🏸 *សូមស្វាគមន៍មកកាន់ បក្សីកីឡា-SB24 Score Bot!*\n\n"
        "បញ្ជាដែលអ្នកអាចប្រើ:\n"
        "• /today – មើលពិន្ទុថ្ងៃនេះ\n"
        "• /fixtures – មើលការប្រកួតខាងមុខ\n"
        "• /results – មើលលទ្ធផលចុងក្រោយ\n"
        "• /help – ជំនួយ"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "ℹ️ *ជំនួយ*\n\n"
        "ប្រើបញ្ជាខាងក្រោម:\n"
        "/today – ពិន្ទុបច្ចុប្បន្ន\n"
        "/fixtures – ការប្រកួតខាងមុខ\n"
        "/results – លទ្ធផលចុងក្រោយ\n"
        "/help – បង្ហាញសារនេះ"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = load_scores()
    matches = data.get("today", [])

    if not matches:
        await update.message.reply_text("📭 គ្មានការប្រកួតថ្ងៃនេះទេ។")
        return

    text = "📅 *ពិន្ទុថ្ងៃនេះ*\n\n"
    for m in matches:
        text += (
            f"🏸 *{m['team_a']}* vs *{m['team_b']}*\n"
            f"   ពិន្ទុ: `{m['score_a']} - {m['score_b']}`\n"
            f"   ស្ថានភាព: {m['status']}\n"
            f"   ម៉ោង: {m['time']}\n\n"
        )
    await update.message.reply_text(text, parse_mode="Markdown")

async def fixtures(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = load_scores()
    matches = data.get("fixtures", [])

    if not matches:
        await update.message.reply_text("📭 គ្មានការប្រកួតខាងមុខទេ។")
        return

    text = "🗓 *ការប្រកួតខាងមុខ*\n\n"
    for m in matches:
        text += (
            f"🏸 *{m['team_a']}* vs *{m['team_b']}*\n"
            f"   កាលបរិច្ឆេទ: {m['date']}\n"
            f"   ម៉ោង: {m['time']}\n"
            f"   ទីតាំង: {m['venue']}\n\n"
        )
    await update.message.reply_text(text, parse_mode="Markdown")

async def results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = load_scores()
    matches = data.get("results", [])

    if not matches:
        await update.message.reply_text("📭 គ្មានលទ្ធផលចុងក្រោយទេ។")
        return

    text = "✅ *លទ្ធផលចុងក្រោយ*\n\n"
    for m in matches:
        text += (
            f"🏸 *{m['team_a']}* {m['score_a']} - {m['score_b']} *{m['team_b']}*\n"
            f"   កាលបរិច្ឆេទ: {m['date']}\n\n"
        )
    await update.message.reply_text(text, parse_mode="Markdown")

# ---------- Main ----------
def main():
    import os
    token = os.environ.get("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_TOKEN environment variable is not set!")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("today", today))
    app.add_handler(CommandHandler("fixtures", fixtures))
    app.add_handler(CommandHandler("results", results))

    logger.info("Bot is starting...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
