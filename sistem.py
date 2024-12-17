import json
from statistics import mean

# Öğrenci kayıtlarını tutacak liste
ogrenci_listesi = []
dersler = ["Matematik", "Edebiyat", "Fen Bilgisi", "Coğrafya", "Felsefe"]

def ogrenci_control(numara):
    #  Girilen numaranın listede olup olmadığını kontrol eder.
    return any(ogrenci["numara"] == numara for ogrenci in ogrenci_listesi)

def ders_sec(notlar):
    # Kullanıcıdan ders seçmesini ister, seçilen dersi döner ve tekrar seçim engellenir.
    while True:
        print("\n--- Ders Seçimi ---")
        print("0. Çıkış (Ders girişini tamamla)")
        for i, ders in enumerate(dersler, 1):
            print(f"{i}. {ders}")
        try:
            secim = int(input("Hangi dersin notunu girmek istiyorsunuz? (0-5): "))
            if secim == 0:
                return None  # Kullanıcı dersi tamamlayarak çıkmak istedi
            elif 1 <= secim <= 5:
                ders = dersler[secim - 1]
                if ders not in notlar:
                    return ders
                else:
                    print(f"{ders} için zaten not girildi! Lütfen farklı bir ders seçin.")
            else:
                print("Lütfen 0-5 arasında bir sayı girin!")
        except ValueError:
            print("Geçerli bir sayı girin!")

def ogrenci_ekle():
    # Kullanıcıdan öğrenci bilgilerini alır ve geçerli ise listeye ekler.
    print("\n--- Yeni Öğrenci Kaydı ---")
    
    # Ad ve Soyad isteme ekranı
    ad = input("Öğrencinin Adı: ").strip().capitalize()
    soyad = input("Öğrencinin Soyadı: ").strip().capitalize()
    
    # Numara kontrolü ekranı
    while True:
        try:
            numara = int(input("Öğrenci Numarası (3 haneli): "))
            if 100 <= numara <= 999:
                if ogrenci_control(numara):
                    print("Bu numara zaten kayıtlı! Lütfen farklı bir numara girin.")
                else:
                    break
            else:
                print("Öğrenci numarası 3 haneli olmalıdır!")
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")
    
    # Ders notlarını isteme ekranı
    notlar = {}
    print("\nDerslerin not girişini yapabilirsiniz. En az bir ders girmelisiniz.")
    while True:
        ders = ders_sec(notlar)
        if ders is None:
            if not notlar:
                print("En az bir dersin notunu girmelisiniz!")
                continue
            else:
                break  # Kullanıcı not girişini tamamladı ve sisteme kaydoldu
        while True:
            try:
                ders_notu = float(input(f"{ders} Notu (0-100): "))
                if 0 <= ders_notu <= 100:
                    notlar[ders] = ders_notu
                    break
                else:
                    print("Not 0 ile 100 arasında olmalıdır!")
            except ValueError:
                print("Lütfen geçerli bir sayı girin!")
    
    # Öğrenci bilgisini ekleme ekranı
    yeni_ogrenci = {
        "ad": ad,
        "soyad": soyad,
        "numara": numara,
        "notlar": notlar
    }
    ogrenci_listesi.append(yeni_ogrenci)
    print("\nÖğrenci başarıyla eklendi!")

def ogrenci_listele():
    # Tüm öğrenci bilgilerini okunabilir formatta listeler.
    print("\n--- Kayıtlı Öğrenci Listesi ---")
    if not ogrenci_listesi:
        print("Henüz öğrenci kaydı bulunmuyor!")
    else:
        for ogrenci in ogrenci_listesi:
            print(f"\nİsim: {ogrenci['ad']} {ogrenci['soyad']}, Numara: {ogrenci['numara']}")
            print("--- Notlar ---")
            for ders, notu in ogrenci["notlar"].items():
                print(f"{ders}: {notu}")
            print("---" * 3)

def not_analizi():
    # Sistemde kayıtlı olan öğrencilerin not analizini yapar.
    print("\n--- Sınıf Not Analizi ---")
    if not ogrenci_listesi:
        print("Henüz öğrenci kaydı bulunmuyor!")
        return
    
    tum_notlar = [notu for ogrenci in ogrenci_listesi for notu in ogrenci["notlar"].values()]
    if not tum_notlar:
        print("Sistemde henüz girilmiş bir not bulunmuyor.")
        return
    
    print(f"En Yüksek Not: {max(tum_notlar)}")
    print(f"En Düşük Not: {min(tum_notlar)}")
    print(f"Sınıf Ortalaması: {mean(tum_notlar):.2f}")

def menu():
    # Ana Menü.
    while True:
        print("\n--- Öğrenci Kayıt Sistemi ---")
        print("1. Yeni Öğrenci Ekle")
        print("2. Öğrenci Listesini Görüntüle")
        print("3. Sınıf Not Analizi")
        print("4. Çıkış")
        
        secim = input("Bir seçenek girin (1-4): ").strip()
        
        if secim == "1":
            ogrenci_ekle()
        elif secim == "2":
            ogrenci_listele()
        elif secim == "3":
            not_analizi()
        elif secim == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek! Lütfen 1-4 arasında bir sayı girin.")

# Programı başlat
menu()
