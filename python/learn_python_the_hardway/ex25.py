def break_words(stuff):
    """This function will break words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words)

def print_first_word(words):
    """Prints first word after popping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes sentence and sorts words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_last_sorted(sentence):
    """"Sorts words and prints first and last"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
