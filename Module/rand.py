import random
import random as ra

# x = ra.getrandbits(8)
# print(x)

print(ra.randrange(10,100))
print(ra.randint(10,100))

print(ra.choice([2,9,3,8,4,7]))
mylist = ["apple", "banana", "cherry"]
print(ra.choices(mylist, weights=[2, 2, 2.1], k=6))

num = [1,2,3,4,5,6,7,8]
ra.shuffle(num)
print(num)

print(ra.sample(mylist, k=1))
print(ra.random())
print(ra.uniform(20, 60))
print(ra.triangular(20, 60, 30))

