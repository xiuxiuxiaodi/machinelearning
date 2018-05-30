def decorator_func(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

@decorator_func
def func(name):
    print 'my name is ',name
    return name

a=func('baomingguang')
print a

