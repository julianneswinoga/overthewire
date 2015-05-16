import string

def contains(lis, chk):
    for i in lis:
        if (i == chk):
            return True
    return False

text = raw_input("Text: ").lower().translate(None, " ")
alpha = [0]*len(string.ascii_lowercase)
alphabet = string.ascii_lowercase
mat2 = [[0 for x in range(len(string.ascii_lowercase))] for x in range(len(string.ascii_lowercase))]
mat3 = [[[0 for x in range(len(string.ascii_lowercase))] for x in range(len(string.ascii_lowercase))] for x in range(len(string.ascii_lowercase))]
repeats = [0]*len(string.ascii_lowercase)

for i,c in enumerate(text):
    if (string.ascii_lowercase.find(c) != -1):
        alpha[ord(c)-ord("a")] += 1
        try:
            mat2[alphabet.find(c)][alphabet.find(text[i+1])] += 1
        except:
            True=True
        try:
            mat3[alphabet.find(c)][alphabet.find(text[i+1])][alphabet.find(text[i+2])] += 1
        except:
            True=True
        try:
            if (text[i] == text[i+1]):
                repeats[alphabet.find(c)] += 1
        except:
            True=True
    

print "Frequency: "
for i in range(len(alpha)):
    print chr(i+ord("a"))+": \t"+str(1.0*alpha[i]/len(text))

print "Sorted: "
sort = sorted(alpha)
sort.reverse()
for i in range(len(alpha)):
    print chr(alpha.index(sort[i])+ord("a"))+": \t"+str(1.0*alpha[alpha.index(sort[i])]/len(text))

# Bigram
rank = []
ranka = []
for p in range(10):
    rank.append(0)
    ranka.append("")
    for top,i in enumerate(mat2):
        for side,k in enumerate(i):
            if (k > rank[p] and not contains(rank, k)):
                rank[p] = k
                ranka[p] = alphabet[top]+alphabet[side]
print rank
print ranka

# Trigrams
rank = []
ranka = []
for p in range(10):
    rank.append(0)
    ranka.append("")
    for top,i in enumerate(mat3):
        for side,k in enumerate(i):
            for dep,j in enumerate(k):
                if (j > rank[p] and not contains(rank, j)):
                    rank[p] = j
                    ranka[p] = alphabet[top]+alphabet[side]+alphabet[dep]
print rank
print ranka

# Repeats
thinger = []
for k,m in enumerate(repeats):
    thinger.append([[repeats[k]], chr(k+ord("a"))])

sort = sorted(thinger)
sort.reverse()
for i in range(len(sort)):
    print sort[i][1]*2 + ": " + str(sort[i][0])
