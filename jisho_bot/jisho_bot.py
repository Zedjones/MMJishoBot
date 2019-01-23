import re

from mmpy_bot.bot import listen_to
from mmpy_bot.bot import respond_to

@respond_to('^Hello', re.IGNORECASE)
def hi(message):
    message.reply('Konichiwa')

@respond_to('^define (.*)', re.IGNORECASE)
@respond_to('^define (.*) (.*)', re.IGNORECASE)
def define(message, word=None, limit_val=None):
    if limit_val is not None:
        print(word, limit_val)
        message.reply('Define: {}, limit: {}'.format(word, limit_val))
    else:
        if ' ' not in word:
            message.reply('Define: {}'.format(word))

@respond_to('^help', re.IGNORECASE)
@listen_to('^help', re.IGNORECASE)
def help_request(message):
    message.send(message.docs_reply())

define.__doc__ = "Define a word, can provide a limit to the number of definitions shown as well (default 1)"