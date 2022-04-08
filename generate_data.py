from telnetlib import STATUS
from mimesis import Generic
from mimesis.locales import Locale
import random

generic = Generic(locale=Locale.EN)

def generate_user():
    created_at = generic.datetime.datetime(start=2015, end=2022)
    first_name = generic.person.first_name()
    email = generic.person.email()
    country = generic.address.country()
    return created_at, first_name, email, country

def generate_order():
    user_id = random.randint(1, 9513)
    created_at = generic.datetime.datetime(start=2015, end=2022)
    order_status_id = random.randint(1, 3)
    price = generic.finance.price(minimum=10, maximum=500)
    return user_id, created_at, order_status_id, price
    