StringInput = input()
StringInput += "$"
Angka = "0123456789"
SubstringTerpanjang = ""
SubstringSekarang = ""

def CekValid(Substring):
    kemunculan = str()
    if len(Substring) % 2 == 1 or len(Substring) == 0:
        return False

    for karakter in Substring:
        if karakter in kemunculan:
            return False
        kemunculan += (karakter)
    return True

for karakter in StringInput:
    if karakter in Angka:
        SubstringSekarang += karakter
    else:
        if(len(SubstringSekarang) > len(SubstringTerpanjang)):
            SubstringTerpanjang = SubstringSekarang
        elif len(SubstringSekarang) == len(SubstringTerpanjang) and CekValid(SubstringSekarang):
            SubstringTerpanjang = SubstringSekarang

        SubstringSekarang = ""

print(SubstringTerpanjang)
if(CekValid(SubstringTerpanjang) == 1):
    print("Valid")
else:
    print("Tidak Valid")
