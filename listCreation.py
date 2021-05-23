#1 und 2
versandAdresseList = []

artikellagerList = []

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

def printInventoryList():            
    for i in range(len(Inventar)):
        print("Index: " + str(i) + " - " + "Nr: " + str(i+1) + " - " + "Produkt: " + Inventar[i])

#3
itList = []
gesundheitList = []
autoList = []
spielList = []

def productListBasedOrdering():
    for x in Inventar:
        if "(IT)" in x:
            itList.append(x)
        elif "(Spiel)" in x:
            spielList.append(x)
        elif "(Auto)" in x:
            autoList.append(x)
        elif "(Gesundheit)" in x:
            gesundheitList.append(x)

#4
def listPrinting():
    print()
    print("IT Liste: " + str(itList))
    print("Spiel Liste: " + str(spielList))
    print("Auto Liste: " + str(autoList))
    print("Geundheit Liste " + str(gesundheitList))

#5
itList.sort()
gesundheitList.sort()
autoList.sort()
spielList.sort()

#6
def inventoryListInput():
    input("Neues Item für Inventar List...")
    neuProduktName = input(print("Produkt Name: "))
    neuProduktAnzahl = input(print("Anzahl der Produkt: "))
    neuProduktBereich = input(print("Bereich der Produkt: "))
    print("Produkt wird in Invetar Liste hinzugefügt... ")
    print("(" + neuProduktAnzahl + ") "  + neuProduktName + " (" + neuProduktBereich + ")")
    return neuProduktName, neuProduktAnzahl, neuProduktBereich

#7    
def indexListDeletion():
    targetList = input(print("Aus welche Liste möchten Sie etwas entfernen?: "))
    targetProduct = input(print("Index der Produkt Sie entfernen möchten: "))
    
    # if targetList in vars():
    #     vars()[targetList].pop(targetProduct)
    # else:
    #     print("Diese Liste ist nicht gültig")
        
    if targetList == "itList":  
        itList.pop(targetProduct)
    elif targetList == "gesundheitList":
        gesundheitList.pop(targetProduct)
    elif targetList == "autoList":
        autoList.pop(targetProduct)
    elif targetList == "spielList":
        spielList.pop(targetProduct)
    else:
        print("Diese Liste ist nicht gültig")

#8
def spielListClear():
    spielList.clear()

inventoryListInput()





