# Logische Puzzels: Drie voor Vandaag
Datum: 15 feb 2026
Onderwerp: Loops & Voorwaarden

*Drie korte puzzels—iets simpeler dan de speltheorie van volgende week.*

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
