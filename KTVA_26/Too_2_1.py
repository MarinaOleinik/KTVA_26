# 1. Juku
# a) Programm küsib eesnime. Kui nimi on Juku, kuvatakse „Lähme Jukuga kinno!“, muidu teatatakse, et täna kinno ei minda.
# Programm peab Juku ära tundma ka siis, kui nimi on kirjutatud suurtähtedega (JUKU) või väiketähtedega (juku).
# Kui nimi on kirjutatud ainult suurtähtedega, lisa märkus „Ära karju, Juku!“.
# Kasuta: lower(), isupper()
eesnimi=input("Sisesta oma eesnimi: ")
if eesnimi.lower() == "juku":   #"JUKU".lower() => "juku"
    print("Lähme Jukuga kinno!")
    if eesnimi.isupper():
        print("Ära karju, Juku!")
    #b) Kui kinno läheb Juku, küsi tema vanus ja otsusta, millist piletit on vaja osta:
    #Kontrolli enne, kas sisestatud vanus on täisarv. Kui ei ole, kuva veateade.
    vanus = input("Sisesta oma vanus: ")
    if not vanus.isdigit():
        print("Palun sisesta kehtiv vanus täisarvuna.")
    else:
        vanus = int(vanus)
        # alla 6 tasuta
        # 6–14 lastepilet
        # 15–65 täispilet
        # üle 65 sooduspilet                          
        # alla 0 või üle 100 viga andmetes
        if vanus < 0 or vanus > 100:
            print("Viga andmetes: vanus peab olema vahemikus 0–100.")
        elif vanus < 6:
            print("Sulle on kinno sissepääs TASUTA!")
        elif vanus <= 14:
            print("Sulle on vaja osta LASTEPILET.")
        elif vanus <= 65:
            print("Sulle on vaja osta TÄISPILET.")
        else:
            print("Sulle on vaja osta SOODUSPILET.")       
else:
    print("Täna kinno ei minda.")
#2 Pinginaabrid
# Küsi kahe inimese nimed. Kontrolli, kas mõlemad nimed koosnevad ainult tähtedest. Kui jah, teata kasutajale, kas nad on täna pinginaabrid või mitte. Kui mõnes nimes on numbreid või muid märke, kuva veateade.
# Otsusta ise, kuidas „pinginaabrid“ määratakse, näiteks juhuslikult või nimede algustähtede järgi.
# Kasuta: isalpha(), capitalize()
pinginaabrid=["Mati","Kati","Juku"]
eesnimi1=input("Sisesta esimese inimese eesnimi: ")
eesnimi2=input("Sisesta teise inimese eesnimi: ")

if eesnimi1.isalpha() and eesnimi2.isalpha():
    if eesnimi1.capitalize() in pinginaabrid and eesnimi2.capitalize() in pinginaabrid:
        print("Inimesed on täna pinginaabrid.")
    else:
        print("Inimesed ei ole täna pinginaabrid.")
else:
    print("Palun sisesta kehtivad nimed.")

# 3. Remont
# Küsi ristkülikukujulise toa pikkus ja laius ning arvuta põranda pindala.
# Seejärel küsi, kas kasutaja soovib remonti teha. Kui vastus on jaatav, küsi ruutmeetri hind ja arvuta põranda vahetamise hind.
# Lisaküsimus: kas kasutaja teeb remondi ise või kasutab professionaali abi? Professionaali puhul küsi ka töö hind ruutmeetri kohta ja arvuta remondi koguhind koos tööga.
# Kasuta: float(), lower() (vastuse „Jah“, „JAH“, „jah“ äratundmiseks), round()
try:
    pikkus=float(input("Sisesta toa pikkus meetrites: "))
    laius=float(input("Sisesta toa laius meetrites: "))
    pindala=pikkus*laius
    print(f"Põranda pindala on {round(pindala,2)} ruutmeetrit.")  #round() ümardab 2 kohta pärast koma
    soov=input("Kas soovid remonti teha? (jah/ei): ").lower()
    if soov=="jah":
        try:
            rm_hind=float(input("Sisesta ruutmeetri hind: "))
            hind=pindala*rm_hind
            print(f"Põranda vahetamise hind on {round(hind,2)} eurot.")
            abi=input("Kas soovid remonti teha ise või kasutada professionaali abi? (ise/professionaal): ").lower()
            if abi=="professionaal":
                try:
                    töö_hind=float(input("Sisesta töö hind ruutmeetri kohta: "))
                    koguhind=hind+pindala*töö_hind
                    print(f"Remondi koguhind koos tööga on {round(koguhind,2)} eurot.")
                except ValueError:
                    print("Palun sisesta kehtiv ujukomaarv töö hinnaks.")
            elif abi=="ise":
                print("Remonti teed ise.")
            else:
                print("Palun sisesta kas 'ise' või 'professionaal'.")
        except ValueError:
            print("Palun sisesta kehtiv ujukomaarv ruutmeetri hinnaks.")
    else:
        print("Remonti ei tehta.")
except ValueError:
    print("Palun sisesta kehtiv ujukomaarv.")

#4,5,6 õpilane teeb ise

#7. Pikkus ja sugu
# Täienda ülesannet 6: küsi lisaks sugu. Meestele ja naistele kehtivad erinevad piirid. Tingimusplokid võivad olla üksteise sees.
# Sugu võib sisestada mis tahes kujul (M, m, mees, MEES). Programm peab selle ära tundma.
# Kui sugu on sisestatud valesti, kuva veateade.
# Kasuta: pesastatud if-laused, lower()
sugu = input("Sisesta oma sugu (M/N): ").lower()
if sugu == "m" or sugu == "mees":
    print("Sinu sugu on mees.")
    # Siin saad lisada meeste jaoks kehtivad piirid ja tingimused
elif sugu == "n" or sugu == "naine":
    print("Sinu sugu on naine.")
    # Siin saad lisada naiste jaoks kehtivad piirid ja tingimused
else:
    print("Palun sisesta kehtiv sugu (M/N).")
