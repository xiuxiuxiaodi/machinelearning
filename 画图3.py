def deco(func):
    def _deco(a, b):
        print("before myfunc() called.")
        ret = func(a, b)
        print("  after myfunc() called. result: %s" % ret)
        return ret

    return _deco


@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b

if __name__=="__main__":
    k=myfunc(1, 2)
    print k