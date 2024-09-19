import random

numero1 = random.randint(1,6)
numero2 = random.randint(1,6)

print("Alberto ha sacado un " , numero1)
print("Bárbara ha sacado un " , numero2)

if (numero1 > numero2):
    print ("Alberto ha ganado")
elif (numero1 < numero2):
    print ("Bárbara ha gando")
else:
    print ("Han empatado")