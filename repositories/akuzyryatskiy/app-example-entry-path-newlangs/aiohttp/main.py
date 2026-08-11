import os

from aiohttp import web


async def index(_request: web.Request) -> web.Response:
    return web.Response(
        text="<h1>TimeWeb + Aiohttp = ❤️</h1>",
        content_type="text/html",
    )


app = web.Application()
app.router.add_get("/", index)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    web.run_app(app, host="0.0.0.0", port=port)
