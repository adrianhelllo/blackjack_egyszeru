import random
KAR_MIN = 2
KAR_MAX = 11
gep_nev = "Gép"
ember_nev = input("Add meg a neved: ")

def huz():
    kartya = random.randint(KAR_MIN, KAR_MAX)
    print(f"A húzott kártya értéke: {kartya}")
    return kartya

def eredmeny(ember_ossz, gep_ossz):
    print(f"\nA jelenlegi állás:\n\n{ember_nev}: {ember_ossz}\n{gep_nev}: {gep_ossz}")

def alap_kioszt(nev):
    print(f"Két kártya kiosztása {nev} felhasználónak")
    osszeg = 0
    for _ in range(2):
        osszeg += huz()
    return osszeg

def megint_huz():
    megint = input("Szeretnél mégegyszer húzni?")
    while megint not in ("igen", "nem"):
        print("Nem értem.")
        megint = input("Szeretnél mégegyszer húzni?")

    if megint == "igen":
        return True
    else:
        print("Rendben.")
        return False

def gep_huz(felh):
    osszeg = 0
    rand = random.randint(0, 1)
    while rand == 1:
        huzott_kartya = huz()
        osszeg += huzott_kartya
        print(f"{gep_nev} {huzott_kartya} kártyát húzta, így kártyáinak összege {felh + osszeg}")
    return osszeg


def main():
    gep = 0
    ember = 0

    gep += alap_kioszt(gep_nev)
    ember += alap_kioszt(ember_nev)

    eredmeny(gep, ember)



    if max(ember, gep) > 20:
        print(f"{min(ember, gep)} nyert")
    else:
        print(f"{max(ember, gep)} nyert")

    gep_huz(gep)



if __name__ == '__main__':
    main()
