from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler
)
from telegram.error import NetworkError, Conflict
from config import BOT_TOKEN, logger
from handlers.command_handlers import start
from handlers.message_handlers import handle_text_message
from handlers.callback_handlers import handle_button

async def error_handler(update, context):
    """Handle errors in the telegram bot."""
    try:
        if update:
            error_message = f"Error while handling update {update}"
            if update.effective_message:
                await update.effective_message.reply_text(
                    "❌ حدث خطأ. الرجاء المحاولة مرة أخرى."
                )
        else:
            error_message = "Error with no update"

        logger.error(f"{error_message}: {context.error}")

        if isinstance(context.error, NetworkError):
            logger.error(f"Network error occurred: {context.error}")
        elif isinstance(context.error, Conflict):
            logger.error("Conflict error: Another instance of the bot is running")
    except Exception as e:
        logger.error(f"Error in error handler: {e}")

def main() -> None:
    """Initialize and start the bot."""
    try:
        # Initialize the Application
        application = Application.builder().token(BOT_TOKEN).build()

        # Add error handler
        application.add_error_handler(error_handler)

        # Add handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))
        application.add_handler(CallbackQueryHandler(handle_button))

        # Start the bot
        logger.info("Starting bot...")
        application.run_polling(drop_pending_updates=True)
        logger.info("Bot started successfully!")

    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        raise  # Re-raise the exception after logging

if __name__ == "__main__":
    main()