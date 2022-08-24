import string


def make_id_from_name(name):
    name = name.strip()
    string.punctuation = string.punctuation + " "
    for i in string.punctuation:
        name = name.replace(i, "_")
    name = '_'.join([i for i in name.split("_") if i])
    return name
