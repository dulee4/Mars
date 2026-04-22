import pandas as pd

df = pd.read_csv('mars_soil_samples.csv', sep=';')

print("Podaci učitani.")
print(f"Ukupan broj uzoraka: {df.shape[0]}")

# Filtriraj: Zadrži samo uzorke gdje je Temp_Tla_C veća od -60
df_topli = df[ df['Temp_Tla_C'] > -60 ]

print("\n--- TEMPERATURNI FILTER ---")
print(f"Broj uzoraka nakon filtriranja temperature: {df_topli.shape[0]}")


# Provjera: Ispiši najnižu temperaturu u novom skupu da budeš siguran
print(f"Nova minimalna temperatura: {df_topli['Temp_Tla_C'].min()}")

df_voda = df[df['H2O_Postotak'] > 1.5]

print("\n--- FILTER VODE ---")
print(f"Broj vlažnih uzoraka: {df_voda.shape[0]}")

# Kreiraj DataFrame 'kandidati' koji zadovoljava sva 3 uvjeta
kandidati = df[ (df['Temp_Tla_C'] > -60) &
                (df['H2O_Postotak'] > 1.0) &
                (df['Metan_Senzor'] == 'Pozitivno') ]

print("\n--- KONAČNI KANDIDATI ---")
print(f"Pronađeno savršenih lokacija: {kandidati.shape[0]}")
print(kandidati.head())

kandidati.to_csv('mars_kandidati.csv', sep=';', index=False)
print("\nDatoteka 'mars_kandidati.csv' je uspješno kreirana.")



