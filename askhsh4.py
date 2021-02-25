import random
with open("mytext.txt", "r", encoding="utf-8") as f:
    lines = f.read()


    for line in lines:
        if not line.isalpha():
          lines = lines.replace(line, " ", 1)
    lines = lines.lower()

    x = lines.split()
    print(x)
    triades = []
    for i in range(len(x)-1):
        t =' '.join((x[i:i+3]))
        print(t)
        triades.append(t)
    
    z = []
    for i in range(len(x)-1):
        z.append((x[i:i+3]))
    print(z)
    tyxaia = random.choice(z)
    arxiki = tyxaia
    print(tyxaia)
    found = []
    newtext = []
    words = 0
    for i in range(len(z)-1):
        if (z[i][0] == tyxaia[1]) and (z[i][1] == tyxaia[2]):
            words += 3
            found.append(z[i])
            x = (random.choice(found))
            newtext.append(x[2])
            tyxaia = z[i]
            found = []
            i = 0
        if words == 200:
            break

    joinedtext = arxiki + newtext
    print(' '.join(joinedtext))






    




