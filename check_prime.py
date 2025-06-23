import math


def is_prime(num):
    end_num = math.ceil(num**0.5 + 1)
    for i in range(2, end_num):
        if num % i == 0:
            return False
    return True


for i in range(2, 1000):
    if is_prime(i):
        print(i, end=", ")
