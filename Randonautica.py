import random

rand = random.randint(1,10000)
rand2 = random.randint(1,10000)
minusorplus = random.randint(1,6)

inp1 = float(input("==>"))
inp2 = float(input("==>"))
inp3 = float(input("==>"))
inp4 = float(input("==>"))

if minusorplus <= 3:
    print(f"{inp1}.{inp2 + rand}, {inp3}.{inp4 + rand2}")
if minusorplus >= 3:
    print(f"{inp1} {inp2 + rand}, {inp3} {inp4 + rand2}")

