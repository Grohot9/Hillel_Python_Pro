def new_format(number: str):
    # place dots between digit order numbers
    return ".".join(number[::-1][index:index + 3] for index in range(0, len(number), 3))[::-1]
