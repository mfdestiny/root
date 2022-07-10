from validator_collection import validators, checkers, errors

def main():
    print(verify(input("What's your email address? ")))

def verify(s):
    is_email_address = checkers.is_email(s)
    if is_email_address:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()