from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Botunuzun API Token'ı
API_TOKEN = '7282375565:AAEHPShSBHWlSNgvbgDdLODxmJQrrn1auPc'

# /start komutunu işle
def start(update: Update, context: CallbackContext):
    user_id = update.messpython bot.pyage.from_user.id
    update.message.reply_text(f'Merhaba! User ID\'niz: {user_id}')

# Botu başlat
def main():
    updater = Updater(API_TOKEN)  # use_context parametresi kaldırıldı
    dp = updater.dispatcher

    # /start komutunu ekle
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()