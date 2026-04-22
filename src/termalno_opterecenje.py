import pandas as pd
import requests

flota_robota = pd.DataFrame({
    'id_robota': [101, 102, 103],
    'sektor': ['Zavarivanje', 'Bojanje', 'Sastavljanje'],
    'model': ['RX-500', 'RX-500', 'TX-200']
})

senzori_temp = pd.DataFrame({
    'id_robota': [101, 102, 103],
    'temperatura_c': [45, 88, 42]
})


izvjestaj = pd.merge(flota_robota, senzori_temp, on='id_robota')

pregrijani_robot = izvjestaj[izvjestaj['temperatura_c'] > 80]

if not pregrijani_robot.empty:
    sektor_kvara = pregrijani_robot.iloc[0]['sektor']
    temperatura = pregrijani_robot.iloc[0]['temperatura_c']

    alarm_podaci = {
        "Autor": "Vito Dušić",
        "Hitnost": "Visoka",
        "Sektor kvara": sektor_kvara,
        "Zabiljezena temperatura": int(temperatura)
    }

    URL_SERVERA = 'https://webhook.site/e2ee3d3c-17a9-4e72-9356-1dd5a4406f13' 
    
    try:
        response = requests.post(URL_SERVERA, json=alarm_podaci)
        
        print(f"Pronađen kvar u sektoru: {sektor_kvara}")
        print(f"Statusni kod servera: {response.status_code}")
        
        if response.status_code == 200:
            print("Alarm je uspješno zaprimljen!")
    except Exception as e:
        print(f"Greška pri slanju: {e}")
else:
    print("Nema zabilježenih pregrijavanja.")