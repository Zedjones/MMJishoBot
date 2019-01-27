import requests

API_URL = "https://jisho.org/api/v1/search/words?keyword={}"

HIRAGANA_DICT = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko', 
    'きゃ': 'kya', 'きゅ': 'kyu', 'きょ': 'kyo',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'しゃ': 'sha', 'しゅ': 'shu', 'しょ': 'sho',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'ちゃ': 'cha', 'ちゅ': 'chu', 'ちょ': 'cho',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'にゃ': 'nya', 'にゅ': 'nyu', 'にょ': 'nyo',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ひゃ': 'hya', 'ひゅ': 'hyu', 'ひょ': 'hyo',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'みゃ': 'mya', 'みゅ': 'myu', 'みょ': 'myo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'りゃ': 'rya', 'りゅ': 'ryu', 'りょ': 'ryo',
    'わ': 'wa', 'ゐ': 'wi', 'ゑ': 'we', 'を': 'wo',
    'ん': 'n', 'っ': 'sokuon',
    'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
    'ぎゃ': 'gya', 'ぎゅ': 'gyu', 'ぎょ': 'gyo',
    'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo',
    'じゃ': 'ja', 'じゅ': 'ju', 'じょ': 'jo',
    'だ': 'da', 'ぢ': 'dji', 'づ': 'dzu', 'で': 'de', 'ど': 'do',
    'ぢゃ': 'ja', 'ぢゅ': 'ju', 'ぢょ': 'jo',
    'ば': 'ba', 'び': 'bi', 'ぶ': 'bu', 'べ': 'be', 'ぼ': 'bo',
    'びゃ': 'bya', 'びゅ': 'byu', 'びょ': 'byo',
    'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po',
    'ぴゃ': 'pya', 'ぴゅ': 'pyu', 'ぴょ': 'pyo'
}

SMALL_HIRAGANA_LIST = [
    'ゅ', 'ゃ', 'ょ'
]

CONSONANTS = "bcdfghjklmnpqrstvwxyz"

KATAKANA_DICT = {
    'ア': 'a', 'イ': 'i', 'ウ': 'u', 'エ': 'e', 'オ': 'o', 'ン': 'n',
    'ァ': 'a', 'ィ': 'i', 'ゥ': 'u', 'ェ': 'e', 'ォ': 'o',
    'カ': 'ka', 'キ': 'ki', 'ク': 'ku', 'ケ': 'ke', 'コ': 'ko',
    'ガ': 'ga', 'ギ': 'gi', 'グ': 'gu', 'ゲ': 'ge', 'ゴ': 'go',
    'サ': 'sa', 'シ': 'shi', 'ス': 'su', 'セ': 'se', 'ソ': 'so',
    'ザ': 'za', 'ジ': 'zi', 'ズ': 'zu', 'ゼ': 'ze', 'ゾ': 'zo',
    'タ': 'ta', 'チ': 'chi', 'ツ': 'tsu', 'テ': 'te', 'ト': 'to',
    'ダ': 'da', 'ヂ': 'di', 'ヅ': 'du', 'デ': 'de', 'ド': 'do',
    'ナ': 'na', 'ニ': 'ni', 'ヌ': 'nu', 'ネ': 'ne', 'ノ': 'no',
    'ハ': 'ha', 'ヒ': 'hi', 'フ': 'hu', 'ヘ': 'he', 'ホ': 'ho',
    'バ': 'ba', 'ビ': 'bi', 'ブ': 'bu', 'ベ': 'be', 'ボ': 'bo',
    'ボ': 'pa', 'ピ': 'pi', 'プ': 'pu', 'ペ': 'pe', 'ポ': 'po',
    'マ': 'ma', 'ミ': 'mi', 'ム': 'mu', 'メ': 'me', 'モ': 'mo',
    'ヤ': 'ya', 'ユ': 'yu', 'ヨ': 'yo',
    'ラ': 'ra', 'リ': 'ri', 'ル': 'ru', 'レ': 're', 'ロ': 'ro',
    'ワ': 'wa', 'ヰ': 'wi', 'ヱ': 'we', 'ヲ': 'wo',
    'ッ': 'sokuon', 'ー': 'ー',
    'ャ': 'ya', 'ュ': 'yu', 'ョ': 'yo',
    'キャ': 'kya', 'キュ': 'kyu', 'キョ': 'kyo',
    'シャ': 'sha', 'シュ': 'shu', 'ショ': 'sho',
    'チャ': 'cha', 'チュ': 'chu', 'チョ': 'cho',
    'ニャ': 'nya', 'ニュ': 'nyu', 'ニョ': 'nyo',
    'ヒャ': 'hya', 'ヒュ': 'hyu', 'ヒョ': 'hyo',
    'ミャ': 'mya', 'ミュ': 'myu', 'ミョ': 'myo',
    'リャ': 'rya', 'リュ': 'ryu', 'リョ': 'ryo',
    'ギャ': 'gya', 'ギュ': 'gyu', 'ギョ': 'gyo',
    'ジャ': 'ja', 'ジュ': 'ju', 'ジョ': 'jo',
    'ヂャ': 'ja', 'ヂュ': 'ju', 'ヂョ': 'jo',
    'ビャ': 'bya', 'ビュ': 'byu', 'ビョ': 'byo',
    'ピャ': 'pya', 'ピュ': 'pyu', 'ピョ': 'pyo'
}

SMALL_KATAKANA_LIST = {
    'ャ', 'ュ', 'ョ'
}

def hiragana_to_romaji(hiragana):
    romaji = []
    for ind, char in enumerate(hiragana):
        if char in SMALL_HIRAGANA_LIST:
            del(romaji[-1])
            romaji.append(HIRAGANA_DICT[hiragana[ind-1] + char])
        elif HIRAGANA_DICT[char] == 'sokuon':
            romaji.append("".join([c for c in HIRAGANA_DICT[hiragana[ind+1]] if c in CONSONANTS]))
        else:
            romaji.append(HIRAGANA_DICT[char])
    return "".join(romaji)

def katakana_to_romaji(katakana):
    romaji = []
    for ind, char in enumerate(katakana):
        if char in SMALL_KATAKANA_LIST:
            del(romaji[-1])
            romaji.append(KATAKANA_DICT[katakana[ind-1] + char])
        elif KATAKANA_DICT[char] == "sokuon":
            romaji.append("".join([c for c in KATAKANA_DICT[katakana[ind+1]] if c in CONSONANTS]))
        else:
            romaji.append(KATAKANA_DICT[char])
    return "".join(romaji)

def get_definition(word, limit=1):
    formatted_url = API_URL.format(word)
    result = requests.get(formatted_url)
    res_dict = result.json()["data"]
    definition_list = []
    for ind in range(0, limit):
        if ind < len(res_dict):
            definition = res_dict[ind]

            ind = 0 
            japanese = definition["japanese"][ind]
            kanji, reading = japanese.get('word'), japanese.get('reading')
            orig_kanji, orig_reading = kanji, reading
            while kanji is None or reading is None:
                japanese = definition["japanese"][ind]
                kanji, reading = japanese.get('word'), japanese.get('reading')
                ind += 1
                if ind == len(definition["japanese"]):
                    kanji, reading = orig_kanji, orig_reading
                    break

            senses = definition["senses"][0]
            english = ",".join([str(x) for x in senses['english_definitions']])

            if all([char in KATAKANA_DICT or char in SMALL_KATAKANA_LIST for char in reading]):
                romaji = katakana_to_romaji(reading)
            else:
                romaji = hiragana_to_romaji(reading)

            definition_dict = {
                'kanji': kanji,
                'reading': reading,
                'english': english,
                'orig_word': word.replace("%20", " "),
                'romaji': romaji
            }
            definition_list.append(definition_dict)
    return definition_list


if __name__ == '__main__':
    print(get_definition("ショ", 3))