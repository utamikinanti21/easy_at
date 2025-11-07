# Daftar makanan dan kalori per porsi (kcal)
makanan = {
    "nasi putih": 200,
    "ayam goreng": 250,
    "ikan bakar": 300,
    "telur rebus": 80,
    "sayur bayam": 50,
    "tahu goreng": 100,
    "tempe": 150,
    "jus jeruk": 120,
    "roti gandum": 100,
    "oatmeal": 150
}

print("=== Kalkulator Kalori Makanan ===")
print("Daftar makanan yang tersedia:")
for nama, kal in makanan.items():
    print(f"- {nama.title()} ({kal} kalori)")

total_kalori = 0

while True:
    pilihan = input("\nMasukkan nama makanan (atau ketik 'selesai' untuk berhenti): ").lower()
    
    if pilihan == "selesai":
        break
    elif pilihan in makanan:
        porsi = float(input("Berapa porsi? "))
        total_kalori += makanan[pilihan] * porsi
        print(f"{pilihan.title()} ditambahkan ({makanan[pilihan] * porsi} kalori).")
    else:
        print("Makanan tidak ditemukan di daftar.")

print("\n=================================")
print(f"Total kalori yang kamu konsumsi: {total_kalori:.0f} kcal")
print("=================================")

# Saran sederhana
if total_kalori < 1500:
    print("Kalorimu masih cukup rendah, pastikan kebutuhan energi tercukupi.")
elif 1500 <= total_kalori <= 2200:
    print("Asupan kalori kamu sudah ideal hari ini.")
else:
    print("Kalorimu cukup tinggi, perhatikan pola makan seimbang ya!")
