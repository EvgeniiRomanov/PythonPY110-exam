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


def generate_random_pages(lenght_=3) -> str:
    tmp_pages = random.sample(digits, lenght_)
    tmp_pages_str = "".join(tmp_pages)

    return int(tmp_pages_str)

k = generate_random_pages()
print(k, type(k))