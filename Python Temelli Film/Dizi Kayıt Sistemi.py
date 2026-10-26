# Python
#Python Temelli Film/Dizi Kayıt Sistemi
import csv
from datetime import datetime
import os

DOSYA_ADI = "film_dizi_gunlugum.csv"

if not os.path.exists(DOSYA_ADI):
  with open(DOSYA_ADI, mode="w", newline="", encoding="utf-8-sig") as dosya:
    yazici = csv.writer(dosya, delimiter=";")
    yazici.writerow([
        "Tarih",
        "Yapım Adı",
        "Format",
        "Tür",
        "İzleme Durumu",
        "Konu",
        "Puan (5)",
        "Sevilen Karakterler",
        "Sevilmeyen Karakterler",
        "En Sevilen Sahne",
        "Tavsiye Eder miyim?",
    ])

while True:
  print("\n=========================================")
  print("     FİLM VE DİZİ GÜNLÜĞÜ ANA MENÜSÜ")
  print("=========================================")
  print("1 - Yeni Film / Dizi Ekle")
  print("2 - Kayıtlı Tüm Yapımları Listele")
  print("3 - En Yüksek Puanlıları Listele (4 ve üzeri)")
  print("4 - Çıkış")

  secim = input("\nYapmak istediğiniz işlemi seçin (1-4): ")

  if secim == "1":
    print("\n--- Yeni Kayıt Bilgilerini Girin ---")
    ad = input("Filmin / Dizinin Adı: ")
    format_turu = input("Formatı nedir? (Film / Dizi): ")
    tur = input("Türü (Bilim Kurgu, Dram, Komedi vb.): ")
    durum = input("İzleme Durumu (Bitti / İzleniyor / İzlenecek): ")
    konu = input("Kısaca konusu: ")

    while True:
      try:
        puan = float(
            input("5 üzerinden puanınız (Henüz izlemediyseniz 0 yazın): ")
        )
        if 0 <= puan <= 5:
          break
        else:
          print("Hata: Lütfen 0 ile 5 arasında bir puan girin!")
      except ValueError:
        print("Hata: Lütfen sayısal bir değer girin!")

    sevilen_karakter = input("En sevdiğin karakter(ler): ")
    sevilmeyen_karakter = input("En sevmediğin karakter(ler): ")
    sevilen_an = input("En sevdiğin olay anı / sahne: ")
    tavsiye = input("Arkadaşına tavsiye eder misin? (Evet/Hayır): ")

    bugun = datetime.now().strftime("%d.%m.%Y")

    with open(DOSYA_ADI, mode="a", newline="", encoding="utf-8-sig") as dosya:
      yazici = csv.writer(dosya, delimiter=";")
      yazici.writerow([
          bugun,
          ad,
          format_turu,
          tur,
          durum,
          konu,
          puan,
          sevilen_karakter,
          sevilmeyen_karakter,
          sevilen_an,
          tavsiye,
      ])

    print(f"\nBaşarılı! '{ad}' listenize kaydedildi.")

  elif secim == "2":
    print("\n--- KAYITLI TÜM FİLM VE DİZİLER ---")
    with open(DOSYA_ADI, mode="r", encoding="utf-8-sig") as dosya:
      okuyucu = csv.reader(dosya, delimiter=";")
      baslik = next(okuyucu)  # İlk satır tablo başlığı olduğu için atlıyoruz

      sayac = 0
      for satir in okuyucu:
        sayac += 1
        print(
            f"{sayac}. {satir[1]} ({satir[2]}) | Durum: {satir[4]} | Puan:"
            f" {satir[6]}/5 | Tür: {satir[3]}"
        )

      if sayac == 0:
        print("Henüz hiç kayıt eklenmemiş.")

  elif secim == "3":
    print("\n--- EN YÜKSEK PUANLI YAPIMLAR (4.0 ve Üzeri) ---")
    with open(DOSYA_ADI, mode="r", encoding="utf-8-sig") as dosya:
      okuyucu = csv.reader(dosya, delimiter=";")
      baslik = next(okuyucu)  # Başlık satırını atla

      bulundu = False
      for satir in okuyucu:
        puan_degeri = float(satir[6])  # 6. indeks Puan sütunu
        if puan_degeri >= 4.0:
          print(
              f"★ {satir[1]} ({satir[2]}) - Puan: {satir[6]}/5 | En Sevilen"
              f" Karakter: {satir[7]}"
          )
          bulundu = True

      if not bulundu:
        print("4 ve üzeri puana sahip bir yapım henüz bulunamadı.")

  elif secim == "4":
    print(f"\nProgram kapatılıyor. Tüm tablonuz '{DOSYA_ADI}' dosyasında!")
    break

  else:
    print("\nHatalı seçim! Lütfen menüden 1, 2, 3 veya 4 rakamlarından birini girin.")
