import signal
from functools import wraps
import time
def raise_timeout(*args, **kwargs):
    raise TimeoutError()

#When an "alarm" signal goes off, call raise_timeout()
signal.signal(signalnum=signal.SIGALRM, handler=raise_timeout)

# #Set Off an alarm in 5 seconds
# signal.alarm(5)
# #cancel the alarm
# signal.alarm(0)

def timeout(n_seconds:int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            signal.alarm(n_seconds)
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0)
        return wrapper
    return decorator

def timeout_in_5s(func):
    def wrapper(*args, **kwargs):
        # Set an alarm for seconds
        signal.alarm(5)
        try:
            return func(*args, **kwargs)
        finally:
            signal.alarm(0)
    return wrapper

@timeout(2)
def over_sleep():
    """Over sleep for 10s
    """
    time.sleep(10)

print(over_sleep.__doc__)
over_sleep()