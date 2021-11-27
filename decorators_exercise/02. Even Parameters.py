def even_parameters(f):
    def wrapper(*numbers):

        if len([num for num in numbers if type(num) == str]) > 0 or len([num for num in numbers if num % 2 == 1]) > 0:
            return f"Please use only even numbers!"

        else:
            return f(*numbers)

    return wrapper

@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

