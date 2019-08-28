import logging

from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

bool active;


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    update.message.reply_text('Hi!')



def runscript(update, context):
    if active:
        update.message.reply_text('You have already a script running')
        return

    chat_id = update.message.chat_id
    try:
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text('Sorry i need a number of the script to run')
            return




        update.message.reply_text('script is succesfully running')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: runscript "Name of script"')


def stopscript(update, context):
    if !active:
        update.message.reply_text('No working script')
        return



    update.message.reply_text('Script succesfully interrupted')
    except (IndexError, ValueError):
        update.message.reply_text('Usage: stopscript "Name of script"')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Run bot."""
    updater = Updater('889724193:AAHtBrmAfxZZmvSICxEYI5VSoATu434JIG4')

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("startscript", startscript,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("stopscript", stopscript, pass_chat_data=True))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
