import requests
import os
from logger import logger
from load_config import *

config = load_config('config.yml')
bot_token = config['TELEGRAM']['BOT_TOKEN']
bot_chatID = str(config['TELEGRAM']['BOT_CHAT_ID'])

send_success = True

def send_telegram(message):

   global send_success

   if send_success:

      for var in [bot_token, bot_chatID]:
         if var is None:
            return

      send_text = 'https://api.telegram.org/botX' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + message
      logger.info('TELEGRAM sending '+message)
      
      response = requests.get(send_text)
      logger.debug('TELEGRAM '+str(response.json()))

      if response.status_code != 200:
         logger.info('failed to send telegram message, disabling')
         send_success = False
      else:
         send_success = True

   else:
      logger.debug('Not sending to telegram, last send failed')