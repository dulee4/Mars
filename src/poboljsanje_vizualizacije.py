import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
ax = sns.heatmap(bathymetry_data, cmap='viridis', cbar_kws={'label': 'Dubina (m)'})
plt.title('Toplinska karta dubine (Bathymetry Heatmap) s mjernim jedinicama')
plt.xlabel('X koordinate')
plt.ylabel('Y koordinate')
plt.savefig('assets/3_toplinska_karta_dubine.png', dpi=300)
plt.close()
