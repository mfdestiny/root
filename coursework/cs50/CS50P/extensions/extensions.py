extension = input("File name: ").strip()

acceptable = [".gif",".jpg",".jpeg",".png",".pdf",".txt",".zip"]

found = 0

for ext in acceptable:
    if extension.casefold().endswith(ext.casefold()) and not found:
        if (ext.casefold() == ".pdf".casefold()):
            found = 1
            print("application/pdf")
        elif (ext.casefold() == ".txt".casefold()):
            found = 1
            print("text/plain")
        elif (ext.casefold() == ".zip".casefold()):
            found = 1
            print("application/zip")
        else:
            found = 1
            if (ext.casefold() == ".jpg".casefold()):
                print("image/jpeg")
            else:
                print("image/" + ext[1:])

if (not found):
    print("application/octet-stream")
