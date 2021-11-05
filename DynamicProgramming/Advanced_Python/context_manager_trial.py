from contextlib import contextmanager
#useful for data base connection
@contextmanager
def my_context():
    print ("hello")
    yield 42
    print ("good byte")

with my_context() as foo:
    print(f"foo is {foo}")