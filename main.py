
from typing import DefaultDict, Optional, Set
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
    Update,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
import asyncio
import os

# from dotenv import load_dotenv
# load_dotenv()

# TOKEN = os.getenv("TOKEN")

# init User Info in the database
def setUserId(context: ContextTypes.DEFAULT_TYPE):
    # Reply Buttons when click '/start'
    startGameButton = InlineKeyboardButton(
        text="Start the Game!",
        web_app=WebAppInfo(
            "https://hamie-game-telegram.vercel.app?user_id={}".format(
                context.chat_data["userId"]
            )
        ),
    )

    configKeyboardMarkup = InlineKeyboardMarkup(
        [
            [startGameButton],
            # [connectWallet, referralUser, userProfile],
        ]
    )

    return configKeyboardMarkup

# start commmand
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get User ID
    context.chat_data["userId"] = update.effective_message.chat_id
    # Set User
    configKeyboardMarkup = setUserId(context)
    photo_file = open("./public/background.png", "rb")

    # Hello Message
    descText = f"""
    Welcome to Hamie's Escape! 🌟\n\nGet ready for an exhilarating adventure! Collect CryptoCoins for extra rewards and challenge yourself to beat your high score in endless gameplay!\n\nJoin the fun and see how far you can go! 🚀✨
    """
    # certification = f"\n<b>Made with ❤️ by Bitcoin Millionaire Team</b>"

    # Send the image with the text
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=photo_file,
        caption=descText,
        reply_markup=configKeyboardMarkup,
    )

if __name__ == "__main__":
    # start the bot
    print("Starting bot...")
    application = Application.builder().token("7829283459:AAFB5zSo5Eckqjc9RW7WXFoSFin74_i8heg").build()

    # Add handler to the bot
    application.add_handler(CommandHandler("start", start))
    
    # Check if running on Windows
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)
