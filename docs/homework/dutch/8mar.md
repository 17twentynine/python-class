# Logische Puzzels: Lijsten (Meer Oefening)
Datum: 8 mrt 2026
Onderwerp: Lijsten — Indices, Zoeken & Schuivende Vensters

*Nog vijf lijstpuzzels (makkelijk tot moeilijk). Bouw lijsten, vind eerste overeenkomsten, verschillen, unieke waarden en schuivende-venster-sommen.*

---

## Puzzel 1: De Verzamelaar van Kwadraten (Makkelijk)
**Het Verhaal**: Je wilt een lijst van **kwadraten** van de getallen 1 tot en met 8 (1², 2², 3², …). Elk gekwadrateerd getal komt in een lijst.

**De Vraag**: Bouw een `kwadraten`-lijst met een lus. Wat is de lijst? Wat is de **som** van de kwadraten?

**Voorbeeld Test**:
- Getallen 1 tot 4: kwadraten = `[1, 4, 9, 16]`, som = **30**.

**Hint**: `kwadraten = []`, dan lus `for n in range(1, 9):` en `kwadraten.append(n * n)`.

**Controleer je Logica**:
- Lijst kwadraten: `[1, 4, 9, 16, 25, 36, 49, 64]`.
- Som van de kwadraten: **204**.

```python
# Start Code
kwadraten = []

for n in range(1, 9):
    # Voeg n² toe aan kwadraten
    pass

print(f"Kwadraten: {kwadraten}")
print(f"Som: {sum(kwadraten)}")
```

---

## Puzzel 2: De Eerste Geslaagde (Makkelijk–Gemiddeld)
**Het Verhaal**: Een leraar kijkt de examenscores in volgorde na. Ze zoekt de **eerste** score die **≥ 70** is (eerste geslaagde). Ze wil ook weten **op welke positie** (index) die score staat.

Scores: `[55, 62, 48, 71, 59, 88, 73, 65]`

**De Vraag**: Loop door de lijst. Als je de eerste score ≥ 70 vindt, bewaar die en de index, en stop. Print de waarde en de positie (bijv. "Eerste geslaagde op index 3: 71").

**Voorbeeld Test**:
- Scores `[60, 65, 72, 80]`: eerste geslaagde is **72** op index **2**.

**Hint**: Gebruik `for i in range(len(scores)):` zodat je zowel index `i` als waarde `scores[i]` hebt. Als `scores[i] >= 70`, bewaar waarde en index, dan `break`.

**Controleer je Logica**:
- Eerste score ≥ 70: **71** op index **3** (4e positie).

```python
# Start Code
scores = [55, 62, 48, 71, 59, 88, 73, 65]
eerste_geslaagd_waarde = None
eerste_geslaagd_index = None

for i in range(len(scores)):
    # Als scores[i] >= 70, zet eerste_geslaagd_waarde en eerste_geslaagd_index, dan break
    pass

print(f"Eerste geslaagde op index {eerste_geslaagd_index}: {eerste_geslaagd_waarde}")
```

---

## Puzzel 3: Het Dagelijkse Verschil (Gemiddeld)
**Het Verhaal**: Een weerstation noteert elke dag de **temperatuur om 12 uur** voor een week. Je wilt een lijst van **dag-tot-dag veranderingen**: temperatuur vandaag min gisteren.

Temperaturen: `[20, 22, 19, 23, 21, 24, 20]`

**De Vraag**: Bouw een `verschillen`-lijst. Het eerste getal is `temperaturen[1] - temperaturen[0]`, het tweede is `temperaturen[2] - temperaturen[1]`, enz. Hoeveel verschillen zijn er?

**Voorbeeld Test**:
- Temps `[10, 15, 12]` → verschillen = `[5, -3]` (twee verschillen).

**Hint**: `verschillen = []`. Lus met `for i in range(1, len(temperaturen)):` en voeg toe `temperaturen[i] - temperaturen[i - 1]`.

**Controleer je Logica**:
- Verschillen: `[2, -3, 4, -2, 3, -4]` (lengte **6**).

```python
# Start Code
temperaturen = [20, 22, 19, 23, 21, 24, 20]
verschillen = []

for i in range(1, len(temperaturen)):
    # Voeg (vandaag - gisteren) toe aan verschillen
    pass

print(f"Dag-tot-dag verschillen: {verschillen}")
print(f"Aantal verschillen: {len(verschillen)}")
```

---

## Puzzel 4: Geen Duplicaten (Gemiddeld–Moeilijk)
**Het Verhaal**: Je hebt een lijst waar getallen kunnen herhalen. Je wilt een **nieuwe** lijst waar elk getal **alleen de eerste keer** dat het voorkomt staat. De volgorde blijft hetzelfde.

Getallen: `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]`

**De Vraag**: Bouw een `uniek`-lijst. Loop over de originele lijst; voeg een getal alleen aan `uniek` toe als het **nog niet** in `uniek` zit.

**Voorbeeld Test**:
- `[2, 3, 2, 4, 3]` → uniek = `[2, 3, 4]`.

**Hint**: `uniek = []`. Voor elke `x in getallen:` controleer `if x not in uniek:` en dan `uniek.append(x)`.

**Controleer je Logica**:
- Unieke lijst: `[3, 1, 4, 5, 9, 2, 6]` (lengte **7**).

```python
# Start Code
getallen = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
uniek = []

for x in getallen:
    # Als x nog niet in uniek zit, voeg toe
    pass

print(f"Uniek (volgorde behouden): {uniek}")
print(f"Aantal: {len(uniek)}")
```

---

## Puzzel 5: De Som van Drie Opeenvolgende (Uitdagend)
**Het Verhaal**: Je hebt een lijst getallen. Je wilt een nieuwe lijst waar elk item de **som van drie opeenvolgende** getallen is: eerste = nums[0]+nums[1]+nums[2], tweede = nums[1]+nums[2]+nums[3], enz.

Getallen: `[10, 20, 30, 40, 50, 60]`

**De Vraag**: Bouw een `drietal_sommen`-lijst. Gebruik een lus over **indices** zodat je bij `nums[i]`, `nums[i+1]` en `nums[i+2]` kunt. Hoe ver kan `i` gaan? (Stop als er geen drie getallen meer over zijn.)

**Voorbeeld Test**:
- `[5, 10, 15, 20]` → drietal_sommen = `[30, 45]` (5+10+15 en 10+15+20).

**Hint**: Lus `for i in range(len(nums) - 2):`. Daarbinnen: voeg toe `nums[i] + nums[i+1] + nums[i+2]` aan `drietal_sommen`.

**Controleer je Logica**:
- Drietal-sommen: `[60, 90, 120, 150]` (lengte **4**).
- Eerste som = 10+20+30 = **60**, laatste = 40+50+60 = **150**.

```python
# Start Code
nums = [10, 20, 30, 40, 50, 60]
drietal_sommen = []

for i in range(len(nums) - 2):
    # Voeg som van nums[i], nums[i+1], nums[i+2] toe
    pass

print(f"Drietal-sommen: {drietal_sommen}")
print(f"Aantal: {len(drietal_sommen)}")
```
