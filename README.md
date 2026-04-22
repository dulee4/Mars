# Analiza kratera Jezero: Sustav za automatiziranu navigaciju

## A. Izvršni sažetak (Executive Summary)
Ovaj projekt obuhvaća kompleksnu analizu geoprostornih i senzorskih podataka prikupljenih iz kratera Jezero na Marsu. Svrha misije je obrada sirovih telemetrijskih podataka kako bi se identificirale ključne geološke i kemijske karakteristike terena. Konačni cilj sustava je generiranje automatiziranog navigacijskog naloga koji omogućuje terenskom robotu sigurno kretanje i ciljano prikupljanje uzoraka na temelju obrađenih informacija.

## B. Metodologija obrade podataka (Data Wrangling)
U fazi pripreme podataka, primijenjen je niz algoritamskih koraka unutar Python biblioteke Pandas kako bi se osigurao integritet modela:
*   **Filtriranje šuma:** Identificirane su i uklonjene anomalije u senzorskim očitavanjima (npr. pH vrijednosti izvan teoretskog raspona i ekstremni temperaturni skokovi uzrokovani smetnjama u prijenosu).
*   **Logički uvjeti:** DataFrame objekti su strukturirani tako da izdvajaju samo relevantne "zone interesa" (AOI), koristeći uvjetno filtriranje za eliminaciju nepotpunih redaka.
*   **Normalizacija:** Svi podaci su standardizirani kako bi se omogućilo precizno relacijsko spajanje različitih izvora podataka.

## C. Geoprostorna analiza i vizualizacija
Analitički model temelji se na vizualnom dokazivanju hipoteza putem generiranih grafova.

### 1. Korelacija parametara i toplinske karte
Senzorska očitavanja metana i temperature korelirana su kako bi se utvrdile potencijalne zone biosignatura.

![Korelacija parametara](assets/korelacija_parametara.png)
*Interpretacija: Graf prikazuje snažnu korelaciju između povišene vlažnosti tla i lokaliziranih džepova metana.*

### 2. Satelitska mapa i Extent mapiranje
Završna vizualizacija koristi tehniku **extent mapiranja** za definiranje točnih granica istraživačkog područja.

![Satelitska mapa](assets/mapa_kratera.png)
*Interpretacija: Kontekstualno pozicioniranje raspršenih podataka na GPS koordinate omogućuje robotu preciznu orijentaciju unutar zadanog pravokutnika (extent) terena.*

## D. Komunikacijski protokol (JSON Uplink)
Za prijenos naredbi robotu koristi se strukturirani JSON mrežni paket. Sustav koristi petlje (`for` loops) za automatizirano generiranje nizova naredbi, čime se izbjegava statično kodiranje (hardcoding) i omogućuje skalabilnost.

**Primjer ugniježđenog JSON niza:**
```json
{
  "mission_id": "JEZERO_2024",
  "navigation_commands": [
    {
      "step": 1,
      "coordinate": [18.452, 77.456],
      "action": "soil_sampling"
    },
    {
      "step": 2,
      "coordinate": [18.455, 77.460],
      "action": "move_forward"
    }
  ]
}
```

## E. Inženjerski dnevnik (Troubleshooting Log)
Tijekom razvoja sustava riješene su sljedeće tehničke prepreke:

1.  **Problem sa separatorom:** Inicijalno učitavanje podataka nije uspijevalo zbog pogrešnog prepoznavanja separatora u CSV datoteci (korišten je `;` umjesto `,`). 
    *   *Rješenje:* Parametar u `read_csv` funkciji je eksplicitno definiran na ispravan separator.
2.  **Greška u tipovima podataka:** Skripta se rušila prilikom izračuna prosječne temperature jer su određene ćelije sadržavale tekstualni niz umjesto broja.
    *   *Rješenje:* Primijenjena je metoda `to_numeric` s opcijom `errors='coerce'` kako bi se neispravni unosi pretvorili u NaN i potom interpolirali.

---
*Dokument izradio: [Tvoje Ime]*
