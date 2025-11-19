class Urun:
    def __init__(self, ad, fiyat, stok):
        self.ad = ad
        self.fiyat = fiyat
        self.stok = stok

    def toplam_deger(self):
        return self.stok * self.fiyat

    def stok_ekle(self, adet):
        self.stok += adet
        print(f"[{adet} adet eklendi]")

    def stok_cikar(self, adet):
        self.stok -= adet
        print(f"[{adet} adet çıkarıldı]")

    def bilgileri_goster(self):
        print(f"Ürün: {self.ad}")
        print(f"Fiyat: {self.fiyat} TL")
        print(f"Stok: {self.stok} adet")
        print(f"Toplam Değer: {self.toplam_deger()} TL")


urun1_data = {
    "ad": "Laptop",
    "fiyat": 15000,
    "stok": 10
}
urun1 = Urun(**urun1_data)
urun1.bilgileri_goster()

print("==================")

urun1.stok_ekle(10)
urun1.stok_cikar(5)
urun1.bilgileri_goster()

print("==================")

urun2 = Urun("Mouse", 250, 50)
urun2.bilgileri_goster()
urun2.stok_cikar(10)
print("\n[10 adet satıldı]")
urun2.bilgileri_goster()
