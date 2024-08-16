import random

def tas_kagit_makas_ahmet_eren_okur():
    print("Merhaba! Bu bir klasik taş kağıt makas oyunudur.")
    print("Her oyun en fazla 3 turdan oluşur.")
    print("İlk 2 turu kazanan oyunu kazanır.")
    print("Önce siz hamle yaparsınız, sonra bilgisayar.")
    print("Her oyun sonunda iki taraf da devam etmek isterse yeni oyun başlar.")
    print("Oyun sırasında 'exit' yazarak istediğiniz zaman çıkabilirsiniz.")
    print("İyi eğlenceler!")

    secenekler = ["taş", "kağıt", "makas"]
    oyun_sayisi = 0

    while True:
        oyun_sayisi += 1
        print(f"\n{oyun_sayisi}. Oyun başlıyor!")
        
        kullanici_skor = 0
        bilgisayar_skor = 0
        tur = 0

        while kullanici_skor < 2 and bilgisayar_skor < 2 and tur < 3:
            tur += 1
            print(f"\n{tur}. Tur")

            kullanici_secimi = input("Taş, kağıt, makas? (veya çıkmak için 'exit' yazın): ").lower()
            if kullanici_secimi == 'exit':
                print("Oyundan çıkılıyor. Hoşça kalın!")
                return

            while kullanici_secimi not in secenekler:
                kullanici_secimi = input("Geçersiz seçim. Lütfen taş, kağıt veya makas seçin (veya çıkmak için 'exit' yazın): ").lower()
                if kullanici_secimi == 'exit':
                    print("Oyundan çıkılıyor. Hoşça kalın!")
                    return

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayar {bilgisayar_secimi} seçti.")

            if kullanici_secimi == bilgisayar_secimi:
                print("Berabere!")
            elif (kullanici_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (kullanici_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (kullanici_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Bu turu siz kazandınız!")
                kullanici_skor += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar_skor += 1

            print(f"Skor - Siz: {kullanici_skor}, Bilgisayar: {bilgisayar_skor}")

        if kullanici_skor > bilgisayar_skor:
            print(f"\nTebrikler! {oyun_sayisi}. oyunu siz kazandınız!")
        elif bilgisayar_skor > kullanici_skor:
            print(f"\nÜzgünüm, {oyun_sayisi}. oyunu bilgisayar kazandı.")
        else:
            print(f"\n{oyun_sayisi}. oyun berabere bitti!")

        kullanici_devam = input("Tekrar oynamak ister misiniz? (evet/hayır/exit): ").lower()
        if kullanici_devam == 'exit':
            print("Oyundan çıkılıyor. Hoşça kalın!")
            break
        kullanici_devam = kullanici_devam == "evet"
        bilgisayar_devam = random.choice([True, False])

        if kullanici_devam and bilgisayar_devam:
            print("Harika! Yeni bir oyun başlıyor.")
        elif kullanici_devam:
            print("Üzgünüm, bilgisayar artık oynamak istemiyor. Hoşça kalın!")
            break
        elif bilgisayar_devam:
            print("Bilgisayar oynamaya devam etmek istiyordu ama siz istemediniz. Görüşmek üzere!")
            break
        else:
            print("İkiniz de oynamak istemiyorsunuz. Oyun bitti. İyi günler!")
            break

if __name__ == "__main__":
    tas_kagit_makas_ahmet_eren_okur()
