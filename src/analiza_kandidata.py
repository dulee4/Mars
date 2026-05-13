import pandas as pd

def izracunaj_prosjek_kandidata():
    try:
        df = pd.read_csv('data/telemetrija.csv', sep=';')
  
        kandidati = df[(df['ph'] >= 6.5) & (df['ph'] <= 8.5) & (df['metan'] > 0.5)]
        
        if not kandidati.empty:
            prosjek_temp = kandidati['temperatura'].mean()
            print(f"Izračunata prosječna temperatura kandidata: {prosjek_temp:.2f} °C")
            return round(prosjek_temp, 2)
        else:
            print("Nema lokacija koje zadovoljavaju kriterije kandidata.")
            return None
    except Exception as e:
        print(f"Greška pri analizi: {e}")
        return None

if __name__ == "__main__":
    izracunaj_prosjek_kandidata()

