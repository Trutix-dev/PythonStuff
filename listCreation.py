
VersandAdresse = []

Artikellager = []

Inventar = ["MacBook Pro 2015 (IT)",
            "PS5 (Spiel)",
            "Volkswagen Polo (Auto)",
            "Jaguar XF (Auto)",
            "FIFA 2020 (Spiel)",
            "Thermometer (Gesundheit)",
            "Red Dead Redemption (Spiel)",
            "Xbox 360 (Spiel)",
            "Razer Blade (IT)",
            "Microsoft Surface 3 (IT)",
            "Texas Instruments N-Spire (IT)",
            "BioNTech-Pfizer Impfstoff(Gesundheit)"]

for i in range(len(Inventar)):
    print("Index: " + str(i) + " - " + "Nr: " + str(i+1) + " - " + "Produkt: " + Inventar[i])

IT = []
Gesundheit = []
Auto = []
Spiel = []

for x in Inventar:
    if "(IT)" in x:
        IT.append(x)
    elif "(Spiel)" in x:
        Spiel.append(x)
    elif "(Auto)" in x:
        Auto.append(x)
    elif "(Gesundheit)" in x:
        Gesundheit.append(x)

print()
print("IT Liste: " + str(IT))
print("Spiel Liste: " + str(Spiel))
print("Auto Liste: " + str(Auto))
print("Geundheit Liste " + str(Gesundheit))












