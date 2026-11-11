ord = "Adrenalin"

o = ""
rätt = "_"*len(ord)
while True:
    gissning = input("Gissa ordet!")
    for i in range(len(ord)):
        if ord[i] == gissning[i]:
            ratt[i] = ordet[i].lower()
            print(ratt)
            
            
        
