import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('mars_data.csv' , sep=';' , decimal= ',')
df = pd.read_csv('mars_data.csv' , sep=';' , decimal= ',')
sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.histplot(data=df_mars, x='Detekcija_Metana_ppm', kde=True, color='teal')

plt.title('Distribucija koncentracije metana (ppm)')
plt.xlabel('Koncentracija metana (ppm)')
plt.ylabel('Frekvencija / Gustoća')

plt.savefig('graf_3_distribucija_metana.png')
plt.show()

df_mars['zona'] = df_mars ['GPS_Lat'].astype(int)

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_mars, x='zona', y='Temperatura_C', palette='Set2')

plt.title('Usporedba stabilnosti temperature po zonama')
plt.xlabel('Zona')
plt.ylabel('Temperatura (°C)')

plt.savefig('graf_4_usporedba_zona.png')
plt.show()