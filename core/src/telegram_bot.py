import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, ConversationHandler, \
    MessageHandler, Filters

from bot import CheifBot

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

bot = CheifBot(logger)


def find_between_r(origin_text: str, first: str, last: str):
    try:
        start = origin_text.rindex(first) + len(first)
        end = origin_text.rindex(last, start)
        return origin_text[start:end]
    except ValueError:
        return ""


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello, welcome to CiVil Bot")


def process_query(update: Update, context: CallbackContext) -> None:
    """process the user message."""
    user_input = update.message.text
    text, reply_markup = get_answer(update, user_input=user_input, button_intent="")
    update.message.reply_text(text, reply_markup=reply_markup)


def get_answer(update, user_input: str, button_intent: str):
    result = bot.get_answer("", user_input, intent_info=button_intent)
    logger.info('result: {}'.format(result))
    response = result.get('response')
    buttons = response.get('buttons')
    if buttons:
        button_list = []
        for item in buttons:
            button_list.append([InlineKeyboardButton(item.get('title'),
                                                     callback_data="[{}]".format(item.get('payload').replace('/', '')))])

        logger.info("button_list: {}".format(button_list))
        reply_markup = InlineKeyboardMarkup(button_list)
        return response.get('text'), reply_markup
    else:
        return response.get('text'), None


def done(update: Update, context: CallbackContext) -> int:
    """Display the gathered info and end the conversation."""
    # user_data = context.user_data
    # if 'choice' in user_data:
    #     del user_data['choice']
    #
    update.message.reply_text(
        "Thanks for using the CiViL Bot."
    )

    # user_data.clear()
    return ConversationHandler.END


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    text, reply_markup = get_answer(update, user_input="", button_intent=find_between_r(query.data, "[", "]"))
    query.answer()
    query.edit_message_text(text=text, reply_markup=reply_markup)


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bots token.
    updater = Updater("2139720036:AAHLPCgkGjce4c5mSPDgpoxDGNSqNCIqSMg", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_query))
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()

