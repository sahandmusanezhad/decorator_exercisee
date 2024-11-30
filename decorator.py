def new_decorator(orginal_func):
    def wrap_func():
        print('Some extra code, before the original function')
        orginal_func()
        print('Some extra code, after the original function')

    return wrap_func


@new_decorator
def func1():
    print('i want to be decorated')