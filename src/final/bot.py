import logging
import os

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)

from src.final.summarization import Summarizer

summarizer = Summarizer()

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_markdown_v2(
        rf"Привет\! Я *LoL Didn\'t Read* Бот\. Могу сократить твое время на чтение длиннопостов или новостей\!",
    )
    gif = open("resources/lol_didnt_read.gif", "rb")
    update.message.reply_animation(gif)


def reply_summarized_text(update, context):
    update.message.reply_text(summarizer.summarize_text(update.message.text)[0])


def main():
    TOKEN = os.environ["TELEGRAM_BOT_KEY"]
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_summarized_text))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
