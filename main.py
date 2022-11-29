import speech_recognition as sr
from funcs import websitesine_gir, ara

r = sr.Recognizer()

print("ok")

while True:
    try:
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=500)

        text = str(r.recognize_google(audio, language="tr"))


        if text == "buraya bak delikanlı":
            print("Bana mı seslendiniz: (Evet/Hayır)")
            with sr.Microphone() as source:
                audio = r.listen(source)
            cevap = str(r.recognize_google(audio, language="tr"))

            if cevap == "Evet":
                print("Tamam. Senin için ne yapmamı istersin?")
                while True:
                    try:
                        with sr.Microphone() as source:
                            audio = r.listen(source)
                        islem = str(r.recognize_google(audio, language="tr"))

                        if islem.endswith(".com aç"):
                            print(islem[:(len(islem)) - 3] + " açılıyor")
                            websitesine_gir(islem[0:(len(islem)) - 3])
                        elif islem == "çık":
                            print("Çıktım")
                            break
                        elif islem.endswith("nedir"):
                            print(islem[:(len(islem)) - 6] + " aratılıyor")
                            ara(islem[0:len(islem)-6])
                    except sr.UnknownValueError:
                        print("wdfsd")

            elif cevap == "Hayır":
                print("Tamam yanlış duymuşum.")
                continue
            else:
                print("Geçerli olmayan cevap girdiniz.")
    except sr.UnknownValueError():
        print("Algılanamadı")
