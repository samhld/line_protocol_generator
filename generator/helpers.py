import string
import datetime
import random

def create_string(num: int):
    letters = string.ascii_lowercase
    s = "".join(random.choice(letters) for i in range(num))
    return s

def create_int(num: int):
    lower_bound = 10 ** (num - 1)
    upper_bound = 10 ** num - 1
    return(random.randint(lower_bound,upper_bound))

def create_timestamp(precision: str='s'):
    '''
    Generates a timestamp to be used at end of line of Line Protocol.
    The precision can be set to seconds, milliseconds, microseconds, or nanoseconds.
    Less precision is achieved with rounding the timestamp to the passed precison
    and then adding zeros as  necessary to keep the timestamp length constant.
    '''
    now  = datetime.datetime.now()
    ts = now.timestamp()
    if precision == ('s' or 'S'):
        ts = round(ts)
        ts = ts*10**9
        # return(ts*10**9)
    elif precision == ('ms' or 'MS'):
        ts = round(ts*10**3)
        ts = ts*10**6
        # return(ts*10**6)
    elif precision == ('us' or 'US'):
        ts = round(ts*10**6)
        # return(ts*10**3)
    elif precision == ('ns' or 'NS'):
        ts = round(ts*10**9)
        # return(ts)
    else:
        raise ValueError("Warn: gen_ts() only takes `s`, `ms`, `us`, or `ns` as inputs")
    
    return ts