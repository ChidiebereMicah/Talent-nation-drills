def first_and_last(value):

    if value == "":
        return {"first": "", "last": ""}

    position = {"first": value[0],
                "last": value[-1]
    }

    return position
