import time
import functools


def timer_v1(func):
    starttime = time.time()
    result = func()
    endtime = time.time()
    execution_time = endtime - starttime
    print('time: ', execution_time)
    return result


def timer_v2(func):
    def wrapper(*args):
        starttime = time.time()
        func(*args)
        endtime = time.time()
        execution_time = endtime - starttime
        print('time: ', execution_time)
    return wrapper


def timer_v3(func):
    @functools.wraps(func)
    def wrapper(*args):
        starttime = time.time()
        result = func(*args)
        endtime = time.time()
        execution_time = endtime - starttime
        print('time: ', execution_time)
        return result
    return wrapper


def timer_v4(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)
        def __getattr__(self, name):
            return getattr(self.wrapped, name)           
    return Wrapper



class Timer_v1:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        starttime = time.time()
        result = self.func(*args)
        endtime = time.time()
        execution_time = endtime - starttime
        print('time: ', execution_time)
        return result


@Timer_v1
def add_num():
    time.sleep(1)
    return 1 + 2


@timer_v2
def add_num_with_decorator():
    time.sleep(1)
    return 1 + 2


@timer_v3
def add_num_with_wraps():
    time.sleep(1)
    return 1 + 2


timer_v1(add_num)
add_num()
add_num_with_decorator()
add_num_with_wraps()
