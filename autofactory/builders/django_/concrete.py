from factory import random


def from_choices(field_cls):
    random_choice_tuple = random.randgen.choice(field_cls.choices)
    random_choice = random_choice_tuple[0]

    return random_choice
