# Python'da Koleksiyonlar: Verilerinizi Düzenlemenin Gücü
# This example demonstrates Python's fundamental collection types: Lists, Tuples, Sets, and Dictionaries.

print("--- Python Koleksiyonları Örneği ---")
print("Verilerinizi düzenlemenin gücünü keşfedin.\n")

# 1. Listeler (Lists): Sıralı, değiştirilebilir (mutable) koleksiyonlar.
# Alışveriş listesi gibi öğelerin sırasının önemli olduğu ve ekleme/çıkarma yapılabilen durumlar için idealdir.
print("1. Listeler (Lists):")
alisveris_listesi = ["Elma", "Ekmek", "Süt", "Yumurta"]
print(f"Başlangıç listesi: {alisveris_listesi}")

alisveris_listesi.append("Peynir") # Listeye yeni öğe ekleme
print(f"Peynir eklendi: {alisveris_listesi}")

alisveris_listesi.remove("Ekmek") # Listeden öğe çıkarma
print(f"Ekmek çıkarıldı: {alisveris_listesi}")

print(f"Listenin ilk öğesi: {alisveris_listesi[0]}\n") # Öğeye indeks ile erişim

# 2. Demetler (Tuples): Sıralı, değiştirilemez (immutable) koleksiyonlar.
# Sabit veri setleri (örn. koordinatlar, bir öğrencinin değişmez bilgileri) için kullanılır.
print("2. Demetler (Tuples):")
ogrenci_bilgisi = ("Ahmet Yılmaz", 101, "Bilgisayar Mühendisliği")
print(f"Öğrenci bilgisi: {ogrenci_bilgisi}")

# ogrenci_bilgisi[0] = "Mehmet Yılmaz" # Hata verir: 'tuple' object does not support item assignment
print(f"Öğrencinin adı: {ogrenci_bilgisi[0]}")
print(f"Öğrenci numarası: {ogrenci_bilgisi[1]}\n")

# 3. Kümeler (Sets): Sırasız, benzersiz öğeler içeren koleksiyonlar.
# Tekrarlayan öğeleri otomatik olarak kaldırır. Üyelik testi ve küme işlemleri için idealdir.
print("3. Kümeler (Sets):")
favori_dersler = {"Matematik", "Fizik", "Kimya", "Matematik"} # "Matematik" tekrar etse de sadece bir kez saklanır
print(f"Favori dersler: {favori_dersler}")

favori_dersler.add("Biyoloji") # Kümeye yeni öğe ekleme
print(f"Biyoloji eklendi: {favori_dersler}")

favori_dersler.discard("Kimya") # Kümeden öğe çıkarma
print(f"Kimya çıkarıldı: {favori_dersler}")

print(f"Fizik dersi favorilerde mi? {'Fizik' in favori_dersler}\n") # Üyelik testi

# 4. Sözlükler (Dictionaries): Anahtar-değer çiftleri (key-value pairs) içeren koleksiyonlar.
# Telefon rehberi, öğrenci notları gibi verileri anahtarlar aracılığıyla hızlıca erişmek için kullanılır.
print("4. Sözlükler (Dictionaries):")
ogrenci_notlari = {
    "Ali": 85,
    "Ayşe": 92,
    "Can": 78
}
print(f"Öğrenci notları: {ogrenci_notlari}")

ogrenci_notlari["Deniz"] = 95 # Yeni öğrenci ve not ekleme
print(f"Deniz'in notu eklendi: {ogrenci_notlari}")

ogrenci_notlari["Ali"] = 88 # Mevcut öğrencinin notunu güncelleme
print(f"Ali'nin notu güncellendi: {ogrenci_notlari}")

print(f"Ayşe'nin notu: {ogrenci_notlari['Ayşe']}") # Anahtar ile değere erişim

print("\n--- Koleksiyonlar ile Veri Yönetimi Tamamlandı ---")
