def repeat(n):
    def wrapper(func):
        def inner(*args):
            for i in range(n):
                func(*args)

        return inner

    return wrapper


def decorator_with_parameter(parameter):

    def wrapper_function(function):
        def inner_function(*args, **kwargs):
            print(parameter)
            # actions before given function run
            for a in range(parameter):
                print("aaa")
            function(*args, **kwargs)
            # actions after given function run
        return inner_function
    return wrapper_function


@decorator_with_parameter(10)
def helloworld(text):
    print(text)


helloworld("aaabbb")
