first = set()
second = set()
with open("Beyondsleep.txt",encoding = 'utf-8') as file:
    for line in file:
        for word in line.split():
           first.add(word)
with open("pride&prejudice.txt",encoding = 'utf-8') as f:
    for l in f:
        for w in l.split():
           second.add(w)

for w in first.intersection(second):
    print (w)
