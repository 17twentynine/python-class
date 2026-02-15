# Logische Puzzels: Speltheorie (Uitdagend)
Datum: 22 feb 2026
Onderwerp: Simulatie, Strategie & Toeval

*Drie puzzels geïnspireerd op klassieke speltheorie. Houd staat, uitbetalingen en uitkomsten bij.*

## Puzzel 1: Het Herhaalde Gevangenendilemma
**Het Verhaal**: Twee verdachten worden elke ronde apart verhoord. Elke ronde kan elke speler **Samenwerken (C)** of **Verraden (D)**. De uitbetaling (punten) per ronde is:

|               | Andere: C | Andere: D |
|---------------|-----------|-----------|
| **Jij: C**    | 3, 3      | 0, 5      |
| **Jij: D**    | 5, 0      | 1, 1      |

(Eerste getal = jouw punten, tweede = tegenstander.)

- **Speler A** speelt **Tit-for-Tat**: eerste ronde Samenwerken; daarna elke ronde doe wat de tegenstander vorige ronde deed.
- **Speler B** speelt **Altijd Verraden**: elke ronde Verraden.

**De Vraag**: Simuleer **20 ronden**. Houd het totaalsaldo van elke speler bij. Wat zijn de eind scores van Speler A en Speler B?

**Voorbeeld Test** (eerste 3 ronden):
- Ronde 1: A speelt C, B speelt D → A krijgt 0, B krijgt 5.
- Ronde 2: A (tit-for-tat) kopieert B's vorige zet → A speelt D. B speelt D. → A krijgt 1, B krijgt 1.
- Ronde 3: A kopieert D, B speelt D. → A krijgt 1, B krijgt 1.
- Dus na 3 ronden: A = 2, B = 7.

**Hint**: Je hebt variabelen nodig voor `score_a`, `score_b`, en `last_move_b` (wat B vorige keer deed—B is altijd D, dus na ronde 1 is het altijd "D"). Voor A gebruik je `last_move_b` om A's zet te bepalen. Elke ronde: bepaal A's zet, B's zet is altijd D, tel dan met de tabel de punten op.

**Controleer je Logica**:
- Na 1 ronde: A = 0, B = 5.
- Na 20 ronden: A = 19, B = 24.

```python
# Start Code
score_a = 0
score_b = 0
last_move_b = "C"  # Voor ronde 1 doen we alsof B "samenwerkte" zodat A met C begint

for ronde in range(1, 21):
    # 1. A's zet: Tit-for-Tat = kopieer last_move_b
    move_a = last_move_b
    move_b = "D"  # Altijd Verraden

    # 2. Uitbetaling: (C,C)=3,3  (C,D)=0,5  (D,C)=5,0  (D,D)=1,1
    #    Tel de juiste punten op bij score_a en score_b
    # 3. Update last_move_b voor de volgende ronde (voor Tit-for-Tat)
    pass

print(f"Speler A (Tit-for-Tat): {score_a} punten")
print(f"Speler B (Altijd Verraden): {score_b} punten")
```

---

## Puzzel 2: De Sint-Petersburg Loterij
**Het Verhaal**: Er wordt met een eerlijke munt gegooid. **Kop** bij de 1e worp → je wint **1** punt en stopt. **Munt** → gooi opnieuw; **Kop** bij de 2e worp → je wint **2** punten en stopt. Weer **Munt** → opnieuw gooien; **Kop** bij de 3e worp wint **4** punten, enz. Dus **Kop bij worp n** levert **2^(n-1)** op (1, 2, 4, 8, 16, ...).

**De Vraag**: Simuleer dit spel **1000 keer**. Wat is de **gemiddelde** uitbetaling per spel (totaal winst ÷ 1000)?

**Voorbeeld Test** (één spel):
- Worp 1: Munt. Worp 2: Munt. Worp 3: Kop → uitbetaling = 4. Dit spel levert 4 op.

**Hint**: Gebruik `import random`. In één spel: loop (of while) tot je Kop gooit: `random.random() < 0.5` (Kop). Tel de worpen; uitbetaling = 2**(worpen - 1). Tel uitbetaling op bij een totaal. Na 1000 spellen: gemiddelde = totaal / 1000.

**Controleer je Logica**:
- Het gemiddelde ligt vaak rond 5–15 (het verschilt door toeval). Draai meerdere keren.
- Bij slechts 10 spellen kan het gemiddelde heel anders zijn; 1000 geeft een stabieler getal.

```python
# Start Code
import random

totaal_uitbetaling = 0
aantal_spellen = 1000

for spel in range(aantal_spellen):
    worpen = 0
    # Blijf gooien tot Kop (random.random() < 0.5 betekent Kop)
    # Tel worpen; bij Kop: uitbetaling = 2 ** (worpen - 1)  (1e worp = 1, 2e = 2, 3e = 4)
    # Tel uitbetaling op bij totaal_uitbetaling
    pass

gemiddelde = totaal_uitbetaling / aantal_spellen
print(f"Gemiddelde uitbetaling over {aantal_spellen} spellen: {gemiddelde:.2f}")
```

---

## Puzzel 3: Het Ultimatum Spel
**Het Verhaal**: Elke ronde deelt een **Voorsteller** 100 munten: hij biedt de **Respondent** een bedrag van 0 tot 100 (de rest houdt hij). De Respondent heeft een regel: **accepteren** als het aanbod **≥ 40** is, anders **weigeren**. Bij accepteren krijgt de Voorsteller (100 - aanbod) en de Respondent (aanbod). Bij weigeren krijgen beiden 0.

**De Vraag**: Simuleer **100 ronden**. Elke ronde doet de Voorsteller een **willekeurig** aanbod (een geheel getal van 0 tot 100). Tel hoeveel aanbiedingen worden **geaccepteerd** en wat het **totaal aantal munten** is dat de Respondent ontvangt.

**Voorbeeld Test**:
- Aanbod 35 → Geweigerd. Voorsteller 0, Respondent 0.
- Aanbod 40 → Geaccepteerd. Voorsteller 60, Respondent 40.
- Aanbod 50 → Geaccepteerd. Voorsteller 50, Respondent 50.

**Hint**: Gebruik `random.randint(0, 100)` voor het aanbod. Als `aanbod >= 40`: tel 1 op bij `geaccepteerd_count` en tel `aanbod` op bij `respondent_totaal`. Loop 100 keer.

**Controleer je Logica**:
- Ongeveer de helft van de willekeurige aanbiedingen is onder 40 (0–39) en de helft 40–100, dus je zou ongeveer 60–65 acceptaties uit 100 moeten zien (40–100 zijn 61 getallen).
- Het totaal van de Respondent is de som van alle geaccepteerde aanbiedingen; dat verschilt per run.

```python
# Start Code
import random

geaccepteerd_count = 0
respondent_totaal = 0

for ronde in range(100):
    aanbod = random.randint(0, 100)

    # Als aanbod >= 40: accepteer → tel op en voeg aanbod toe aan respondent_totaal
    # Anders: weiger → niets toevoegen
    pass

print(f"Geaccepteerd: {geaccepteerd_count} van de 100")
print(f"Respondent totaal munten: {respondent_totaal}")
```
