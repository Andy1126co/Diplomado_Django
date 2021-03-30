import random
# adivina un nimero
a = random.randrange(0,10)
while True:
    
    try:
        b = int(input("Adivina el numero: ") )
        if b == a :
            print("adivinaste el numero")
            break
        elif b !=a :
            print("intentalo de nuevo")
            pass
    except:
        pass    
