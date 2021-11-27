# def logged(fun_name):
#     def wrapper(*elements):
#         result = fun_name(*elements)
#         return f"you called {fun_name.__name__}{(elements)}\nit returned {result}"
#     return wrapper
#
#
#
# @logged
# def sum_func(a, b):
#     return a + b
# print(sum_func(1, 4))
#
# @logged
# def func(*args):
#     return 3 + len(args)
# print(func(4, 4, 4))

z = [1, "fp", 5]
x = [a for a in z if type(a)==str]
print(x)