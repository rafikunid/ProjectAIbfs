import matplotlib.pyplot as plt
import numpy as np

# Konstanta percepatan gravitasi (g)
g = 9.8  # m/s^2

# Array ketinggian dari 10 sampai 90 meter (step 10)
h = np.arange(10, 100, 10)

# Hitung kecepatan menggunakan rumus v = sqrt(2gh)
v = np.sqrt(2 * g * h)

# Plot grafik kecepatan vs ketinggian
plt.plot(h, v, marker='o')
plt.title("Grafik Kecepatan terhadap Ketinggian (Jatuh Bebas)")
plt.xlabel("Ketinggian (m)")
plt.ylabel("Kecepatan (m/s)")
plt.grid(True)
plt.show()