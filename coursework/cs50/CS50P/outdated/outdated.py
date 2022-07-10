def main():
    m,d,y,f = prompt()
    transform(m,d,y,f)


def prompt():
    while True:
        try:
            date = input("Date: ").strip()
            #two cases
            mfound = 0
            for i in range(len(date)):
                if (date[i].isspace()): #case 1
                    if date[0].isdecimal():
                        prompt()
                    #month to MM
                    if mfound != 1:
                        month = date[:i]
                        mfound = 1
                elif date[i] == "," and mfound == 1:
                    if (date[i] == ","):
                        if (date[i-2].isdecimal()): #day is ##
                            dfound = int(date[i-2] + date[i-1])
                            if (date[i+1].isspace()):
                                yfound = int(date[i+2:])
                            else:
                                yfound = -1
                            return month,dfound,yfound,0
                        else: #day is #
                            dfound = int(date[i-1])
                            if date[i+1].isspace():
                                yfound = int(date[i+2:])
                            else:
                                yfound = -1
                            return month,dfound,yfound,0
                    else: #incorrect input: no ,
                        prompt()
                elif date[i] == "/" and mfound == 0:
                    if date[0].isalpha():
                        prompt()
                    month = int(date[:i])
                    if month < 1 or month > 12:
                        prompt()
                    mfound = 1
                elif date[i] == "/" and mfound == 1:
                    if (date[i-2].isdecimal()):
                        dfound = int(date[i-2] + date[i-1])
                    else:
                        dfound = int(date[i-1])
                    yfound = date[i+1:]
                    return month,dfound,yfound,1



        except EOFError:
                return print()

def transform(month,day,year,flag):
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    if day > 31:
        prompt()

    if flag == 0: #transform to ####-##-## format
        if month.title() in months:
            try:
                m = months.index(month.title()) + 1
                print(f"{year}-{str(m).zfill(2)}-{str(day).zfill(2)}")
            except ValueError:
                prompt()
        else:
            prompt()
    else:
        if month < 0 or month > 12:
            prompt()
        print(f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}")




main()