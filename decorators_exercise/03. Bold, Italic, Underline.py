def make_bold(fun):
    def wrapper(*args):
        result = fun(*args)
        return f"<b>{result}</b>"
    return wrapper


def make_italic(fun):
    def wrapper(*args):
        result = fun(*args)
        return f"<i>{result}</i>"
    return wrapper


def make_underline(fun):
    def wrapper(*args):
        result = fun(*args)
        return f"<u>{result}</u>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
