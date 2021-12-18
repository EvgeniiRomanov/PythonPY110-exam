import random
from faker import Faker


def gen_random_author() -> list:
    name_author = []
    count_ = random.randint(1, 3)
    for i in range(count_):
       fake = Faker()
       name_author.append(fake.name())

    return name_author

# rand_ = random.randint(1,3)
# print(rand_)
#k = gen_author()
#print(k, type(k))
k = gen_random_author()
print(k, type(k))