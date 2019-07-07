def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair
    
def car(a):
    return a[0]
    
def cdr(a):
    return a[1]
    
print cons(3, 4) 