from search import linear


def run(term="first"):
    print(f"Searching for term {term} using linear search: {play_linear(term)}")


def play_linear(search_term):
    test_input = ["This", "is", "actually", "my", "first", "Python", "project"]

    return linear.search(test_input, search_term)
