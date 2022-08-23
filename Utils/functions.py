import string


def make_id_from_name(name):
    name = name.strip()
    for i in string.punctuation:
        name = name.replace(i, "_")
    return name.replace(" ", "_")
