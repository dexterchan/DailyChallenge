import time
from functools import wraps

def timer(func):
    """a decorator to time a function

    Args:
        func ([type]): [description]
    """
    #wraps fix the problem of returning meta data of decorator function
    @wraps(func)
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_total = time.time() - t_start
        print (f"{func.__name__} took {t_total} s")
        return result
    return wrapper

@timer
def sleep_a_while(t:int) -> str:
    """SLeeping a while function

    Args:
        t (int): seconds to sleep

    Returns:
        str: sleeping description
    """
    time.sleep(t)
    return f"sleep for {t} seconds"

ret:str = sleep_a_while(t=2)
print (f"returns {ret}")
print(f"{sleep_a_while.__doc__}")

def counter(func):
  def wrapper(*args, **kwargs):
    wrapper.count += 1
    # Call the function being decorated and return the result
    return func(*args, **kwargs)
  wrapper.count = 0
  # Return the new decorated function
  return wrapper

# Decorate foo() with the counter() decorator
@counter
def foo():
  print('calling foo()')

foo()
foo()

print('foo() was called {} times.'.format(foo.count))


def run_n_times(n):
  """Define and return a decorator

  Args:
      n ([type]): [description]
  """
  def decorator(func):
    def wrapper(*args, **kwargs):
      for i in  range(n):
        func(*args, **kwargs)
    return wrapper
  return decorator

@run_n_times(3)
def print_sum(a,b):
  print(a+b)

print_sum(5,4)