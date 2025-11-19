# ÖDEV 3: Okul Sınıf Sistemi
# Tarih: 19/11/2025
# Öğrenci: Bora

class Ogrenci:
    def __init__(self, ad, numara, notlar):
        """
        Öğrenci sınıfının yapıcı metodu
        ad: Öğrencinin adı
        numara: Öğrenci numarası
        notlar: Öğrencinin notları listesi
        """
        self.ad = ad
        self.numara = numara
        self.notlar = notlar

    def not_ekle(self, not_degeri):
        """
        Öğrencinin notlar listesine yeni not ekler
        not_degeri: Eklenecek not
        """
        self.notlar.append(not_degeri)

    def ortalama_hesapla(self):
        """
        Öğrencinin notlarının ortalamasını hesaplar
        Döndürür: Notların ortalaması
        """
        if len(self.notlar) == 0:
            return 0
        return sum(self.notlar) / len(self.notlar)

    def bilgileri_goster(self):
        """
        Öğrencinin tüm bilgilerini ve ortalamasını gösterir
        """
        print(f"Öğrenci: {self.ad}")
        print(f"Numara: {self.numara}")
        print(f"Notlar: {self.notlar}")
        print(f"Ortalama: {self.ortalama_hesapla():.2f}")


class Sinif:
    def __init__(self, sinif_adi):
        """
        Sınıf sınıfının yapıcı metodu
        sinif_adi: Sınıfın adı (örn: "10-A")
        """
        self.sinif_adi = sinif_adi
        self.ogrenciler = []

    def ogrenci_ekle(self, ogrenci):
        """
        Sınıfa yeni öğrenci ekler
        ogrenci: Eklenecek Ogrenci nesnesi
        """
        self.ogrenciler.append(ogrenci)

    def sinif_ortalamasi(self):
        """
        Sınıftaki tüm öğrencilerin not ortalamasını hesaplar
        Döndürür: Sınıf ortalaması
        """
        if len(self.ogrenciler) == 0:
            return 0

        toplam_ortalama = 0
        for ogrenci in self.ogrenciler:
            toplam_ortalama += ogrenci.ortalama_hesapla()

        return toplam_ortalama / len(self.ogrenciler)

    def en_basarili_ogrenci(self):
        """
        En yüksek ortalamaya sahip öğrenciyi bulur
        Döndürür: En başarılı Ogrenci nesnesi
        """
        if len(self.ogrenciler) == 0:
            return None

        en_basarili = self.ogrenciler[0]
        en_yuksek_ortalama = en_basarili.ortalama_hesapla()

        for ogrenci in self.ogrenciler:
            ogrenci_ortalama = ogrenci.ortalama_hesapla()
            if ogrenci_ortalama > en_yuksek_ortalama:
                en_yuksek_ortalama = ogrenci_ortalama
                en_basarili = ogrenci

        return en_basarili


# TEST KODLARI (Bu kısım hazır)

# Sınıf oluştur
sinif = Sinif("10-A")

# Öğrenci 1
ogr1_data = {
    "ad": "Ali Veli",
    "numara": 101,
    "notlar": []
}
ogr1 = Ogrenci(**ogr1_data)
ogr1.not_ekle(85)
ogr1.not_ekle(90)
ogr1.not_ekle(78)
sinif.ogrenci_ekle(ogr1)

# Öğrenci 2
ogr2 = Ogrenci("Ayşe Yılmaz", 102, [])
ogr2.not_ekle(95)
ogr2.not_ekle(88)
ogr2.not_ekle(92)
sinif.ogrenci_ekle(ogr2)

# Öğrenci 3
ogr3 = Ogrenci("Mehmet Kaya", 103, [])
ogr3.not_ekle(70)
ogr3.not_ekle(75)
ogr3.not_ekle(80)
sinif.ogrenci_ekle(ogr3)

# Sonuçları göster
print("=== ÖĞRENCİ BİLGİLERİ ===")
ogr1.bilgileri_goster()
print("----------")
ogr2.bilgileri_goster()
print("----------")
ogr3.bilgileri_goster()
print("----------")

print("\n=== SINIF BİLGİLERİ ===")
print(f"Sınıf: {sinif.sinif_adi}")
print(f"Sınıf Ortalaması: {sinif.sinif_ortalamasi():.2f}")

en_basarili = sinif.en_basarili_ogrenci()
print(f"En Başarılı Öğrenci: {en_basarili.ad} ({en_basarili.ortalama_hesapla():.2f})")