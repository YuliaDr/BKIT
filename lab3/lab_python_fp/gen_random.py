from random import randint

def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield randint(begin, end)

# a = gen_random(5, 1, 3)
# for i in a:
#     print(i, end=" ")
