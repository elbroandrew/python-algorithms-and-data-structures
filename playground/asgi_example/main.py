import json
import pprint
import time
import traceback


async def app(scope, receive, send):
    traceback.print_stack()
    assert scope["type"] == "http"
    pprint.pprint(scope)

    incoming_event = await receive()
    pprint.pprint(incoming_event)

    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": [[b"content-type", b"application/json"],],
    })

    await send(
        {"type": "http.response.body", "body": json.dumps({"key": "value"}).encode(),}
    )


class TimingMiddleware:
    """
    this middleware displays the time that await took
    """
    def __init__(self, myapp):
        self.app = myapp

    async def __call__(self, scope, receive, send):
        start_time = time.time()
        await self.app(scope, receive, send)
        end_time = time.time()
        print(f"Took {end_time - start_time:.2f} seconds.")

wrapped_application = TimingMiddleware(app)
