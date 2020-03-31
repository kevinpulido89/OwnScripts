import random
import math

def estimate_pi(n):
    npc = 0
    npt = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            npc +=1
        npt +=1

    return (4*npc)/npt

print(estimate_pi(10000000))
