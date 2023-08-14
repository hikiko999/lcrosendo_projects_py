def type_check(correct_type):
    # correct_type = int
    def checker (old_func):
        # old_func = times2 function
        def new_func(value):
            if isinstance(value,correct_type):
                return old_func(value)
            else:
                print("'%s' is a Bad Type" % (value))
                # raise TypeError("Bad Type")
        return new_func
    return checker

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])