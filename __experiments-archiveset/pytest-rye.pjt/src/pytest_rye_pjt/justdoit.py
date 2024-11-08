class JustDoIt:

    def __init__(cls, nums):
        cls.nums = nums 

    def __call__(cls, func):
        cls.func = func
        return cls.wrapper

    def wrapper(cls, do):
        doWhat = None
        if do == "sum":
            doWhat = lambda x : sum(x)
        elif do == "max":
            doWhat = lambda x : max(x)
        else:
            pass
        cls.func(do=do)
        return doWhat(cls.nums) if doWhat is not None else "Invalid"
