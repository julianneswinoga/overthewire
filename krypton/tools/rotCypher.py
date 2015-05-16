import string

code = raw_input("Input: ").upper()
rot = input("Rot: ")
out = ""
for c in code:
    if (string.ascii_uppercase.find(c) != -1):
        if (ord(c)+rot > ord("Z")):
            out += chr(ord("A")-1+(ord(c)+rot-ord("Z")))
        else:
            out += chr(ord(c) + rot)
    else:
        out += c
print out
