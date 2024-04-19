import random

members = ["john", "marry","mosh","Tala"]
leader = random.choice(members)
print(leader)
for i in range(3):
    print(random.random())
    print(random.randint(5,20))