
class DummyObj:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self


if __name__ == "__main__":
    d = DummyObj(1)
    for i in d:
        print(i.value)