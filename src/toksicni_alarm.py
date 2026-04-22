import pandas as pd

df = pd.read_csv('mars_soil_samples.csv', sep=';')

print(f"Učitano uzoraka: {len(df)}")
print("--- OPASNE ZONE ---")

opasni_uzorci = df[(df['pH_Vrijednost'] < 3) | (df['pH_Vrijednost'] > 10)]

print(f"Pronađeno opasnih uzoraka: {len(opasni_uzorci)}")
print(opasni_uzorci.head(5))