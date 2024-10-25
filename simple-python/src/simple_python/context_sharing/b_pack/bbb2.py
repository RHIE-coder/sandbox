from context.marker import mark


@mark(deps="BBBBB")
def BBBB():
    print("BBBB")

@mark()
def BBBBB():
    print("BBBBB")
