# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișaza a intra x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări’





list_players = ['Dorel', 'Dorin', 'Radu', 'Paul', 'George']
list_rezerva = ['Marian', 'Marin', 'Anton']
print(f"Echipa este formata din 5 jucatori: {' ,'.join(list_players)}")
print()
schimbari_efectuate = 3
print(f"Putem face maxim {schimbari_efectuate} schimbari")
x =list_players.pop(0)
y =list_rezerva.pop(0)
list_players.append(y)
list_rezerva.append(x)
print()
print(f"A iesit {x} si a intrat {y}")
schimbari_efectuate -=1
print(f"{schimbari_efectuate} schimbari ramase")
x =list_players.pop(0)
y =list_rezerva.pop(0)
list_players.append(y)
list_rezerva.append(x)
print()
print(f"A iesit {x} si a intrat {y}")
schimbari_efectuate -=1
print(f"{schimbari_efectuate} schimbari ramase")
print()

if 'Radu' in list_players and schimbari_efectuate > 0:
    x = list_players.pop(0)
    y = list_rezerva.pop(0)
    list_players.append(y)
    list_rezerva.append(x)
    schimbari_efectuate -= 1
    print(f"A iesit {x} si a intrat {y} si mai sunt posibile {schimbari_efectuate} schimbari.")
else:
    print(f"Nu se poate efectua schimbarea, jucatorul {x} nu este in teren.")
    print(f"Mai ai {schimbari_efectuate} mutari.")
    print()
print(f"Echipa jucatori: {' ,'.join(list_players)}")
print(f"Rezerva jucatori: {' ,'.join(list_rezerva)}")



