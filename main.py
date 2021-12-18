import random

from string import digits
from faker import Faker
from conf import MODEL

INPUT_FILE = "books.txt"

def main():

    pk = 1
    # func start generator for 100
    def start_gen():
        pass

    # import to json


#-------------functions for Fields-------------------------------------------------
    # 3.1 func random read one book from file book.txt
    def read_rows_from_book() -> str:
        with open(INPUT_FILE, "r", encoding="UTF8") as f:
            rows_ = f.readlines()
            rows_ = [x.strip() for x in rows_]
            rows_random = random.choice(rows_)

        return rows_random


    # 3.2 func  random generate fictional year
    def generate_random_year(lenght_= 4) -> int:
        tmp_year = random.sample(digits, lenght_)
        tmp_year_str = "".join(tmp_year)

        return int(tmp_year_str)


    # 3.3 func  random generate pages
    def generate_random_pages(lenght_= 3) -> int:
        tmp_pages = random.sample(digits, lenght_)
        tmp_pages_str = "".join(tmp_pages)

        return int(tmp_pages_str)

    # 3.4 func generate random isbn13
    def gen_isbn13() -> str:
        fake = Faker()
        isbn13_ = fake.isbn13()

        return isbn13_


    # 3.5 func random generate raiting (float)
    def generate_random_rating() -> float:
        #tmp_taring = random.randint(0, 5) + random.random()
        tmp_rating = round(random.uniform(0, 5), 7)

        return tmp_rating

    # 3.6 func random generate price(float)
    def generate_random_price() -> float:
        #tmp_taring = random.randint(0, 5) + random.random()
        tmp_price = round(random.uniform(100, 2000), 2)

        return tmp_price


    # 3.7 func random generate from 1 to 3 authors
    def gen_random_author() -> list:
        name_author = []
        count_ = random.randint(1, 3)
        for i in range(count_):
            fake = Faker()
            name_author.append(fake.name())

        return name_author


if __name__ == '__main__':
    main()


