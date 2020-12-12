from __future__ import annotations
import multiprocessing
import random
import time

import datetime

import rx
from rx.scheduler import ThreadPoolScheduler, EventLoopScheduler
from rx import operators as ops

class Request:
    def __init__(self, seed:str, duration_ms: int):
        self.time = int(datetime.datetime.now().timestamp()*1000)
        self.seed = seed
        self.run = True
        self.expireTime = self.time + duration_ms
    def is_expired(self)->bool:
        now = int(datetime.datetime.now().timestamp()*1000)
        return now >= self.expireTime
    def stop(self):
        self.run = False
class Response:
    def __init__(self, id: str, result:str):
        self.value = result
        self.id = id

    def __str__(self):
        return self.value

def generate_content(request: Request) -> Response:
    # sleep for a random short duration between 0.5 to 2.0 seconds to simulate a long-running calculation
    if (not request.run ) or request.is_expired():
        raise TimeoutError("Stop!")
    time.sleep(random.random())
    randomValue = random.randint(1, 10)
    timestamp = int(datetime.datetime.now().timestamp() * 1000)
    responseString = ("%s-%d-%d"%(request.seed, timestamp, randomValue))
    return Response(request.seed, responseString)



def runProcess (request:Request, pool_scheduler:ThreadPoolScheduler)->None:
    rx.repeat_value(request).pipe(
        ops.subscribe_on(pool_scheduler),
        ops.map(lambda r: generate_content(r)),
    ).subscribe(
        on_next=lambda response: print("PROCESS %s: %s"%(response.id, str(response))),
        on_error=lambda e: print(e),
        on_completed=lambda: print("PROCESS done!"),
    )

if __name__ == "__main__":
    requestA = Request("A", 10*1000)
    requestB = Request("B", 10*1000)


    #optimal_thread_count = multiprocessing.cpu_count()
    pool_schedulerA = EventLoopScheduler() #ThreadPoolScheduler(optimal_thread_count)
    runProcess(requestA, pool_schedulerA)
    pool_schedulerB = EventLoopScheduler()
    runProcess(requestB, pool_schedulerB)


    print("running background")
    print("main thread sleep 5 seconds")
    time.sleep(5)
    print("force stop all")
    requestA.stop()
    requestB.stop()
