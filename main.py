import random
KAR_MIN = 2
KAR_MAX = 11
gep_nev = "Gép"
ember_nev = input("Add meg a neved: ")

def huz(min, max, felh):
    kartya = random.randint(KAR_MIN, KAR_MAX)
    print(f"A húzott kártya értéke: {kartya}")

def eredmeny(felh, nev):
    print(f"{nev} felhasználónak kártyáinak összege: {felh}.")

def alap_kioszt(felh, nev):
    print(f"Két kártya kiosztása {nev} felhasználónak")
    for _ in range(2):
        huz(KAR_MIN, KAR_MAX, felh)
    eredmeny(felh, nev)

def main():
    alap_kioszt(gep, gep_nev)
    alap_kioszt(ember, ember_nev)


if __name__ == '__main__':
    main()
