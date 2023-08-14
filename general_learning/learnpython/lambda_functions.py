l = [2,4,7,3,14,19]
for i in l:
    checker = lambda i : i%2
    check_result = checker(i)
    if check_result == 0:
        print("False")
    else:
        print("True")