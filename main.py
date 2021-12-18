import random
import json

from faker import Faker
from conf import MODEL

INPUT_FILE = "books.txt"
OUTPUT_FILE = "books_JSON.json"


def main() -> json:

    while True:
        try:
            num_tmp = int(input("Введите стартовое число отсчета от 1 до 100 (по умолчанию 1): "))
            if 1 <= num_tmp <= 100:
                break
            else:
                print(f"Вы ввели чмсло не из требуемого диапазона, попробуйте снова.")
                continue
        except ValueError:
            print("Вы ввели не число, попробуйте снова.")

    start_pk = 1
    if num_tmp >= start_pk:
        start_pk = num_tmp
        numbers_of_models = 100              # numbers of models load to json
        result_list = []                   # list to json

        for number_ in range(start_pk, numbers_of_models+1):
            k_ = next(generator_library(number_))
            result_list.append(k_)

        with open(OUTPUT_FILE, "w") as f:
            json.dump(result_list, f, indent=4, ensure_ascii=False)


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


def read_random_bookname_fromfile() -> str:

    with open(INPUT_FILE, "r", encoding="UTF8") as f:
        rows_ = f.readlines()
        rows_ = [x.strip() for x in rows_]
        rows_random = random.choice(rows_)

    return rows_random


def generate_random_year() -> int:
    tmp_year = random.randint(1800, 2100)
    return tmp_year


def generate_random_pages() -> int:
    tmp_pages = random.randint(100, 1000)
    return tmp_pages


def generate_random_isbn13() -> str:
    fake = Faker()
    isbn13_ = fake.isbn13()
    return isbn13_


def generate_random_rating() -> float:
    tmp_rating = round(random.uniform(0, 5), 7)
    return tmp_rating


def generate_random_price() -> float:
    tmp_price = round(random.uniform(100, 2000), 2)
    return tmp_price


def generate_random_author() -> list:
    name_author = []
    count_ = random.randint(1, 3)
    for i in range(count_):
        fake = Faker()
        name_author.append(fake.name())

    return name_author


if __name__ == '__main__':
    main()


