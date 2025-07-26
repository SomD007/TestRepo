
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, ContextTypes, JobQueue
import time


"""
import pprint #

import asyncio
from telegram import Bot
from datetime import datetime, timedelta
import logging

"""


"""
#configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level= logging.INFO)
logger = logging.getLogger(__name__)
TARGET_USER_ID = 5952787525

"""


TOKEN = "7593172741:AAFtOHYaP2FtJaJq5841kx-VPTxngMzRkB0"

# Start Command
async def start(update: Update, context: CallbackContext):
    
    #storing the user id
    user_id = update.effective_user.id
    
    await update.message.reply_text("Hello! I am your bot. How can I help you?")



# Echo Messages
async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(update.message.text)
    
    
    
#Help Command
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("You can use the following commands:\n/start - Start the Bot\n/help - Show Avalable commands\n")
    
    
    
#about command
async def about_command(update: Update,context: CallbackContext):
    await update.message.reply_text("This is MySDbot !\nI am Practice bot made by SD\nI have few functionality, you can view them by typing \help command in the chat.\nFeel free to try them.")
    
    #print(pprint.pprint(vars(update)))
    
#timer command
async def timer_command(update: Update,context: CallbackContext):
    user_id = update.effective_user.id
    time.sleep(6)
    
    await context.bot.send_message(chat_id = user_id, text = f"Update after 6 seconds {update} \n Context: {CallbackContext}")
    
    
"""    
#create bot instance
bot = Bot(token = TOKEN)


#send delayed message

async def setup_delayed_message(context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now()
    job_time = now + timedelta(seconds = 6)
    message = "Hello"
    
    await context.bot.send_message(chat_id=TARGET_USER_ID,text=message)
    
    logger.info(f"Delayed message sent to {TARGET_USER_ID}")
    
"""    
        
    

def main():
    app = Application.builder().token(TOKEN).build()

#adding commands to the bot
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help",help_command))
    app.add_handler(CommandHandler("about",about_command))
    app.add_handler(CommandHandler("timer",timer_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


    """
    app.job_queue  = app.job_queue or JobQueue()
    
    app.job_queue.set_application(app)
    app.job_queue.start()

    """
    #job_queue = app.job_queue


    #Schedule the delayed Message
    #app.job_queue.run_once(setup_delayed_message,6)
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
    