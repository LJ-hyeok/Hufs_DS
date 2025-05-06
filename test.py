import random
def hash_mod(k, m = 1000):
    return k % m
def hash_universal(k, a = 31, p = 1000):
    h = 0
    h = ((h*a) + k) % p
    return h % 1000

# 1. key % m
key_mod = [-1] * 1000
collisions_mod = 0
for i in range(1000):
    r = random.randint(0, 100000)
    hashed = hash_mod(r)
    if(key_mod[hashed] != -1):
        collisions_mod += 1
    key_mod[hashed] = hashed

# 2. universal
key_univ = [-1] * 1000
collisions_univ = 0
for i in range(1000):
    r = random.randint(0, 100000)
    hashed = hash_universal(r)
    if(key_univ[hashed] != -1):
        collisions_univ += 1
    key_univ[hashed] = hashed


print(collisions_univ, collisions_mod)