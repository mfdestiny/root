class lexicon(object):
    def __init__(self):
        self.sentence = [('direction', 'north'),('direction', 'south'),('direction', 'east'),('direction', 'west'),('direction', 'down'),('direction', 'up'),('direction', 'left'),('direction', 'right'),('direction', 'back'),('verbs', 'go'),('verbs', 'stop'),('verbs', 'kill'),('verbs', 'eat')]
        #self.sentence = [('direction', 'north'),('direction', 'south'),('direction','east')]


def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None


def scan(request):
    lex = lexicon()
    requested = request.split(' ')
    results = []

    for token1 in requested:
        print(f"{token1}")
        for idx, (word, token2) in enumerate(lex.sentence):
            if (token1 == token2):
                results.append(lex.sentence[idx])

    return results
