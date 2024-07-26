import re


def class_name_changer(cls, new_name):
    if not isinstance(new_name, str) or not re.match(r'^[A-Z][A-Za-z0-9]*$', new_name):
        raise ValueError("Doesn't match the requirements")


    cls.__name__ = new_name
    return cls