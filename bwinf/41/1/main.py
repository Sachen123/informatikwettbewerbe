import re

filename = "Alice_im_Wunderland.txt"  # "Alice_im_Wunderland.txt"
taskname = "stoerung" + "1" + ".txt"

buch = open(filename, encoding="utf-8").read().split()
buch2 = open(filename, encoding="utf-8").read().split()
aufgabe = open("stoerung1.txt", encoding="utf-8").read().split()

for i in range(len(buch2)):
    buch2[i] = re.sub(r'[^a-zA-Zßäüö]', '', buch2[i].lower())
    buch[i] = re.sub(r'[^a-zA-Zßäüö]', '', buch[i].lower())

for i in range(len(buch)):
    buch[i] += " "

for j in range(len(buch2)):
    if buch2[j] not in aufgabe:
        buch2[j] = "_"
    else:
        buch2[j] = buch2[j][:1]

for i in range(len(aufgabe)):
    aufgabe[i] = aufgabe[i][:1]

bu = "".join(buch2)
auf = "".join(aufgabe)
index = bu.find(auf)

sentence = ""
for i in range(len(aufgabe)):
    sentence += buch[index+i]

print(sentence)