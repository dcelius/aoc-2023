# File Helper
def read_file_lines(filepath):
    with open(filepath, 'r') as file:
        lines = [line.rstrip('\n') for line in file.readlines()]
    return lines

# Int Try Parse
def int_try_parse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False
    
def int_list_parse_from_string(values, separator = ' '):
    int_list = []
    for value in values.split(separator):
        result, is_int = int_try_parse(value)
        if is_int:
            int_list.append(result)
    return int_list

from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap