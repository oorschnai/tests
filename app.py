from sanic import Sanic, json

app = Sanic("analytics_sanic")


@app.get("/health")
async def health(request):
    return json({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
