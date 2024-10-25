from context.marker import mark


@mark(deps="AAAAA")
def AAAA():
    print("AAAA")

@mark(deps="AAAA")
def AAAAA():
    print("AAAAA")
