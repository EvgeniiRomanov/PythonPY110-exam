import random
import json

from string import digits
from faker import Faker
from traceback import print_exc
from conf import MODEL

INPUT_FILE = "books.txt"
OUTPUT_FILE = "books_JSON.json"


def main():

    while True:
        try:
            n = int(input("Введите стартовое число отсчета от 1 до 100 (по умолчанию 1): "))
            if 1 <= n <= 100:
                break
            else:
                print(f"Вы ввели чмсло не из требуемого диапазона, попробуйте снова.")
                continue
        except ValueError:
            print("Вы ввели не число, попробуйте снова.")

    start_pk = 1                            # начальное значение счетчика
    if n >= start_pk:
        start_pk = n
        numbers_of_models = 10               # число выгружаемых записей
        result_list = []                    # выходной список в json

        # with open(OUTPUT_FILE, "w") as f:
        #
        #     for i in range(start_pk, numbers_of_models+1):
        #         k_ = next(generator_library(i))
        #         print(k_)
        #         result_list.append(k_)
        #         print(result_list)
        #         json.dump(result_list, f, indent=4, ensure_ascii=False)

        for i in range(start_pk, numbers_of_models+1):
            k_ = next(generator_library(i))
            result_list.append(k_)

        with open(OUTPUT_FILE, "w") as f:
            json.dump(result_list, f, indent=4, ensure_ascii=False)

#----------------------------------------------------------------------------------

    #Func generator
def generator_library(count_ = 1) -> dict:

    all_model_ = {
        "model": MODEL,
        "pk": count_,
        "fields": {
            "title": read_random_bookname_fromfile(),
            "year": generate_random_year(),
            "pages": generate_random_pages(),
            "isbn13": generate_random_isbn13(),
            "rating": generate_random_rating(),
            "price": generate_random_price(),
            "author": generate_random_author()
        }
    }

    yield all_model_

#-------------functions for Fields-------------------------------------------------
    # 3.1 func random read one book from file book.txt
def read_random_bookname_fromfile() -> str:
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
def generate_random_isbn13() -> str:
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
def generate_random_author() -> list:
    name_author = []
    count_ = random.randint(1, 3)
    for i in range(count_):
            fake = Faker()
            name_author.append(fake.name())

    return name_author

    # func create fields


if __name__ == '__main__':
    main()


