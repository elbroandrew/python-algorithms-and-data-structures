import asyncio


"""
code similar to gevent
"""

async def task(pid):
    await asyncio.sleep(1)
    print("Task %s done" % pid)

loop = asyncio.get_event_loop()


futures = asyncio.gather(
    *[task(i) for i in range(5)]
)

loop.run_until_complete(futures)

loop.close()

#asyncio.run(task(3))