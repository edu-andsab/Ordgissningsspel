import random
ords = [
    "apelsiner",
    "bibliotek",
    "blommorna",
    "chokladig",
    "datorerna",
    "elefanter",
    "fantasier",
    "fiskebåtar",
    "flickorna",
    "fotbollen",
    "glassarna",
    "guldfiskar",
    "himmelskt",
    "hundarna",
    "jordgubbe",
    "kanelbull",
    "kattungen",
    "kläderna",
    "kompisarna",
    "krokodiler",
    "lärarinna",
    "matlagning",
    "morgonluft",
    "nycklarna",
    "papegojor",
    "passagerar",
    "planeterna",
    "regnbågar",
    "skolbänkar",
    "skogarna",
    "solsystem",
    "sommarhus",
    "stjärnorna",
    "stranden",
    "telefoner",
    "tandborste",
    "tavlorna",
    "trädgårdar",
    "vintertid",
    "äventyras",
    "överrask"
]




while True:
    användabokstäver = []
    
    totalord = len(ords)
    ran = random.randint(0,totalord-1)
    Valtord = ords[ran]
    rätt = ["*"]*len(Valtord)
    print("Du ska gissa ett ord, bokstav för bokstav, på 9 bokstäver")
    liv = 10
    while liv > 0:
        if "*" not in rätt:
            print("Du vann!")
            break
        
        print(f"Du har {liv} försök kvar!")
        gissning = input("Ange gissning ---> ")
        
        if len(gissning) != 1:
            print("Ogiltig gissning")
            continue
        if not gissning.isalpha():
            print("Ogilitigt tecken")
            continue
        

        elif gissning in Valtord.lower():
            if gissning not in användabokstäver:
                användabokstäver.append(gissning)

                
            for i in range(len(Valtord)):
                if Valtord[i].lower() == gissning:
                    rätt[i] = Valtord[i]
                
       
        else:
           
            if not gissning in användabokstäver:
                användabokstäver.append(gissning)
                liv -= 1
                print("Fel!")
                if liv == 0:
                    print("Du förlorade!")
                    print("Ordet var:",Valtord)
                    break
            else:
                print(f"Använda bokstäver är: {"".join(användabokstäver).upper()}")
                print("".join(rätt).upper())
                continue
        print(f"Använda bokstäver är: {"".join(användabokstäver).upper()}")
        print("".join(rätt).upper())

    försök = input("Vill du försöka igen? j/n ----> ").lower()
    if försök == "j":
        continue
    elif försök == "n":
        break

        
  

            





            
            
            
            
            
            
            
            
            
            
         
         
            
            
            
            
            
            
            
            
            
        
