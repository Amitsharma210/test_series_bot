import json
import logging
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

# Load config
with open('config.json') as config_file:
    config = json.load(config_file)

# Logging setup
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# Initialize bot and set authorized users
bot_token = config['telegram_bot_token']
authorized_users = config['authorized_users']
bot = Bot(token=bot_token)

# Command to start the bot
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    if user.username in authorized_users:
        update.message.reply_text("Welcome to the Test Series Bot! Use /test to access tests.")
    else:
        update.message.reply_text("Access denied. Contact the admin.")

# Command to fetch a test
def get_test(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    if user.username in authorized_users:
        with open('templates/sample_test.html', 'r') as f:
            test_content = f.read()
        update.message.reply_text("Test:")
        update.message.reply_html(test_content)
    else:
        update.message.reply_text("Access denied. Contact the admin.")

# Main function
def main():
    updater = Updater(token=bot_token)
    dp = updater.dispatcher

    # Handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('test', get_test))

    # Start bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
