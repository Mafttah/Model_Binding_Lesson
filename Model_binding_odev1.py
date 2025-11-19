class Kisi:
    def __init__(self, ad, soyad, yas):
        """
        Kişi sınıfının yapıcı metodu
        ad: Kişinin adı
        soyad: Kişinin soyadı
        yas: Kişinin yaşı
        """
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

    def bilgileri_yazdir(self):
        print(f"Ad: {self.ad}")
        print(f"Soyad: {self.soyad}")
        print(f"Yaş: {self.yas}")


kisi1 = Kisi("Ahmet", "Yılmaz", 25)
kisi1.bilgileri_yazdir()

print("---------")

kisi2 = Kisi("Ayşe", "Kaya", 30)
kisi2.bilgileri_yazdir()

print("---------")

kisi3_data = {
    "ad": "Mehmet",
    "soyad": "Demir",
    "yas": 22
}
kisi3 = Kisi(**kisi3_data)
kisi3.bilgileri_yazdir()


















