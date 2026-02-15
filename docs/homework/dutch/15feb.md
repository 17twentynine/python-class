# Logische Puzzel: Eentje voor Vandaag
Datum: 15 feb 2026
Onderwerp: Loops & Voorwaarden

*Eén korte puzzel—iets simpeler dan de speltheorie van volgende week.*

## Puzzel: De Verzamelaar van Even Getallen
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
