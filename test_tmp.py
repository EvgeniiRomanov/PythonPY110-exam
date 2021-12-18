from string import digits, ascii_letters
import random
from itertools import count
#from traceback import print_exc

# def password_min_8symbols(lenght_ = 8):
#
#     #while True:
#     #for _ in count(1):
#     tmp_pwd = random.sample(digits+ascii_letters, lenght_)
#     random.shuffle(tmp_pwd)
#
#     return "".join(tmp_pwd)
#
# print(password_min_8symbols())

from string import digits, ascii_letters
import random
from itertools import count


# 3.6 func random generate price(float)
def generate_random_rating() -> float:
    # tmp_taring = random.randint(0, 5) + random.random()
    tmp_rating = round(random.random(0, 5), 7)

    return tmp_rating

k = generate_random_rating()
print(k, type(k))