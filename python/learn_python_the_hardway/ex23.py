import sys
#command line arguments sent at as variables
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    #read line from language file
    line = language_file.readline()
    if line: #if line exists then:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) #repeat until no lines exist

def print_line(line, encoding, errors):
    next_lang = line.strip() #strips line parsing
    raw_bytes = next_lang.encode(encoding, errors=errors) #encoding string w/ encoding
    cooked_string = raw_bytes.decode(encoding, errors=errors) #decode bytes w/ encoding

    print(raw_bytes, "<====>", cooked_string)

languages = open("languages.txt", encoding="utf-8")
#call main function
main(languages, input_encoding, error)
