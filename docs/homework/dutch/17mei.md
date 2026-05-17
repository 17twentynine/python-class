# Logica in de echte wereld: Lijsten & Dictionaries
Datum: 17 mei 2026
Onderwerp: Lijsten en Dictionaries — Praktische Simulaties & Calculators

*Deze week gaan we verder dan pure logische puzzels en passen we Lijsten en Dictionaries toe op scenario's uit de echte wereld. We gaan een verkeerslicht simuleren, een boodschappenrekening berekenen en temperaturen bijhouden. Dit zijn de bouwstenen van echte software.*

---

## Puzzel 1: De Vlucht Planner (Overstappen)
**Het Verhaal**: Je bouwt een reis-app. Je hebt een dictionary met directe vluchten. De keys (sleutels) zijn vertreksteden, en de values (waarden) zijn **lijsten** van steden waar je rechtstreeks naartoe kunt vliegen.

**De Vraag**: Een gebruiker wil vertrekken vanuit **Amsterdam** en precies **TWEE** vluchten nemen (één overstap). Wat zijn alle unieke eindbestemmingen die ze kunnen bereiken?

**Voorbeeld Test**:
- `{"A": ["B", "C"], "B": ["D"], "C": ["D", "E"]}`. Start "A" → Overstap "B" of "C" → Eindbestemming "D", "E".

**Hint**: Je hebt een geneste loop (loop in een loop) nodig. Loop eerst door de steden die je direct vanuit Amsterdam kunt bereiken (dit zijn je overstappen). Loop daarna, voor elke overstap, door de steden die je van *daaruit* kunt bereiken (je eindbestemmingen). Voeg deze toe aan de lijst `mogelijke_bestemmingen` als ze er nog niet in staan.

**Controleer je Logica**:
- Via Londen: New York, Madrid, Parijs
- Via Parijs: Madrid, Rome, Amsterdam
- Via Berlijn: Rome, Warschau
- Uiteindelijke unieke lijst: **['New York', 'Madrid', 'Parijs', 'Rome', 'Amsterdam', 'Warschau']**

```python
# Start Code
vluchten = {
    "Amsterdam": ["Londen", "Parijs", "Berlijn"],
    "Londen":    ["New York", "Madrid", "Parijs"],
    "Parijs":    ["Madrid", "Rome", "Amsterdam"],
    "Berlijn":   ["Rome", "Warschau"],
    "Madrid":    ["Rome"],
    "Rome":      ["Athene"],
    "New York":  ["Toronto"]
}

start_stad = "Amsterdam"
mogelijke_bestemmingen = []

# 1. Loop door de overstap-steden vanuit start_stad
# 2. Voor elke overstap, loop door ZIJN bestemmingen
# 3. Voeg toe aan mogelijke_bestemmingen als het er nog niet in staat
pass

print(f"Vertrekkend vanuit {start_stad} met 1 overstap, kun je bereiken:")
print(mogelijke_bestemmingen)
```


---

## Puzzel 2: Het Boodschappenmandje Totaal (Gemiddeld)
**Het Verhaal**: Je hebt een prijslijst (een dictionary) en een boodschappenmandje (een lijst met items die je wilt kopen). Je moet de totale kosten van alle items in het mandje berekenen.

**De Vraag**: Als je mandje `["Melk", "Brood", "Melk", "Eieren"]` bevat, wat zijn dan de totale kosten op basis van de onderstaande prijzen?

**Voorbeeld Test**:
- Prijzen: `{"A": 1, "B": 2}`, Mandje: `["A", "A", "B"]` → Totaal: **4**.

**Hint**: Loop door de `mandje` lijst. Zoek voor elk `item` de prijs op in de `prijzen` dictionary en tel deze op bij een `totaal` variabele.

**Controleer je Logica**:
- Melk (2.50) + Brood (1.50) + Melk (2.50) + Eieren (3.00) = **9.50**.

```python
# Start Code
prijzen = {
    "Melk":   2.50,
    "Brood":  1.50,
    "Eieren": 3.00,
    "Appel":  0.75
}

mandje = ["Melk", "Brood", "Melk", "Eieren"]
totaal = 0

for item in mandje:
    # Zoek prijs op en tel op bij totaal
    pass

print(f"Totaal kosten mandje: €{totaal:.2f}")
```

---

## Puzzel 3: De Temperatuur Tracker (Gemiddeld)
**Het Verhaal**: Je hebt de hoogste temperatuur van elke dag van de week bijgehouden in een dictionary. Je wilt de **gemiddelde** temperatuur en de **warmste dag** vinden.

**De Vraag**: Wat was de gemiddelde temperatuur voor de week, en welke dag was de warmste?

**Voorbeeld Test**:
- `{"Ma": 20, "Di": 22}` → Gemiddelde: **21**, Warmste: **Di**.

**Hint**: Om het gemiddelde te vinden, tel je alle waarden op en deel je door het aantal. Om de warmste dag te vinden, gebruik je een "hoogste tot nu toe" loop zoals we in eerdere puzzels hebben gedaan.

**Controleer je Logica**:
- Gemiddelde: `(18+20+25+22+19+15+17) / 7` ≈ **19.43**.
- Warmste: **Woensdag** (25).

```python
# Start Code
temps = {
    "Maandag":   18,
    "Dinsdag":   20,
    "Woensdag":  25,
    "Donderdag": 22,
    "Vrijdag":   19,
    "Zaterdag":  15,
    "Zondag":    17
}

totaal_temp = 0
warmste_dag = ""
max_temp = -100 # Begin heel laag

for dag, temp in temps.items():
    # 1. Tel op bij totaal_temp
    # 2. Controleer of dit de warmste dag tot nu toe is
    pass

gemiddelde = totaal_temp / len(temps)
print(f"Gemiddelde temperatuur: {gemiddelde:.2f}")
print(f"De warmste dag was {warmste_dag} met {max_temp} graden.")
```

---

## Puzzel 4: Presentielijst Controle (Gemakkelijk–Gemiddeld)
**Het Verhaal**: Je hebt een lijst met studenten die "Aanwezig" zijn. Je moet controleren of een lijst met "Verwachte" studenten ook daadwerkelijk is gekomen.

**De Vraag**: Print voor elke student in de `verwacht` lijst of ze "Aanwezig" of "Afwezig" zijn.

**Voorbeeld Test**:
- Aanwezig: `["Ali", "Bo"]`, Verwacht: `["Ali", "Bo", "Cal"]` → Cal is **Afwezig**.

**Hint**: Gebruik het `in` trefwoord om te controleren of een naam voorkomt in de `aanwezig` lijst: `if naam in aanwezig:`.

**Controleer je Logica**:
- Alice: **Aanwezig**
- Bob: **Afwezig**
- Charlie: **Aanwezig**
- Dave: **Afwezig**

```python
# Start Code
aanwezig = ["Alice", "Charlie", "Eve", "Frank"]
verwacht = ["Alice", "Bob", "Charlie", "Dave"]

for student in verwacht:
    # Controleer of student in de 'aanwezig' lijst staat
    if student in aanwezig:
        print(f"{student}: Aanwezig")
    else:
        print(f"{student}: Afwezig")
```

---

## Puzzel 5: Het Bankafschrift (Gemiddeld)
**Het Verhaal**: Een bankafschrift is een lijst met transacties. Positieve getallen zijn stortingen (+), en negatieve getallen zijn opnames (-). Je wilt je eindbalans weten en hoeveel van elk type transactie er heeft plaatsgevonden.

**De Vraag**: Beginnend met een saldo van `€100`, wat is de eindbalans na de onderstaande transacties? Hoeveel opnames zijn er gedaan?

**Voorbeeld Test**:
- Start: 100, Transacties: `[20, -10]` → Balans: **110**, Opnames: **1**.

**Hint**: Loop door `transacties`. Tel elke waarde op bij `balans`. Als de waarde kleiner is dan 0, verhoog je een `opname_teller`.

**Controleer je Logica**:
- Balans: 100 + 50 - 20 - 10 + 100 - 40 = **180**.
- Opnames: **3** (-20, -10, -40).

```python
# Start Code
balans = 100
transacties = [50, -20, -10, 100, -40]
opnames = 0

for t in transacties:
    # Update balans en tel opnames
    pass

print(f"Eindbalans: €{balans}")
print(f"Aantal opnames: {opnames}")
```

---

## Puzzel 6: Uitgaven per Categorie (Gemiddeld–Moeilijk)
**Het Verhaal**: Je hebt een lijst met transacties, waarbij elke transactie een dictionary is met een "bedrag" (amount) en een "categorie" (zoals "Eten", "Vervoer", of "Huur"). Je wilt weten hoeveel je in **elke** categorie hebt uitgegeven.

**De Vraag**: Wat is voor de onderstaande transacties het totaal uitgegeven bedrag in de categorie "Eten"? Wat is het totaal voor "Vervoer"?

**Voorbeeld Test**:
- `[{"cat": "A", "amt": 10}, {"cat": "A", "amt": 5}]` → `{"A": 15}`.

**Hint**: Maak een lege dictionary `totalen = {}`. Loop door de `transacties`. Haal voor elke transactie de categorie op. Als de categorie **niet** in `totalen` staat, voeg deze dan toe met het huidige bedrag. Als de categorie **wel** al in `totalen` staat, tel dan het huidige bedrag op bij de bestaande waarde.

**Controleer je Logica**:
- Eten: 20 + 15 = **35**.
- Vervoer: 10 + 25 = **35**.
- Huur: **500**.

```python
# Start Code
transacties = [
    {"categorie": "Eten",    "bedrag": 20},
    {"categorie": "Vervoer", "bedrag": 10},
    {"categorie": "Eten",    "bedrag": 15},
    {"categorie": "Huur",    "bedrag": 500},
    {"categorie": "Vervoer", "bedrag": 25},
]

categorie_totalen = {}

for t in transacties:
    cat = t["categorie"]
    bedrag = t["bedrag"]
    
    # Als categorie niet in categorie_totalen staat, stel deze in op bedrag
    # Anders, tel bedrag op bij bestaande categorie_totalen[cat]
    pass

print(f"Uitgaven per categorie: {categorie_totalen}")
```

