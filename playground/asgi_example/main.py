import json
import pprint


async def app(scope, receive, send):
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


# uvicorn main:app