def outerfunc(msg):
    print("outer: " + msg)
    def innerfun():
        print("inner: " + msg)
    return innerfun

funct1 = outerfunc("hi")
funct1()
