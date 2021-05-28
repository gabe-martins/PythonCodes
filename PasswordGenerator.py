import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
special = "[]{}()*;/.,_-"

all = lower + upper + number + special

length = 16
passowrd = "".join(random.sample(all,length))
print(passowrd)