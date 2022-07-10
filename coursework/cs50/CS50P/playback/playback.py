phrase = input()
bag = phrase.split(' ')
new = ""
for word in bag:
    new = new + word + "..."

print(new[:-3])