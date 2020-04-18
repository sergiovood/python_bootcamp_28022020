usr_txt = input("Podaj tekst: ")
counts = dict()

for sign in usr_txt:
    if sign in counts:
        counts[sign] = counts[sign] + 1
    else:
        counts[sign] = 1
print(counts)

##################

for sign in usr_txt:
    counts[sign] = counts.get(sign, 0) + 1
print(counts)

###################

for sign in usr_txt:
    counts[sign] = usr_txt.count(sign)
print(counts)

##############

from collections import defaultdict

counts = defaultdict(int)
for sign in usr_txt:
    counts[sign] += 1
print("___:", counts)