import re
from .jisho_api import get_definition

from mmpy_bot.bot import listen_to
from mmpy_bot.bot import respond_to

DEF_RESP_STR = "Word: {}\nEnglish: {}\nKanji: {}\nHiragana/Katakana: {}"

def form_definition_string(word, limit):
    definition_list = get_definition(word, limit)
    resp_str = ""
    for ind, item in enumerate(definition_list):
        resp_str += DEF_RESP_STR.format(item["orig_word"], item["english"],
                                        item["kanji"], item["reading"])
        if ind != len(definition_list) - 1:
            resp_str += '\n\n'
    return resp_str

@respond_to('^Hello', re.IGNORECASE)
def hi(message):
    message.reply('Konichiwa')

@respond_to('^define (.*)', re.IGNORECASE)
@respond_to('^define (.*) (.*)', re.IGNORECASE)
def define(message, word=None, limit_val=None):
    word = word.replace("_", "%20")
    if limit_val is not None:
        def_str = form_definition_string(word, int(limit_val))
        message.reply('{}'.format(def_str))
    else:
        if ' ' not in word:
            def_str = form_definition_string(word, 1)
            message.reply('{}'.format(def_str))

@respond_to('^help', re.IGNORECASE)
@listen_to('^help', re.IGNORECASE)
def help_request(message):
    message.send(message.docs_reply())

define.__doc__ = "Define a word, can provide a limit to the number of definitions shown as well (default 1)"