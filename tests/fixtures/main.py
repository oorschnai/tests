"""Stub upstream used by the integration tests.

Started by the test harness on a random port so that the outbound calls of the
notification senders hit something local.
"""

from __future__ import annotations

from fastapi import FastAPI, Request

app = FastAPI(title="ep-test-upstream")

RECEIVED: list[dict] = []


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


@app.post("/hooks/{name}")
async def hook(name: str, request: Request) -> dict:
    RECEIVED.append({"name": name, "body": await request.body()})
    return {"received": len(RECEIVED)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8099)
