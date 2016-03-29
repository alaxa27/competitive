import sys

tab = []
while True:
    try:
        tab.append(input())
    except:
        break




for i in range(0, len(tab)):
    if int(tab[i]) == 42:
        break
    print tab[i]


