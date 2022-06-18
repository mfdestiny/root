class lexicon(object):
    def __init__(self):
        self.sentence = [('direction', 'north'),('direction', 'south'),('direction', 'east'),('direction', 'west'),('direction', 'down'),('direction', 'up'),('direction', 'left'),('direction', 'right'),('direction', 'back'),('verb', 'go'),('verb', 'stop'),('verb', 'kill'),('verb', 'eat'),('stop', 'the'),('stop', 'in'),('stop', 'of'),('stop', 'from'),('stop', 'at'),('stop', 'it'),('noun', 'door'),('noun', 'bear'),('noun', 'princess'),('noun', 'cabinet'),('number', 1234),('number', 3),('number', 91234)]

def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(request):
    lex = lexicon()
    requested = request.split(' ')
    results = []

    for requested_word in requested:
        found_word = False
        found_number = False

        for item in range(0,len(lex.sentence)):#iterates through requests
            if (not found_word): #keep searching for word
                if (requested_word == lex.sentence[item][1]):#word matches add to results
                    found_word = True
                    results.append(lex.sentence[item]) #add to list

            if (not found_number):#search for number
                if (convert_numbers(requested_word) == lex.sentence[item][1]):#number matches
                    found_number = True
                    results.append(lex.sentence[item]) #add to list

        if (not found_number and not found_word): # if nothing was matches return error
            results.append(('error', requested_word))

    return results
