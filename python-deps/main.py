import os
from http.server import BaseHTTPRequestHandler, HTTPServer

import requests


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        body = (
            "frameworkless python dependencies ok; "
            f"requests={requests.__version__}\n"
        ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        return


port = int(os.environ.get("PORT", "8000"))
HTTPServer(("0.0.0.0", port), Handler).serve_forever()
