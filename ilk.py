import os
import shutil
liste = os.listdir("Egzersizler/")
filename = "01_EgzersizManipulate.ipynb"
for item in liste:
    adres = f"Egzersizler/{item}/{filename}"
    target = f"Egzersizler/SoruCevap/{filename}"

    if not os.path.exists(adres):
        shutil.copy(target,adres)
    #     # try:
    #     #     print(adres[:-6])
    #     #     os.remove(adres[:-6])
    #     # except:
    #     #     pass
    #     open(adres,"wb")



