import numpy as np

veriler = np.random.randint(1, 100, size=10)

medyan = np.median(veriler)

print("=" * 40)
print("📌 MEDYAN (Median)")
print("=" * 40)
print(f"Verilerimiz     : {sorted(veriler.tolist())}")
print(f"Sonuç           : {medyan:.2f}")
print("=" * 40)
