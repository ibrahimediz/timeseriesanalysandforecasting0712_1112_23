import os
liste = os.listdir("Egzersizler/")
filename = "01_ManipulateDataNote.ipynb"
for item in liste:
    adres = f"Egzersizler/{item}/{filename}"
    if not os.path.exists(adres):
        # try:
        #     print(adres[:-6])
        #     os.remove(adres[:-6])
        # except:
        #     pass
        open(adres,"wb")
