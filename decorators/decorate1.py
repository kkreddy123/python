def decorate_me(org_fun):
    def inner():
        print("decorated:")
        org_fun()
    return inner

def display():
    print("ordinary:")

display()

decorated_display = decorate_me(display)
decorated_display()