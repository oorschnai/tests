import os

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/html; charset=utf-8")
        self.write("<h1>TimeWeb + Tornado = ❤️</h1>")


def make_app() -> tornado.web.Application:
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    port = int(os.getenv("PORT", "8000"))
    app.listen(port, address="0.0.0.0")
    tornado.ioloop.IOLoop.current().start()
