"""Thin WSGI wrappers applied to the served application."""

from __future__ import annotations

import time


class ProxyHeaders:
    """Rewrites the scheme from the balancer header."""

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        forwarded = environ.get("HTTP_X_FORWARDED_PROTO")
        if forwarded:
            environ["wsgi.url_scheme"] = forwarded.split(",")[0].strip()
        return self.app(environ, start_response)


class RequestTiming:
    """Adds the handler duration to the response headers."""

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        started = time.monotonic()

        def start(status, headers, exc_info=None):
            elapsed = (time.monotonic() - started) * 1000
            headers.append(("X-Runtime-Ms", f"{elapsed:.1f}"))
            return start_response(status, headers, exc_info)

        return self.app(environ, start)
