def tags(t):
    def add_tag(f):
        def wrapper(*args):
            return f"<{t}>{f(*args)}</{t}>"
        return wrapper
    return add_tag



@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
