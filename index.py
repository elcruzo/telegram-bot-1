#First install Telegram, and search the keywords "BotFather Bot"
#Start interacting with the Bot on the telegram bot


import telegram.ext
import pandas_datareader as web

with open('token.txt', 'r') as f:
    TOKEN = f.read()
    
    
def start(update, context):
    update.message.reply_text("Hello! Welcome to ElCruzoBot!")
    
def help(update, context):
    update.message.reply_text("""
    The following commands are available:
    
    /start -> Welcome Message
    /help -> This Message
    /content -> Information About ElCruzo
    /contact -> Information about Contact                        
                              
    """)
    
def content(update, context):
    update.messsage.reply_text("We have videos and books! Watch and read them!")
    
def contact(update, context):
    update.message.reply_text("You can contact ElCruzo by email - dev.elcruzo@gmail.com")        

def stock(update, context):
    ticker = context.args[0]
    data = web.DataReader(ticker, 'yahoo')
    price = data.iloc[-1]['Close']
    update.message.reply_text(f"The current price of {ticker} is {price:.2f}$!")
    

def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}")    
    
    
updater = telegram.ext.Updater(TOKEN, use_content=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("stock", stock))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))



updater.start_polling()
updater.idle()




