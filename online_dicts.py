class AndhraBharati:

    def check_word(self, word):
        # post https://andhrabharati.com/dictionary/getWM.php
        # formdata {w: word}

        import requests

        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'referer':
            'https://andhrabharati.com/dictionary/index.php?w=%E0%B0%87%E0%B0%B5%E0%B0%BF',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = 'w=' + requests.utils.quote(
            word
        ) + '&token=&opt=' + requests.utils.quote(
            'W|E|N|Y|2|6|7|8|35|50|10|13|14|29|52|1|11|4|12|51|48|49|43|55|54|56|34|36|37|9|44|58|17|18|19|20|21|22|23|24|25|33|15|41|31|32|3|39|38|40|42|45|46|47'
        )

        response = requests.post(
            'https://andhrabharati.com/dictionary/getWM.php',
            headers=headers,
            data=data)

        if 'అడిగిన వాటికి నిఘంటు శోధనలో ఫలితములు లభించలేదు.' in response.text:
            return False

        dictionary_entry = response.text

        return True


class Brown:

    def check_word(self, word):
        # get https://dsal.uchicago.edu/cgi-bin/app/brown_query.py?qs={word}&matchtype=exact

        import requests

        response = requests.get(
            'https://dsal.uchicago.edu/cgi-bin/app/brown_query.py?qs=' +
            requests.utils.quote(word) + '&matchtype=exact')

        if 'No results for search term' in response.text:
            return False

        dictionary_entry = response.text


        return True

class TamilCube:
    def check_word(self, word):
        # post http://dictionary.tamilcube.com/telugu-dictionary/?term=<word>

        import requests

        response = requests.post(
            'http://dictionary.tamilcube.com/telugu-dictionary/?term=' + requests.utils.quote(word))
        
        if "Oops, we can't find the translation for that word." in response.text:
            return False
        
        dictionary_entry = response.text
        
        return True

# tests

test_word_list = ['పని', 'అవి', 'తెలుగు']
test_non_word_list = ['అందంం', 'అవిం', 'తెలుగుం']


def test_andhrabharati():
    ab = AndhraBharati()
    for word in test_word_list:
        assert ab.check_word(word) == True
    for word in test_non_word_list:
        assert ab.check_word(word) == False


def test_brown():
    b = Brown()
    for word in test_word_list:
        assert b.check_word(word) == True
    for word in test_non_word_list:
        assert b.check_word(word) == False

def test_tamilcube():
    tc = TamilCube()
    for word in test_word_list:
        assert tc.check_word(word) == True
    for word in test_non_word_list:
        assert tc.check_word(word) == False

def time_dictionaries():
    import time

    ab = AndhraBharati()
    b = Brown()
    tc = TamilCube()

    start = time.time()
    for word in test_word_list:
        ab.check_word(word)
    avg_time = (time.time() - start) / len(test_word_list)
    print(f'AndhraBharati: {avg_time:.2f}')

    start = time.time()
    for word in test_word_list:
        b.check_word(word)
    avg_time = (time.time() - start) / len(test_word_list)
    print(f'Brown: {avg_time:.2f}')

    start = time.time()
    for word in test_word_list:
        tc.check_word(word)
    avg_time = (time.time() - start) / len(test_word_list)
    print(f'TamilCube: {avg_time:.2f}')

time_dictionaries()