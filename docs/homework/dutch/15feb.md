# Logische Puzzels: Vijf voor Vandaag
Datum: 15 feb 2026
Onderwerp: Loops, Voorwaarden & Twee Loops

*Vijf puzzels—de laatste twee hebben twee loops nodig (genest of de een na de ander).*

## Puzzel 1: De Verzamelaar van Even Getallen
**Het Verhaal**: Een robot moet langs dozen lopen genummerd 1, 2, 3, … tot 50. Hij mag alleen een doos meenemen als het nummer **even** is. Elk meegenomen getal telt hij op bij zijn lopende totaal.

**De Vraag**: Wat is het **totaal** van alle even getallen van 1 tot 50? (Dus: 2 + 4 + 6 + … + 50.)

**Voorbeeld Test**:
- Als het bereik 1 tot 10 was: even getallen zijn 2, 4, 6, 8, 10 → totaal = **30**.

**Hint**: Loop van 1 tot 50. In de loop gebruik je `if getal % 2 == 0:` om te controleren of het getal even is. Zo ja, tel het op bij een variabele zoals `totaal`.

**Controleer je Logica**:
- Voor 1 tot 10: totaal = **30**.
- Voor 1 tot 50: totaal = **650**.

```python
# Start Code
totaal = 0

for getal in range(1, 51):
    # Als getal even is, tel het op bij totaal
    pass

print(f"Totaal van even getallen (1 tot 50): {totaal}")
```

---

## Puzzel 2: De Vijfjes-Teller
**Het Verhaal**: Een juf heeft een lijst met stoelnummers van 1 tot 100. Ze wil weten hoeveel stoelen in rijen zitten die een "groepsprijs" krijgen—dat zijn precies de rijen waarvan het nummer deelbaar is door 5 (5, 10, 15, …, 100).

**De Vraag**: Hoeveel getallen van 1 tot 100 zijn **deelbaar door 5**? (Tel ze.)

**Voorbeeld Test**:
- Als het bereik 1 tot 20 was: de veelvouden van 5 zijn 5, 10, 15, 20 → aantal = **4**.

**Hint**: Loop van 1 tot 100. Gebruik `if getal % 5 == 0:` en tel dan 1 op bij een teller.

**Controleer je Logica**:
- Voor 1 tot 20: aantal = **4**.
- Voor 1 tot 100: aantal = **20**.

```python
# Start Code
aantal = 0

for getal in range(1, 101):
    # Als getal deelbaar is door 5, tel 1 op bij aantal
    pass

print(f"Getallen deelbaar door 5 (1 tot 100): {aantal}")
```

---

## Puzzel 3: De Som van de Eerste Oneven Getallen
**Het Verhaal**: De eerste **oneven** getallen zijn 1, 3, 5, 7, 9, … (elk is 2 meer dan het vorige). Je wilt de som van de **eerste 10** daarvan: 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19.

**De Vraag**: Wat is die totaalsom?

**Voorbeeld Test**:
- Eerste 3 oneven getallen: 1 + 3 + 5 = **9**.

**Hint**: Je kunt 10 keer loopen. Het 1e oneven is 1, het 2e is 3, het 3e is 5—dus het **i-de** oneven getal is `2 * i - 1` (voor i = 1, 2, 3, …). Tel elk op bij een lopend totaal.

**Controleer je Logica**:
- Eerste 3 oneven: **9**.
- Eerste 5 oneven: **25** (1+3+5+7+9).
- Eerste 10 oneven: **100**.

```python
# Start Code
totaal = 0

for i in range(1, 11):
    # Het i-de oneven getal is (2 * i - 1). Tel het op bij totaal.
    pass

print(f"Som van de eerste 10 oneven getallen: {totaal}")
```

---

## Puzzel 4: De Som van de Tafel van Vermenigvuldiging
**Het Verhaal**: Een 5×5 tafel van vermenigvuldiging heeft rijen 1 tot 5 en kolommen 1 tot 5. De cel in rij `r` en kolom `c` heeft de waarde `r * c`. De eerste rij is dus 1, 2, 3, 4, 5; de tweede 2, 4, 6, 8, 10; enz.

**De Vraag**: Wat is de **som van alle 25 getallen** in deze tafel? Gebruik **twee loops**: een buitenste loop over de rijen (1 tot 5) en een binnenste loop over de kolommen (1 tot 5). Daarbinnen tel je `rij * kolom` op bij een lopend totaal.

**Voorbeeld Test**:
- Voor een 2×2 tafel (rijen 1–2, kolommen 1–2): waarden 1, 2, 2, 4 → som = **9**.

**Hint**: `totaal = 0`, dan `for rij in range(1, 6):` en daarbinnen `for kolom in range(1, 6): totaal += rij * kolom`.

**Controleer je Logica**:
- 2×2 tafel: som = **9**.
- 5×5 tafel: som = **225**.

```python
# Start Code
totaal = 0

for rij in range(1, 6):
    for kolom in range(1, 6):
        # Tel (rij * kolom) op bij totaal
        pass

print(f"Som van 5×5 tafel van vermenigvuldiging: {totaal}")
```

---

## Puzzel 5: De Driehoek van Puntjes
**Het Verhaal**: Puntjes liggen in een driehoek. Rij 1 heeft **1** puntje, rij 2 heeft **2** puntjes, rij 3 heeft **3**, rij 4 heeft **4** en rij 5 heeft **5**.

**De Vraag**: Hoeveel puntjes zijn er **in totaal**? Gebruik **twee loops**: een buitenste loop over de rijen (1 tot 5). Voor elke rij een binnenste loop die `rij` keer draait en elke keer 1 bij een teller optelt (of tel in één keer `rij` bij het totaal op).

**Voorbeeld Test**:
- Als de driehoek maar 3 rijen had: 1 + 2 + 3 = **6** puntjes.

**Hint**: `totaal = 0`. Buiten: `for rij in range(1, 6):`. Binnen: `for punt in range(rij): totaal += 1` (of gewoon `totaal += rij` in de buitenste loop—maar oefen met twee loops).

**Controleer je Logica**:
- Eerste 3 rijen: **6** puntjes.
- Eerste 5 rijen: **15** puntjes (1+2+3+4+5).

```python
# Start Code
totaal = 0

for rij in range(1, 6):
    for punt in range(rij):
        # Tel 1 op voor elk puntje in deze rij
        pass

print(f"Totaal puntjes in driehoek (5 rijen): {totaal}")
```
