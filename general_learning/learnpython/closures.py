# your code goes here

def multiplier_of(number):
    # 1 - number = 5
    def multiplier(n):
        # 3 - number is remembered
        # 4 - function is called
        # n is used = 9
        return number*n
    return multiplier
    # 2 - returns function

multiplywith5 = multiplier_of(5)
# print(multiplywith5)
print(multiplywith5(9))
print(multiplywith5(10))