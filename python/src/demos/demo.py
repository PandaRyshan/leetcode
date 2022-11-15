from functools import cache, partial, wraps

import asyncio


def with_greeting(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print("Hello world!")
        return func(*args, **kwargs)
    return wrapper


@with_greeting
def add(x, y):
    """_summary_

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
    print(x + y)


@cache
def add_cache(x, y):
    import time
    print("running")
    time.sleep(2)
    return x + y


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))


if __name__ == "__main__":
    add(2, 5)
    print(add.__name__)
    print(add.__doc__)

    add_two_and_five = partial(add, y=5)
    add_two_and_five(x=4, y=6)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))
    loop.close()
