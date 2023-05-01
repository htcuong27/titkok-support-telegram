from setting import token
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from subprocess import Popen, PIPE


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Open tiktok's Mia")
    
    tiktokFile = Popen(['python3', 'tiktok.py'], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    out, _ = tiktokFile.communicate()
    
    if out == 'Mia is not connect yet':
        await update.message.reply_text("Mia is not online yet 🥺")
    else:
        await update.message.reply_text(f'{out}')
    # except:

app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("start", start))
# app.add_handler(CommandHandler("hello", hello))

app.run_polling()
