def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    f = lambda x, y: x
    return pair(f)

def cdr(pair):
    f = lambda x, y: y
    return pair(f)

a = car(cons(3, 4))
b = cdr(cons(3, 4))

print(a)  # Output: 1

print(b)  # Output: 2