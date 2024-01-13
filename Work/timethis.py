# timethis.py

import time


def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__module__}.{func.__name__} : {end - start}")
        return ret

    return wrapper
