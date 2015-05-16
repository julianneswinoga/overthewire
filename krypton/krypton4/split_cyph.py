text = raw_input("Text: ").replace(" ", "")
keyLength = input("Key length: ")



thing = ""
for i,c in enumerate(text):
    if (i == 0):
        i = 1
    if (i % keyLength == 0):
        print thing
        thing = c
    else:
        thing += c
