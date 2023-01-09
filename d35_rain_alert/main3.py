import time

def speed_calc_decorator(funkcja):

    def wrapper_fun():
        start_time = time.time()
        funkcja()
        finish_time = time.time()
        czas = finish_time - start_time
        print(czas)
    return wrapper_fun

def fast_function():
    for i in range(10000000):
        i = i * i
def slow_function():
    for i in range(100000000):
        i = i * i


def startstop(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished!")
    return wrapper

@startstop
def roll():
    print("Rolling on the floor laughing XD")

def measuretime(func):
    def wrapper():
        starttime = time.perf_counter()
        func()
        endtime = time.perf_counter()
        print(f"Time needed: {endtime - starttime} seconds")
    return wrapper
@measuretime
def wastetime():
    sum([i**2 for i in range(1000000)])


def sleep(func, how_long):
    def wrapper():
        time.sleep(how_long)
        return func()
    return wrapper


# @sleep(4,-)
# def wakeup():
#     print("Get up! Your break is over.")

def decorator(function):
    def wrapper_function():
        # actions before given function run
        function()
        # actions after given function run
    return wrapper_function

def wastetime():
    sum([i**2 for i in range(10000000)])


def decorator_for_functions_with_arguments(function):
    def wrapper_function(*args, **kwargs):
        # actions before given function run
        function(*args, **kwargs)
        print(function.__name__)
        # actions after given function run
    return wrapper_function


@decorator_for_functions_with_arguments
def zwykłaFunkcja(a, b, c):
    print("To jest zwykła funkcja, która dodaje liczby:")
    print(a + b + c)


zwykłaFunkcja(1, 2, 3)