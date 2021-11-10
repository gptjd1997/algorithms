import random

def ran_array():
    random.seed(1)
    ranNum = []
    for i in range(0,1000000):
        ranNum.append(random.randrange(1,11))
    return ranNum