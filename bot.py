#import libraries

import os

from dotenv import load_dotenv

from functions import start,reply,data,generate,nopicture

from telegram import Update

from telegram.ext import Application,CommandHandler,ContextTypes,MessageHandler, filters,Updater

#get env file information
load_dotenv()

# get telegram bot token
token = os.getenv("API_BOT")



def main ():
    #define as global to use it in this function
    global user_data,picture_name
    #initalize variables (remove all data)
    user_data = ""
    picture_name = ""
    
    application = Application.builder().token(token).build()
    #when user type /start
    application.add_handler(CommandHandler("start", start))
    #when user upload picture of file image
    application.add_handler(MessageHandler(filters.PHOTO, reply))
    #when user type /data
    application.add_handler(CommandHandler("data", data))
    #when user type /generate
    application.add_handler(CommandHandler("generate", generate))
    #when user type /nopicture
    application.add_handler(CommandHandler("nopicture", nopicture))
    # listen to any message from users
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()