import re

from mmpy_bot.bot import listen_to
from mmpy_bot.bot import respond_to

@respond_to('Hello', re.IGNORECASE)
def hi(message):
    message.reply('Konichiwa')
