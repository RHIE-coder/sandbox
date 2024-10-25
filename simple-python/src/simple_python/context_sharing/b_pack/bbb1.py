from context.marker import mark


@mark(deps="BBB")
def B():
    print("B")

@mark()
def BB():
    print("BB")

@mark(deps="B")
def BBB():
    print("BBB")