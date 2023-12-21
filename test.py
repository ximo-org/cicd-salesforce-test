import random

with open('test.txt', mode='w') as f:
    f.write(str(random.randint(0, 1000000000)))