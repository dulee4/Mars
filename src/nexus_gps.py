import pandas as pd

df_kemija = pd.read_csv('mars_soil_samples.csv', sep=';')
print(df_kemija.head())

df_gps = pd.read_csv('mars_sample_locations.csv', sep=';')
print(df_gps.head())

print(f"Broj kemijskih uzoraka: {df_kemija.shape[0]}")
print(f"Broj GPS zapisa: {df_gps.shape[0]}")

print(f"Najsjeverniju točku: {df_gps['GPS_LAT'].max()} ")
print(f"Najjužniju točku: {df_gps['GPS_LAT'].min()} ")

print(f"Najistočniju točku: {df_gps['GPS_LONG'].max()} ")
print(f"Najzapadniju točku: {df_gps['GPS_LONG'].min()} ")

max_lat = df_gps['GPS_LAT'].max()
min_lat = df_gps['GPS_LAT'].min()
max_long = df_gps['GPS_LONG'].max()
min_long = df_gps['GPS_LONG'].min()

povrsina = (max_lat - min_lat) * (max_long - min_long)

print(f"Površina istraživanog pravokutnika (u stupnjevima²): {povrsina}")
