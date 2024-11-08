from context.marker import mark


@mark(deps="AA")
def A():
    print("A")

@mark()
def AA():
    print("AA")

@mark()
def AAA():
    print("AAA")