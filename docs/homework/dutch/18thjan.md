# Logische Puzzels met Loops

Datum: 18 jan 2026
Onderwerp: Loops

*Drie nieuwsgierige vragen om op te lossen met Python.*

## Puzzel 1: Het Onstuitbare Nummer (Het 3n+1 Mysterie)
**Het Verhaal**: Wiskundigen hebben een magische regel gevonden. Kies **ELK** willekeurig nummer (zoals 10 of 27 of 500).
- Als het nummer **Even** is: Deel het door 2.
- Als het nummer **Oneven** is: Vermenigvuldig met 3 en tel er 1 bij op.
- Herhaal dit!

**Het Mysterie**: Het lijkt erop dat het *altijd* uiteindelijk crasht naar het nummer **1**. Niemand weet waarom!

**De Vraag**: Begin met het nummer **27**. Hoeveel stappen duurt het om bij 1 te komen? (Het is meer dan je denkt!)

**Voorbeeld Test**:
- Input: `6`
- Logica: `6` (even) -> `3` (oneven) -> `10` -> `5` -> `16` -> `8` -> `4` -> `2` -> `1`
- Output: `8 stappen`

**Hint**: Je hebt een loop nodig die doorgaat *zolang* (while) het nummer niet 1 is. Controleer daarbinnen of het even of oneven is en verander het nummer.

**Kleine Syntax Hint**: `nummer % 2 == 0` is `True` als een nummer **Even** is.

```python
# Start code
nummer = 27
stappen = 0

while nummer > 1:
    # Jouw logica hier!
    # Vergeet niet de stappen te tellen
    pass
```

### Controleer je Antwoord
Probeer `nummer` te veranderen in deze waarden en kijk of je het juiste antwoord krijgt:
- **Input: 9** -> Antwoord: **19 stappen**
- **Input: 12** -> Antwoord: **9 stappen**
- **Input: 15** -> Antwoord: **17 stappen**
- **Input: 27** -> Antwoord: **111 stappen** (Het duurt heel lang!)

---

## Puzzel 2: De Magische Stuiver (Exponentiële Groei)
**Het Verhaal**: Een ietwat gemene geest biedt je een deal aan. Je kunt kiezen:
1.  **$1,000,000** (1 Miljoen Dollar) nu meteen.
2.  **Een Magische Stuiver** ($0.01) die elke dag verdubbelt in waarde, 30 dagen lang. (Dag 1: $0.01, Dag 2: $0.02, Dag 3: $0.04...)

**De Vraag**: Welke is meer waard op Dag 30? Schrijf een loop om het te bewijzen.

**Voorbeeld Test**:
- Input: `Dag 5`
- Logica: Dag 1 (`0.01`), Dag 2 (`0.02`), Dag 3 (`0.04`), Dag 4 (`0.08`), Dag 5 (`0.16`)
- Output: `$0.16`

**Hint**: Probeer niet 2^30 uit je hoofd te rekenen! Gebruik een loop om de waarde van de `stuiver` 30 keer te updaten.

**Kleine Syntax Hint**: Om een nummer te verdubbelen, gebruik de regel `stuiver = stuiver * 2`.

```python
# Start code
geld = 0.01

# Loop voor 30 dagen
for dag in range(1, 31):
    # Update 'geld' hier
    pass
```

### Controleer je Antwoord
Probeer de loop te veranderen naar deze dagen:
- **Dag 10**: `$5.12`
- **Dag 20**: `$5,242.88` (Al 5 duizend!)
- **Dag 30**: `$5,368,709.12` (5 Miljoen!)

---

## Puzzel 3: De Kikker in de Put (Logica Valstrik)
**Het Verhaal**: Een kikker valt in een put die **20 meter diep** is.
- Elke **ochtend** springt de kikker **5 meter OMHOOG**.
- Elke **nacht** terwijl hij slaapt, glijdt de kikker **4 meter OMLAAG**.

**De Vraag**: Hoeveel dagen duurt het voordat hij eruit is?

**Voorbeeld Test**:
- Input: `Diepte 10 meter`
- Logica:
  - Dag 1: Klim 0 -> 5. Glij naar 1.
  - Dag 2: Klim 1 -> 6. Glij naar 2. ...
  - Dag 6: Klim 5 -> 10 (ERUIT!)
- Output: `6 Dagen`

**De Valstrik**: Het is NIET 20 dagen!
*Denk na*: Zodra hij de top (20m) bereikt tijdens de dag, glijdt hij die nacht niet meer terug? Nee, hij is eruit!

**Hint**: Wees voorzichtig! Dit dag-voor-dag simuleren is veiliger dan rekenen. Onthoud: hij springt *tijdens de dag*.

**Kleine Syntax Hint**: Gebruik `if diepte >= 20: break` om de loop direct te stoppen wanneer hij ontsnapt.

```python
# Start code
diepte = 0
dagen = 0

while True:
    dagen = dagen + 1
    # 1. Hij springt 5m omhoog
    # 2. Check: Is hij eruit? (>= 20). Zo ja, break!
    # 3. Zo niet, glijdt hij 4m omlaag
    pass
```

### Controleer je Antwoord
Verander de diepte check naar `if diepte >= 50:` enz. om te testen:
- **Diepte 10m** -> Antwoord: **6 dagen**
- **Diepte 20m** -> Antwoord: **16 dagen**
- **Diepte 50m** -> Antwoord: **46 dagen**
- **Diepte 100m** -> Antwoord: **96 dagen**
