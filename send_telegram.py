import requests
import os
from logger import logger

def send_telegram(message):

   bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
   bot_chatID = os.getenv('TELEGRAM_BOT_CHAT_ID')

   for var in [bot_token, bot_chatID]:
      if var is None:
         return

   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + message
   logger.info('TELEGRAM sending '+message)
   
   response = requests.get(send_text).json()
   logger.debug('TELEGRAM '+str(response))
