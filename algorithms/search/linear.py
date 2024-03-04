def search(collection: list[str], term: str):
    if type(collection) is not list:
        raise TypeError("Invalid collection type. Expected list.")

    for position, value in enumerate(collection):
        if value == term:
            return position

    return None
