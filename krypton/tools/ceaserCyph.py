import string

code = raw_input("Input: ").upper()
for rot in range(1,27):
    out = ""
    print str(rot)+":"
    for c in code:
        if (string.ascii_uppercase.find(c) != -1):
            if (ord(c)+rot > ord("Z")):
                out += chr(ord("A")-1+(ord(c)+rot-ord("Z")))
            else:
                out += chr(ord(c) + rot)
        else:
            out += c
    print out
