import asyncio
import concurrent.futures

def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    with open('/dev/urandom', 'rb') as f:
        return f.read(100)

class Hub():
    def __init__(self):
        self.subscriptions = set()

    def publish(self, message):
        for queue in self.subscriptions:
            queue.put_nowait(message)

async def main():
    loop = asyncio.get_running_loop()

    ## Options:

    # 2. Run in a custom thread pool:
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result =  loop.run_in_executor(
            pool, blocking_io)
        print('custom thread pool', result)


asyncio.run(main())
print("running")