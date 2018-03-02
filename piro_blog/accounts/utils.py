import string
import random


def generate_random_string(length=50):
    choice_set = string.ascii_letters + string.digits
    return ''.join(random.choices(choice_set, k=length))
