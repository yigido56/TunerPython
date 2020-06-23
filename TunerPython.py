import matplotlib.pyplot as plt    #Gerekli kütüpheneler eklendi.
import numpy as np
from scipy.fftpack import fft,ifft,ifftshift,fftfreq
import sounddevice as sd
from scipy.io import wavfile
import soundfile as sf

class tuner(): #tuner sınıfı oluşturuldu.

    def kayıt(self): #Ses kayıtları için kayıt objesi tuner sınıfı altında oluşturuldu.
        Fs = 48000 # Oluşturulacak kaydın örnekleme frekansı
        d = 6 #Kayıt süresi (sn)
        print("""
        *************AKORD AYARLAMA PROGRAMI***********
        Kaydetmek İstediğiniz Telin Numaraları Şu Şekilde:
        1- E4 Mi Teli
        2- B3 Si Teli
        3- G3 Sol Teli
        4- D3 Re Teli
        5- A2 La Teli
        6- E2 Mi Teli
        """)
        tel = int(input("Tel Numarasını Giriniz:")) #Tel numarasının kullanıcıdan alınmasıyla oluşturulan wav dosya ismi bölümü.
        teln = (str(tel) + ".wav")
        filename = "gitar-akor" + str(teln)

        print("Record Starting")
        a = sd.rec(int(d * Fs), Fs, 1, blocking="True") #Belirlenen örnekleme frekansıyla 1.kanalda kaydedildi ve bir değişkene atandı.
        a = a.flatten()  # Kayıt sonucu oluşan veri, tek boyuta indirgendi.
        print("Record end")
        sd.play(a, Fs) # Oluşturulan kayıt örnekleme frekansına göre oynatıldı.


        output = filename #Veri, çıkış değişkenine atandı.

        sf.write(output, a, Fs) # Veri, çıkış dosyasına yazıldı.

    def kontrol(self): #Elde Edilen verilerin kontrol edilmesi için kontol objesi oluşturuldu.
        def telnumara(x): #Verilen x parametresine göre gitar tellerinin olması gereken frekans aralıklarını ve doğru akord ayarı yapabilmek
        # için yapılması gerekenleri kullanıcıya belirten fonksiyon.
            if x == 1:
                while 327 < frequency < 331:
                    print("Akort doğru ayarlandı")
                    break
                if frequency <= 327:
                    print("Akort burgusunu saat yönü tersine çeviriniz\n")
                    print("Olması gereken frekans aralığı:327-331Hz")

                elif frequency >= 331:
                    print("Akort burgusunu saat yönüne çeviriniz")
                    print("Olması gereken frekans aralığı:327-331Hz")
            elif x == 2:
                while 245 < frequency < 249:
                    print("Akort doğru ayarlandı")
                    break
                if frequency <= 245:
                    print("Akort burgusunu saat yönü tersinde çeviriniz")
                    print("Olması gereken frekans aralığı:245-249Hz")
                elif frequency >= 249:
                    print("Akort burgusunu saat yönünde çeviriniz")
                    print("Olması gereken frekans aralığı:245-249Hz")
            elif x == 3:
                while 194 < frequency < 198:
                    print("Akort doğru ayarlandı")
                    break
                if frequency <= 194:
                    print("Akort burgusunu saat yönüne çeviriniz")
                    print("Olması gereken frekans aralığı:194-198Hz")
                elif frequency >= 198:
                    print("Akort burgusunu saat yönü tersine çeviriniz")
                    print("Olması gereken frekans aralığı:194-198Hz")
            elif x == 4:
                while 144 < frequency < 148:
                    print("Akort doğru ayarlandı")
                    break
                if frequency <= 144:
                    print("Akort burgusunu saat yönü tersine çeviriniz")
                    print("Olması gereken frekans aralığı:144-148Hz")
                elif frequency >= 148:
                    print("Akort burgusunu saat yönüne çeviriniz")
                    print("Olması gereken frekans aralığı:144-148Hz")
            elif x == 5:
                while 108 < frequency < 112:
                    print("Akort doğru ayarlandı")
                    break
                if frequency <= 108:
                    print("Akort başlığını saat yönü tersine çeviriniz")
                    print("Olması gereken frekans aralığı:108-112Hz")
                elif frequency >= 112:
                    print("Akort Başlığını saat yönünde çeviriniz")
                    print("Olması gereken frekans aralığı:108-112Hz")
            elif x == 6:
                while 2*81 < frequency < 2*83:
                    print("Akort doğru ayarlandı")
                    break
                if frequency <= 2*81:
                    print("Akort başlığını saat yönü tersinde çeviriniz")
                    print("Olması gereken frekans aralığı:162-168Hz")
                elif frequency >= 2*83:
                    print("Akort Başlığını saat yönünde çeviriniz")
                    print("Olması gereken frekans aralığı:162-168Hz")
            else:
                print("Yanlış Değer Girdiniz...")

        print("""
        *************AKORT AYARLAMA PROGRAMI***********
        Ayarlamak İstediğiniz Telin Numaraları Şu Şekilde:
        1- E4 Mi Teli
        2- B3 Si Teli
        3- G3 Sol Teli
        4- D3 Re Teli
        5- A2 La Teli
        6- E2 Mi Teli
        """)

        tel = int(input("Tel Numarasını Giriniz:"))  #Kullanıcının girişi ile kayıt dosyası bulundu ve değişkene atandı.
        teln = (str(tel) + ".wav")
        filename = "gitar-akor" + str(teln)

        samplerate, data = wavfile.read(filename) #Kayıt dosyası okundu ve veri ile örnekleme frekansı değişkenleri ayrıştırıldı.
        samples = data.shape[0] # Veride oluşan 2 boyutlu arrayin satır boyutu değişkene atandı.

        datafft = fft(data) # Verinin ayrık fourier dönüşümü alındı.

        fftabs = abs(datafft) #Ayrık fourier dönüşümü alınan verinin genliği alındı.
        freqs = fftfreq(samples, 1 / samplerate) # Ayrık fourier dönüşümünün örnek frekans arrayi bulundu.

        plt.xlim([10, samplerate / 100]) #Grafiğin x ekseni arası limitlendi.
        plt.grid(True)
        plt.xlabel('Frekans (Hz)')
        plt.ylabel('Genlik')
        plt.plot(freqs, fftabs) #X ekseni frekans ve Y ekseni genlik olarak grafik çizdirildi.
        plt.show()
        frequency = freqs[np.argmax(fftabs)] #Maksimum genliğe sahip indeks tespit edildi.Bu indekse karşılık gelen frekans
        # değeri değişkene atandı.

        telnumara(tel) #Girilen tel numarasına göre fonksiyon çağrıldı ve frekans değerinin olması gereken aralıkları belirtildi.

        print('Şuanki frekans değeri: {} Hz'.format(frequency))




while True:
    print("""
    *****************AKORT AYARLAMA PROGRAMI*******************
    Yapmak İstediğiniz İşlemi Seçiniz:

    1.Akort Kayıt
    2.Akort Kontrol
     Çıkmak için q ya basınız.
    """)
    işlem=input(print("İşlem Seçiniz : ")) #Kullanıcının seçeceği işleme göre tuner sınıfından objeler çağrıldı.

    if işlem=="q":
        print("Programdan çıkılıyor...")
        break

    if( işlem == "1"):
        tuner().kayıt()

    elif (işlem == "2"):
        tuner().kontrol()
    else:
        print("Yanlış işlem girdiniz...")
        continue