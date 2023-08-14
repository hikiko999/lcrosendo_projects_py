# fill in this function
def fib():
    # 1 1 2 3 5
    # 1 + 1, 1 + 2, 2 + 3, 3 + 5
    a = 1
    b = 0
    while True:
        yield a # 1 1 2
        b = a + b # 1 2
        a, b = b, a # 1,1 2,1
        # b = a + b
        # yield b # 1
        # a, b = b, a
    
# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break