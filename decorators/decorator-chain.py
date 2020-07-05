from functools import wraps

def star(org_func):
    print("star function argunamet :" + org_func.__name__)
    @wraps(org_func)
    def inner(*args, **kwargs):
        print("*" * 30)
        org_func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(org_func):
    print("percent function argunamet :" + org_func.__name__)
    @wraps(org_func)
    def inner(*args, **kwargs):
        print("%" * 30)
        org_func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")

#func1 = percent(printer)
#func2 = star(func1)
#func2("Hello")