


import json      # Biblioteka za rad s JSON formatom (standard za podatke)
import requests  # Biblioteka za slanje HTTP zahtjeva (potrebno instalirati)
import datetime  # Za bilježenje točnog vremena
# --- MODUL 1: PAKIRANJE PODATAKA ---
def kreiraj_tovarni_list(id_palete, tezina, hitno=False):
    """
    Funkcija prima sirove varijable i slaže ih u RJEČNIK (Dictionary).
    """

    # Kreiramo složenu strukturu s ugniježđeni podacima
    paket = {
         "projekt": "Nexus",
    "pošiljatelj": "Vito Dušić",
    "meta": {
        "uzorak_id": 1,
        "lokacija": {
            "lat": 18.478147,
            "lon": 77.396189

    },
    "senzori": {
        "temperatura": -26.7,
        "vlaga": 6.59 ;

        "status": "PRIORITET"

    }
    return paket
# --- MODUL 2: POHRANA (Lokalno) ---
def spremi_lokalno(podaci, naziv_datoteke):
    """
    Sprema rječnik u .json datoteku na disku.
    """
    print(f"--- Arhiviram paletu {podaci['id_artikla']} ---")

    try:
        # 'w' mode otvara datoteku za pisanje
        with open(naziv_datoteke, 'w') as f:
            # indent=4 čini da JSON izgleda lijepo i čitljivo
            json.dump(podaci, f, indent=4)
        print(f"Podaci uspješno zapisani u '{naziv_datoteke}'.")
    except Exception as e:
        print(f"Greška pri spremanju: {e}")
# --- MODUL 3: UPLINK (Slanje mrežom) ---
def posalji_na_server(url, podaci_json):
    """
    Šalje podatke na centralni server koristeći POST metodu.
    """
    print(f"--- Šaljem podatke na: {url} ---")

    try:
        # timeout=5 znači: ako server šuti 5 sekundi, odustani.
        odgovor = requests.post(url, json=podaci_json, timeout=5)

        if odgovor.status_code == 200:
            print("SERVER POTVRDIO: Paket primljen.")
        else:
            print(f"SERVER ODBIO: Greška kod {odgovor.status_code}")

    except Exception as greska:
        print(f"KOMUNIKACIJSKA GREŠKA: {greska}")
# 1. Ulazni podaci (Simulacija senzora)
skenirani_barkod = 900255
tezina_senzora = 12.5
je_hitno = True

# 2. Pakiranje
moj_paket = kreiraj_tovarni_list(skenirani_barkod, tezina_senzora, je_hitno)

# 3. Ispis za kontrolu
print("Generirani paket u memoriji:")
print(moj_paket)

# 4. Arhiviranje
spremi_lokalno(moj_paket, "zadnja_paleta.json")

# 5. Slanje
# URL dobijete od nastavnika na ploči!
server_url = " 1. Ulazni podaci (Simulacija senzora)"
skenirani_barkod = 900255
tezina_senzora = 12.5
je_hitno = True

# 2. Pakiranje
moj_paket = kreiraj_tovarni_list(skenirani_barkod, tezina_senzora, je_hitno)

# 3. Ispis za kontrolu
print("Generirani paket u memoriji:")
print(moj_paket)

# 4. Arhiviranje
spremi_lokalno(moj_paket, "zadnja_paleta.json")

# 5. Slanje
# URL dobijete od nastavnika na ploči!
server_url = "https://webhook.site/0f4473ac-158e-40e3-8e19-36a6af8f9a88"
# posalji_na_server(server_url, moj_paket) # Otkomentiraj za slanje

posalji_na_server(server_url, moj_paket) # Otkomentiraj za slanje
