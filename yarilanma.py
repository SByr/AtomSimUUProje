proton_sayısı = {
    "hidrojen": 1,
    "helyum": 2,
    "lityum": 3,
    "berilyum": 4,
    "bor": 5,
    "karbon": 6,
    "azot": 7,
    "oksijen": 8,
    "flor": 9,
    "neon": 10,
    "sodyum": 11,
    "magnezyum": 12,
    "alüminyum": 13,
    "silisyum": 14,
    "fosfor": 15,
    "kükürt": 16,
    "klor": 17,
    "argon": 18,
    "potasyum": 19,
    "kalsiyum": 20,
}

yarılanma_ömürleri = {
   "hidrojen-1": 12.32,
    "hidrojen-2": 0.0000000000000114,
    "hidrojen-3": 0.000000000116,
    "helyum-3": 7.004,
    "helyum-4": 0.0000000000099,
    "lityum-5": 0.00000000000000000000037,
    "lityum-6": 3.053,
    "lityum-7": 0.0000000000000106,
    "berilyum-8": 0.0000000000000000082, 
    "berilyum-9": 1.39,
    "berilyum-10": 1.39e+6,
    "bor-10": 0.829,
    "bor-11": 0.0000000000000153,
    "karbon-12": 0.0000000000000129,
    "karbon-13": 0.0000000000987,
    "karbon-14": 0.0000000000000153,
    "azot-14": 3.988,
    "azot-15": 0.000000000000168,
    "oksijen-16": 0.203,
    "oksijen-17": 0.000000000000959,
    "oksijen-18": 0.0000000000000165,
    "flor-18": 1.61,
    "flor-19": 0.000000000000156,
    "neon-20": 20.2,
    "neon-21": 0.0000000000000163,
    "neon-22": 0.0000000000064,
    "sodyum-23": 2.605,
    "sodyum-24": 0.000000000000342,
    "magnezyum-24": 7.646,
    "magnezyum-25": 0.000000000000876,
    "magnezyum-26": 0.0000000000000153,
    "alüminyum-27": 0.0000000000074,
    "alüminyum-28": 0.000000000000341,
    "silisyum-28": 23.8,
    "silisyum-29": 0.00000000000959,
    "silisyum-30": 0.000000000000193,
    "fosfor-30": 1.42,
    "fosfor-31": 0.000000000000135,
    "kükürt-32": 87.3,
    "kükürt-33": 0.000000000000135,
    "kükürt-34": 0.000000000000341,
    "Kükürt-35": 0.00000076,
    "kükürt-36": 0.000000000000135,
    "klor-35": 3.01,
    "klor-36": 0.0000095, 
    "klor-37": 0.00000000000255,
    "argon-36": 35.0,
    "argon-37": 0.00003,
    "argon-38": 0.000000000000012,
    "argon-39": 0.00000085,
    "argon-40": 0.000000000000532,
    "potasyum-39": 1.248,
    "potasyum-40": 1.248,
    "kalsiyum-40": 0.158,
    "kalsiyum-41": 0.000000000031,
    "kalsiyum-42": 0.000000000000199,
    "kalsiyum-43": 0.0000000000162,
    "kalsiyum-44": 0.000000000000011,
    "kalsiyum-45": 0.00000000014,
    "kalsiyum-46": 0.000000000000011,
    "kalsiyum-47": 0.0000039,
    "kalsiyum-48": 0.00000000000006,


}


def elementi_bul(proton):
    for element, atom_numarası in proton_sayısı.items():
        if proton == atom_numarası:
            return element
    return None

def izotopu_bul(nötron, proton):
    _element = elementi_bul(proton)
    for izotop, yarılanma_ömrü in yarılanma_ömürleri.items():
        # izotopu isim ve atom numarasına ayırma kısmı
        elementin_adı, atom_numarası = izotop.split("-")
        atom_numarası = int(atom_numarası)
        if nötron + proton == atom_numarası and elementin_adı == _element:
            return izotop, yarılanma_ömrü
    return None

if __name__ == "__main__":
    # proton sayısı inputu
    proton = int(input("Proton sayısı girin: "))

    # proton sayısından elementi bulma
    element = elementi_bul(proton)

    if element:
        # nötron sayısı inputu
        nötron = int(input("Nötron sayısı girin: "))

        # proton ve nötron sayısına göre izotopu bulma
        izotop = izotopu_bul(nötron, element)

        if izotop:
            elementin_adı, yarılanma_ömrü = izotop
            print(f"Elementin adı {elementin_adı} ve yarılanma ömrü {yarılanma_ömrü} saniye.")
        else:
            print("Verilen element için doğal izotopu yoktur.")
    else:
        print("Proton sayısına uygun bir element bulunamadı.")

maxOrbitalDuzeni = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2)] #devam ediyor ama projenin menzilinde değil
orbitaller = ["1s","2s","2p","3s","3p","4s","3d"]
def orbitalHesapla(p):
    orbitalKapasite = 0
    indeks = 0
    orb = []
    for i in maxOrbitalDuzeni:
        indeks = indeks + 1
        a,b = i
        m = 2*b + 1
        orbitalKapasite += 2*m
        if orbitalKapasite >= p:
            orb.append(orbitaller[indeks-1])
            break
        else:
            orb.append(orbitaller[indeks-1])
            continue
    return orb