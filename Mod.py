import pandas as pd
import numpy as np
from scipy import stats

# Mod için aralığı daraltıyoruz ki tekrar eden sayı çıksın
veriler = pd.Series(np.random.randint(1, 20, size=15))

mod = stats.mode(veriler, keepdims=True)

print("=" * 40)
print("📌 MOD (Mode)")
print("=" * 40)
print(f"Verilerimiz     : {veriler.tolist()}")
print(f"Mod Değeri      : {mod.mode[0]}")
print(f"Kaç kez tekrar  : {mod.count[0]} kez")
print("=" * 40)
