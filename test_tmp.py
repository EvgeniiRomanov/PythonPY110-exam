from faker import Faker

# def gen_isbn13():
#     fake = Faker()
#     Faker.seed(0)
#     k = fake.isbn13()
#
#     return k
#
#
# print(gen_isbn13())

# print(gen_isbn13())
sbn_ = []
fake = Faker()
Faker.seed(0)
for _ in range(2):
   print(fake.isbn13())
   sbn_.append(_)
print(sbn_)
# k = fake.isbn13()
# print(k)
# print(k)