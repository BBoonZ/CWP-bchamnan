def array_of_names(d):
    result = []
    for first, last in d.items():
        result.append(first.capitalize() + " " + last.capitalize())
    return result

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))