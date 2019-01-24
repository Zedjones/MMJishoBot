import requests

API_URL = "https://jisho.org/api/v1/search/words?keyword={}"

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

            definition_dict = {
                'kanji': kanji,
                'reading': reading,
                'english': english,
                'orig_word': word.replace("%20", " ")
            }
            definition_list.append(definition_dict)
    return definition_list


if __name__ == '__main__':
    print(get_definition("watashi"))