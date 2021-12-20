import random
import json

from faker import Faker
from conf import MODEL

INPUT_FILE = "books.txt"
OUTPUT_FILE = "books_JSON.json"


def main():
    """
    Input integer number of books that will be export to json.
    Generates the entered numbers of dictionaries and put it
    into the list. Export list of dictionaries to json.
    """
    while True:
        try:
            num_tmp = int(input("Введите стартовое число отсчета от 1 до 100 (по умолчанию 1): "))
            if 1 <= num_tmp <= 100:
                break
            else:
                print(f"Вы ввели число не из требуемого диапазона, попробуйте снова.")
                continue
        except ValueError:
            print("Вы ввели не число, попробуйте снова.")

    start_pk = 1                            # start number for books
    if num_tmp >= start_pk:
        start_pk = num_tmp
        numbers_of_models = 100             # number of books load to json
        result_list = []                    # list with all books load to json

        for number_ in range(start_pk, numbers_of_models+1):
            k_ = next(generator_library(number_))
            result_list.append(k_)

        with open(OUTPUT_FILE, "w") as f:
            json.dump(result_list, f, indent=4, ensure_ascii=False)


def generator_library(count_ = 1) -> dict:
    """
    Generate one random book.

    :param count_: start count
    :type count_: int
    :return: dict
    """
    all_model_ = {
        "model": MODEL,                                         # model name
        "pk": count_,                                           # position number
        "fields": {
            "title": read_random_bookname_fromfile(),           # book name
            "year": generate_random_year(),                     # year of made
            "pages": generate_random_pages(),                   # number of pages
            "isbn13": generate_random_isbn13(),                 # number of isbn
            "rating": generate_random_rating(),                 # rating in our magazine
            "price": generate_random_price(),                   # price in $
            "author": generate_random_author()                  # author this book
        }
    }

    yield all_model_


def read_random_bookname_fromfile() -> str:
    """Random read one book name from file and return it."""
    with open(INPUT_FILE, "r", encoding="UTF8") as f:
        rows_ = f.readlines()
        rows_ = [x.strip() for x in rows_]
        rows_random = random.choice(rows_)

    return rows_random


def generate_random_year() -> int:
    """ Generate year. """
    tmp_year = random.randint(1800, 2100)
    return tmp_year


def generate_random_pages() -> int:
    """ Generate numbers of pages. """
    tmp_pages = random.randint(100, 1000)
    return tmp_pages


def generate_random_isbn13() -> str:
    """ Generate ISBN. """
    fake = Faker()
    isbn13_ = fake.isbn13()
    return isbn13_


def generate_random_rating() -> float:
    """ Generate rating. """
    tmp_rating = round(random.uniform(0, 5), 7)
    return tmp_rating


def generate_random_price() -> float:
    """ Generate price. """
    tmp_price = round(random.uniform(100, 2000), 2)
    return tmp_price


def generate_random_author() -> list:
    """ Generate author. """
    name_author = []
    count_ = random.randint(1, 3)
    for i in range(count_):
        fake = Faker(locale="ru_RU")
        name_author.append(fake.name())

    return name_author


if __name__ == '__main__':
    main()
