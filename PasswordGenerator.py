import random
import string

length = 16

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
special = string.punctuation

all = lower + upper + number + special

passowrd = "".join(random.sample(all,length))
print(passowrd)