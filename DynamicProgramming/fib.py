from typing import Dict


def fib_number(n:int, memory:dict={}) -> int:
    if n in memory:
        return memory[n]
    if n <= 2:
        return 1
    else:
        memory[n] = fib_number(n-2, memory) + fib_number(n-1, memory)
        return memory[n]

if __name__ == "__main__":
    N = fib_number(40)
    print(N)