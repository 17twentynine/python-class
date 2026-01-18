# Logische Puzzels: Loops & Logica (Niveau 2)
Datum: 25 jan 2026
Onderwerp: Loops & Modulo

*Drie nieuwe puzzels om je skills te testen.*

## Puzzel 1: De Raket Countdown (Makkelijk)
**Het Verhaal**: SpaceX lanceert een nieuw "Starship". Het publiek wacht vol spanning.
Jij moet het computersysteem bouwen dat aftelt van 10 naar 1, en dan roept "BLAST OFF!".

**De Vraag**: Gebruik een loop om de nummers 10 omlaag naar 1 te printen.
*Let op*: Hij moet stoppen BIJ 1, niet 0.

**Voorbeeld Test**:
- Input: `Start 5`
- Output: `5, 4, 3, 2, 1, BLAST OFF!`

**Hint**: Je kunt `range(10, 0, -1)` gebruiken. De `-1` betekent "tel achteruit".

**Controleer je Logica**:
- Als je `range(10, 0, -1)` gebruikt, print hij dan 0? (Dat zou niet moeten).

```python
# Start Code
import time

print("Initiating Launch Sequence...")

# Loop start hier
for t in range(10, 0, -1):
    # Print 't' (de tijd)
    pass

print("BLAST OFF! 🚀")
```

---

## Puzzel 2: De "Virale" Video (Actuele Gebeurtenis)
**Het Verhaal**: Je hebt een grappige video op Instagram gezet.
- Op Uur 0 heb je **10 views** (kijkers).
- Elk uur **VERDUBBELT** (x3) het aantal views!
- **MAAR**, elk uur haken er **50 mensen** af (ze klikken weg).

**De Vraag**: Hoeveel uur duurt het voordat je "Beroemd" bent (10.000 views bereikt)?

**Voorbeeld Test**:
- Uur 1: (10 * 3) - 50 = ... Wacht, dat is negatief! (Stel minimum is 0).
- *Correctie*: Laten we starten met **100 views**.
- Input: `Start 100` -> Doel `1000`
- Uur 1: (100 * 3) - 50 = 250
- Uur 2: (250 * 3) - 50 = 700
- Uur 3: (700 * 3) - 50 = 2050 (Doel!) -> Antwoord: 3 Uur

**Hint**: Gebruik een `while views < 10000:` loop. Daarbinnen doe je de wiskunde `views = (views * 3) - 50`.

**Controleer je Logica**:
- Input: `Start 25` (Lastig!)
- Uur 1: 25 * 3 - 50 = 25.
- Uur 2: 25.
- Antwoord: **Voor altijd** (Het groeit nooit!). De loop kan voor altijd blijven draaien (Oneindige Loop).
- *Code Tip*: Voeg `if uren > 100: break` toe om je computer te redden!

```python
# Start Code
views = 100
uren = 0

while views < 10000:
    # 1. Tel het uur erbij op
    # 2. Update views (x3 en dan -50)
    # 3. Print de status
    pass
```

---

## Puzzel 3: De Magazijn Robot (Uitdagend)
**Het Verhaal**: Een Amazon robot moet een pakketje naar de overkant van de vloer brengen.
- De vloer is **20 meter** lang.
- De robot rijdt **1 meter** elke seconde.
- **MAAR**: Elke **3e seconde** (3, 6, 9...), moet de robot STOPPEN om op te laden. Hij rijdt dan **0 meter** die seconde.

**De Vraag**: Hoeveel seconden duurt het om 20 meter af te leggen?

**Voorbeeld Test**:
- Afstand: `5 meter`
- Sec 1: Rijden (op 1m)
- Sec 2: Rijden (op 2m)
- Sec 3: **Opladen** (nog steeds op 2m)
- Sec 4: Rijden (op 3m)
- Sec 5: Rijden (op 4m)
- Sec 6: **Opladen** (nog steeds op 4m)
- Sec 7: Rijden (op 5m) -> KLAAR!
- Antwoord: **7 seconden**

**Hint**: Je hebt een loop nodig (die seconden telt). Check daarbinnen met `if tijd % 3 == 0:` of het een oplaad-seconde is.

**Kleine Syntax Hint**: `x % 3 == 0` betekent "x is deelbaar door 3".

```python
# Start Code
afstand = 0
seconden = 0
doel = 20

while afstand < doel:
    seconden = seconden + 1
    
    # Check of het oplaad-tijd is (3, 6, 9...)
    if seconden % 3 == 0:
        print(f"Sec {seconden}: Opladen...")
    else:
        afstand = afstand + 1
        print(f"Sec {seconden}: Is nu op {afstand}m")

print(f"Klaar in {seconden} seconden!")
```
