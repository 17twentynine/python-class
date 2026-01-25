# Logische Puzzels: Meester-niveau
Datum: 1 feb 2026
Onderwerp: Optellen, Reeksen & Geneste Loops

*Drie geavanceerde puzzels om je Python-vaardigheden tot het uiterste te drijven.*

## Puzzel 1: De Gulzige Bakker (Accumulatie)
**Het Verhaal**: Een bakker is erg blij. Om het 1-jarig bestaan van zijn winkel te vieren, besluit hij koekjes weg te geven.
- Op **Dag 1** geeft hij **1 koekje** weg.
- Op **Dag 2** geeft hij **2 koekjes** weg.
- Op **Dag 3** geeft hij **3 koekjes** weg.
- Dit gaat zo door voor **30 dagen**.

**De Vraag**: Hoeveel koekjes heeft de bakker in totaal weggegeven aan het einde van Dag 30?

**Voorbeeld Test**:
- Input: `5 dagen`
- Logica: 1 + 2 + 3 + 4 + 5 = 15
- Output: `15 koekjes`

**Hint**: Je hebt een variabele nodig `totaal_koekjes = 0`. In een loop die 30 keer draait, blijf je het `dag` nummer optellen bij je `totaal_koekjes`.

```python
# Start Code
totaal_koekjes = 0

for dag in range(1, 31):
    # Jouw logica hier
    pass

print(f"Totaal aantal koekjes: {totaal_koekjes}")
```

**Controleer je Logica**:
- Als je het controleert voor 10 dagen, moet het antwoord **55** zijn.
- Als je het controleert voor 20 dagen, moet het antwoord **210** zijn.
- Wat is het antwoord voor **30 dagen**?

---

## Puzzel 2: De Fibonacci Konijnen (Reeksen)
**Het Verhaal**: Je hebt een paar legendarische Fibonacci-konijnen.
- In **Maand 1** heb je **1 paar**.
- In **Maand 2** heb je nog steeds **1 paar**.
- Vanaf **Maand 3** is het aantal paren de som van de twee voorgaande maanden!
- (Maand 3 = Maand 1 + Maand 2 = 1 + 1 = 2)
- (Maand 4 = Maand 2 + Maand 3 = 1 + 2 = 3)

**De Vraag**: Hoeveel paren konijnen heb je in **Maand 12**?

**Voorbeeld Reeks**: `1, 1, 2, 3, 5, 8, 13...`

**Hint**: Je hebt twee variabelen nodig om de "vorige maand" en de "maand daarvoor" te onthouden.

```python
# Start Code
a = 1 # Maand 1
b = 1 # Maand 2

# We hebben al 2 maanden, dus loop van 3 tot en met 12
for maand in range(3, 13):
    nieuwe_paren = a + b
    # Nu moet je 'a' en 'b' bijwerken voor de volgende maand!
    # a wordt wat b was
    # b wordt de nieuwe_paren
    pass

print(f"Maand 12: {b} paren")
```

**Controleer je Logica**:
- Maand 5: **5 paren**
- Maand 7: **13 paren**
- Maand 10: **55 paren**

---

## Puzzel 3: De Digitale Klok (Drie Dubbele Loops)
**Het Verhaal**: Je bouwt de software voor een high-tech digitale klok.
Deze moet elke seconde van de dag tellen, van `00:00:00` tot `23:59:59`.

**De Vraag**: Gebruik **drie** loops (de een in de ander) om de tijd te printen in het formaat `HH:MM:SS`.

**Voorbeeld Output**:
```
00:00:00
00:00:01
00:00:02
...
23:59:59
```

**Hint**:
- De buitenste loop is voor de **Uren** (0 tot 23).
- De middelste loop is voor de **Minuten** (0 tot 59).
- De binnenste loop is voor de **Seconden** (0 tot 59).
- Gebruik `f"{u:02}:{m:02}:{s:02}"` om te zorgen dat 7 veranderd in `07`.
- **Super Hint**: Gebruik `print(tijd_string, end="\r")` om telkens op dezelfde regel te printen!

```python
# Start Code
import time

for u in range(24):
    for m in range(60):
        for s in range(60):
            # 1. Maak de tijd-string (HH:MM:SS)
            # 2. Print deze!
            # 3. Optioneel: voeg een kleine 'sleep' toe (tijd.sleep) om het te zien tikken
            # time.sleep(0.01)
            pass

print("Einde van de dag!")
```

**Controleer je Logica**:
- Als je uren verandert naar `range(1)`, zou het 3600 regels moeten printen (60 * 60).
- De allerlaatste regel die geprint wordt moet `23:59:59` zijn.
