import fastapi
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from slow import ans
import requests
from util import tracer
app = fastapi.FastAPI()

@app.get("/foobar")
async def foobar():
    return {"message": "hello world"}

@app.get("/op")
async def foobar():
    with tracer.start_as_current_span("rootSpan"):
        ans()
        with tracer.start_as_current_span("childSpan"):
            data = requests.get("https://random-data-api.com/api/v2/users?size=1").json()
    return data

FastAPIInstrumentor.instrument_app(app)
