import json      # Biblioteka za rad s JSON formatom (standard za podatke)
import requests  # Biblioteka za slanje HTTP zahtjeva (potrebno instalirati)
import datetime  # Za bilježenje točnog vremena
# --- MODUL 1: PAKIRANJE PODATAKA ---

df_gps = pd.read_csv ('mars_samples_locations.csv', sep = ';'
df_kandidati = pd.read_csv ('mars_kandidati.csv', sep = ';'
def kreiraj_podatke(trazena_lokacija, podatci):

    """
    Funkcija prima sirove varijable i slaže ih u RJEČNIK (Dictionary).
    """

    # Kreiramo složenu strukturu s ugniježđeni podacima
    paket = {
         "projekt": "Nexus",
    "pošiljatelj": "Vito Dušić",
    "meta": {
        "uzorak_id":  trazena_lokacija ['ID_uzorka'],
        "lokacija": {
            "lat": trazena_lokacija ['GPS_LAT'],
            "lon": trazena_lokacija ['GPS_LONG']
        }
    },

    "senzori": {
        "Dubina_Busenja_cm": podatci ['Dubina_Busenja_cm'],
        "Temperatura_Tla": podatci ['Temperatura_Tla'],
        "H2O_postotak": podatci ['H2O_postotak'],
        "Metan_Senzor": podatci ['Metan_Senzor'],
        "Orgenske_Molekule": podatci ['Organske_Molekule']


        "status": "PRIORITET"


    return paket


    def spremi_lokalno(podatci, naziv_datoteke):
    """
    Sprema rječnik u .json datoteku na disku.
    """


    try:
        # 'w' mode otvara datoteku za pisanje
        with open(naziv_datoteke, 'w') as f:
            # indent=4 čini da JSON izgleda lijepo i čitljivo
            json.dump(podaci, f, indent=4)
        print(f"Podaci uspješno zapisani u '{naziv_datoteke}'.")
    except Exception as e:
        print(f"Greška pri spremanju: {e}")

    trazena_lokacija = df_gps[ df_gps['ID'] == 1 ]

    # 1. Ulazni podaci (Simulacija senzora)
trazena_lokacija = df_gps[ df_gps['ID_Uzorak'] == 1]
podatci = df_kandidati[df_kandidati['ID_Uzorak'] == 1]



# 2. Pakiranje
moj_paket = kreiraj_podatke(trazena_lokacija, podatci)

# 3. Ispis za kontrolu
print("Generirani paket u memoriji:")
print(moj_paket)

# 4. Arhiviranje
spremi_lokalno(moj_paket, "zadnja_paleta.json")

# 5. Slanje
# URL dobijete od nastavnika na ploči!
server_url = "https://webhook.site/0f4473ac-158e-40e3-8e19-36a6af8f9a88"


posalji_na_server(server_url, moj_paket) # Otkomentiraj za slanje








