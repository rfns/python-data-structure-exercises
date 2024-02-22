def search(collection, term):
    if type(collection) is not list:
        raise TypeError("Invalid collection type. Expected list.")

    for position, value in enumerate(collection):
        print(str(position))
        if value == term:
            return position

    return None


print(search(["a", "b", "c", "d"], "c"))
