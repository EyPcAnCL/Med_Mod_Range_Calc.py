import numpy as np
import pandas as pd

veriler = pd.Series(np.random.randint(1, 100, size=10))

aralik = veriler.max() - veriler.min()

print("=" * 40)
print("📌 RANGE (Açıklık)")
print("=" * 40)
print(f"Verilerimiz     : {veriler.tolist()}")
print(f"En Büyük Değer  : {veriler.max()}")
print(f"En Küçük Değer  : {veriler.min()}")
print(f"Sonuç (Açıklık) : {aralik}")
print("=" * 40)
