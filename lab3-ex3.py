# 100 people line up to take their seats in a 100 seat theater. The 1st in line lost her ticket and decided to sit in a random seat. Each remaining theatergoer sits in their assigned seat unless it’s occupied and then sits in a random seat. What’s the probability the last person takes their assigned seat?

import random

n=int(input("Input simulations: "))
m=0

for _ in range(n):
    random_seats = random.sample(range(1, 101), 100)
    seating=[]
    seating.append(random.choice(random_seats))
    for i in range(1,len(random_seats)-1):
        if random_seats[i] in seating:
            seating.append(random.choice(list(set(random_seats)-set(seating))))
        else:
            seating.append(random_seats[i])
    if random_seats[-1] not in seating:
        m+=1

print(m/n)
