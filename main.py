
import random

from string import digits
from conf import MODEL


def main():

    pk = 1
    # func start generator for 100
    def start_gen():
        pass

    # import to json


#-------------functions for Fields-------------------------------------------------


    # 3.2 func  random generate fictional year
    def generate_random_year(lenght_= 4) -> int:
        tmp_year = random.sample(digits, lenght_)
        tmp_year_str = "".join(tmp_year)

        return tmp_year_str

    # 3.3 func  random generate pages
    def generate_random_pages(lenght_= 3) -> str:
        tmp_pages = random.sample(digits, lenght_)
        tmp_pages_str = "".join(tmp_pages)

        return tmp_pages_str

    # 3.4 func random generate "isbn13" from Faker
    # def generate_random_pages(lenght_= 3) -> str:
    #     tmp_pages = random.sample(digits, lenght_)
    #     tmp_pages_str = "".join(tmp_pages)
    #
    #     return tmp_pages_str

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

if __name__ == '__main__':
    main()


