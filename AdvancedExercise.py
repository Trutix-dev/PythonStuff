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

lists = {
    "IT": [],
    "Gesundheit": [],
    "Auto": [],
    "Spiel": []
}

def listsPrint():
    Inventar.sort()
    print(Inventar)

def inventoryListInput():
    bereichKontroll = False

    while bereichKontroll == False:
        print("Neues Item für Inventar List...")
        neuProduktName = input(print("Produkt Name: "))
        neuProduktAnzahl = input(print("Anzahl der Produkt: "))
        neuProduktBereich = input(print("Bereich der Produkt: "))
        if(neuProduktBereich in lists):
            bereichKontroll = True
            print("Produkt wird in Invetar Liste hinzugefügt... ")
            print("(" + neuProduktAnzahl + ") "  + neuProduktName + " (" + neuProduktBereich + ")")
        else:
            print("Bereich ist nicht gültig, bitte versuchen Sie nochmal.")
          
    return neuProduktName, neuProduktAnzahl, neuProduktBereich

def automaticInventorySorting():
    neuProduktName, neuProduktAnzahl, neuProduktBereich = inventoryListInput()

    print(neuProduktBereich)

    if neuProduktBereich in lists:
        print("INSERTING INTO LIST: " + neuProduktBereich)
        lists[neuProduktBereich].append(neuProduktName + " (" + neuProduktAnzahl + ")")

    # if neuProduktBereich == "IT":
    #     itList.append("("+str(neuProduktAnzahl)+ ") " + neuProduktName)  
    # elif neuProduktBereich == "Gesundheit":
    #     gesundheitList.append("("+str(neuProduktAnzahl)+ ") " + neuProduktName) 
    # elif neuProduktBereich == "Auto":
    #     autoList.append("("+str(neuProduktAnzahl)+ ") " + neuProduktName) 
    # elif neuProduktBereich == "Spiel":
    #     spielList.append("("+str(neuProduktAnzahl)+ ") " + neuProduktName)

def automaticDuplicateUpdater():

    for listName in lists:
        list = lists[listName]
        ''' Check if given list contains any duplicates, rebuild list'''
        itemsDict = {}
        neuList = []
        for item in list:
            # item looks something like "MacBook Pro 2015 (20)"
            # separate quantity from name
            itemDetails = item.split("(") # ['Macbook Pro 2015 ', '20)']
            itemName = itemDetails[0]
            itemQty = itemDetails[1].replace(')', '')

            if itemName in itemsDict:
                itemsDict[itemName] = itemsDict[itemName] + int(itemQty)
            else:
                itemsDict[itemName] = int(itemQty)
       
        for itemName in itemsDict:
            neuList.append(itemName + " (" + str(itemsDict[itemName]) + ")")
        
        lists[listName] = neuList.sort()

# Running tests. Insert 4 Products in any list. Will take care of inserting in the correct lists (1 by 1), and then remove all the duplicates
while(len(lists["IT"]) < 4):
    automaticInventorySorting()
    print(lists["IT"])

print(lists["IT"])

automaticDuplicateUpdater()

print(lists["IT"])


#GUI
# print("- Klug IT GmbH Inventar Software -")
# print()
# programBeenden = False
# while (programBeenden == False):
    # print("Welche Funktion möchten Sie verwenden?...")
    # print("1 - Artikel im gesamte Inventar hinzufügen") 
    # print("2 - Inventar anzeigen")
    # print("3 - Duplikat Prüfung")
    # print("4 - Programm Beenden")
    # print()
    # auswahl = input(print("Ihre auswahl: "))

    # if auswahl = 1:
    #   programBeenden = True

    #print(Wieder im hauptmenu? (y/n) programBeenden = False

