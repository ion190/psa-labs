# Suppose you toss a dart at a circular target of radius 10 inches. Given that the dart lands in the upper half of the target, find the probability that
# * it lands in the right half of the target 
# * its distance from the centre is less than 5 inches 
# * its distance from the centre is greater than 5 inches 
# * it lands within 5 inches of the point (0, 5)

import random

def generate_points():
    x = random.uniform(-10, 10)
    y = random.uniform(0, 10)
    while pow(x,2)+pow(y,2)>=pow(10,2):
        x = random.uniform(-10, 10)
        y = random.uniform(0, 10)
    return x,y


n=1000000
m=0
q=0
p=0
l=0
for _ in range(n):
    x,y=generate_points()

    if pow(x-0,2)+pow(y-5,2)<=pow(5,2):
        l+=1
    if x>0:
        m+=1
    if pow(x,2)+pow(y,2)<=pow(5,2):
        q+=1
    if pow(x,2)+pow(y,2)>=pow(5,2):
        p += 1

print("a.", m/n)
print("b.", q/n)
print("c.", p/n)
print("d.", l/n)
