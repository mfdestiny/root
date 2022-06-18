class lexicon(object):
    def __init__(self):
        self.sentence = [('direction', 'north'),('direction', 'south'),('direction', 'east'),('direction', 'west'),('direction', 'down'),('direction', 'up'),('direction', 'left'),('direction', 'right'),('direction', 'back'),('verb', 'go'),('verb', 'stop'),('verb', 'kill'),('verb', 'eat'),('stop', 'the'),('stop', 'in'),('stop', 'of'),('stop', 'from'),('stop', 'at'),('stop', 'it'),('noun', 'door'),('noun', 'bear'),('noun', 'princess'),('noun', 'cabinet'),('number', 1234),('number', 3),('number', 91234)]

def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None


def scan(request):
    #creates lexicon object
    lex = lexicon()
    #splits words
    requested = request.split(' ')
    results = []

    #for each word requested, iterate through available list and if found add it to the empty results array and return array
    for requested_word in requested:
        for idx, (type, word_in_list) in enumerate(lex.sentence):
            if (type == 'number'): #number in list
                if (convert_numbers(requested_word) == word_in_list):
                    results.append(lex.sentence[idx])
            elif (requested_word == word_in_list): #word in list
                results.append(lex.sentence[idx])
            else: #does not exist in list
                results.append(('error',requested_word))



    return results
