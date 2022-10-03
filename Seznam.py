import random

seznam =[]

for i in range(5):
    r = round(random.uniform(1,2000))
    seznam.append(r)
    sou = sum(seznam)
    poc = len(seznam)
    prum = sou/poc

print("List", seznam)
print("Soucet: ", sou)
print("Pocet: ", poc)
print("Prumer: ", prum)



