import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json

df_lokacije = pd.read_csv('mars_lokacije.csv', sep=';', decimal=',')
df_uzorci = pd.read_csv('mars_uzorci.csv', sep=';', decimal=',')

df = pd.merge(df_lokacije, df_uzorci, on='id')

uvjet_anomalije = (df['temp'] < -150) | (df['temp'] > 50) | (df['vlaga'] < 0)

df_anomalije = df[uvjet_anomalije]

df_cisto = df[~uvjet_anomalije]

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_cisto, x='temp', y='vlaga', hue='metan')
plt.title('Odnos temperature i vlage')
plt.savefig('graph1_temp_h2o.png')
plt.close()

# GRAPH 2: Heatmap dubine 
plt.figure(figsize=(10, 6))
# Koristimo 'dubina' umjesto 'Dubina'
sns.scatterplot(data=df_cisto, x='lon', y='lat', hue='dubina', palette='viridis', size='dubina')
plt.title('Karta dubine bušenja')
plt.savefig('graph2_heatmap_depth.png')
plt.close()

# GRAPH 3: Metan
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_cisto, x='lon', y='lat', hue='metan', palette={True: 'red', False: 'blue'})
plt.title('Prisutnost metana')
plt.savefig('graph3_methane_scatter.png')
plt.close()

# GRAPH 4: Kandidati 
kandidati = df_cisto[(df_cisto['metan'] == True)]
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_cisto, x='lon', y='lat', hue='vlaga', alpha=0.5)

if not kandidati.empty:
    plt.scatter(kandidati['lon'], kandidati['lat'], marker='*', s=250, color='red', label='Kandidati')
    plt.legend()

plt.title('Kandidati za bušenje')
plt.savefig('scatter_plot.png')
plt.close()

# --- PETI GRAF: JEZERO MISSION MAP ---
plt.figure(figsize=(12, 8))


extent_koordinate = [
    df_cisto['lon'].min(), df_cisto['lon'].max(),
    df_cisto['lat'].min(), df_cisto['lat'].max()
]


try:
    slika_kratera = plt.imread('jezero_crater_satellite_map.jpg')


    plt.imshow(slika_kratera, extent=extent_koordinate, aspect='auto', alpha=0.7)


    sns.scatterplot(data=df_cisto, x='lon', y='lat', alpha=0.4, color='white', label='Sva očitanja')


    if not kandidati.empty:
        plt.scatter(kandidati['lon'], kandidati['lat'], marker='*', s=200, color='red', label='Kandidati')

    plt.title('Satelitska navigacijska karta - Krater Jezero')
    plt.legend()
    plt.savefig('jezero_mission_map.jpg')
    print("Peti graf uspješno spremljen!")

except FileNotFoundError:
    print("Greška: Datoteka 'jezero_crater_satellite_map.png' nije pronađena!")

plt.close()

{
  "uplink_id": "JEZERO_NAV_2026",
  "navigation_commands": [
    {
      "step": 1,
      "coords": {"lat": 18.452, "lon": 77.456},
      "action": "move_to_poi"
    },
    {
      "step": 2,
      "coords": {"lat": 18.455, "lon": 77.460},
      "action": "soil_sampling"
    }
  ]
}
