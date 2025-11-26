# faker use example
from faker import Faker

fake = Faker('ru_RU')

for _ in range(5):
    print(fake.name())
    print(fake.email())
    print(fake.address())
    #print(fake.text())