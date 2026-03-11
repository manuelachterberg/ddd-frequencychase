#!/usr/bin/env python3
"""
Simple local server for Frequenzjaeger.

Why:
- Browser audio playback is more reliable on http://localhost than file://
- Keeps setup dependency-free (stdlib only)
"""

from __future__ import annotations

import argparse
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


class AppHandler(SimpleHTTPRequestHandler):
    def _should_serve_app_shell(self, path: str) -> bool:
        parsed = urlparse(path)
        resolved = Path(super().translate_path(parsed.path))

        # Serve the app shell for root and extensionless routes so direct opens
        # like / or stale paths such as /login still load the game UI.
        return parsed.path == "/" or (not resolved.exists() and "." not in Path(parsed.path).name)

    def translate_path(self, path: str) -> str:
        parsed = urlparse(path)
        if self._should_serve_app_shell(path):
            return str(Path.cwd() / "index.html")

        return super().translate_path(parsed.path)

    def do_GET(self) -> None:
        if self._should_serve_app_shell(self.path):
            self.path = "/index.html"
        super().do_GET()

    def do_HEAD(self) -> None:
        if self._should_serve_app_shell(self.path):
            self.path = "/index.html"
        super().do_HEAD()

    # Slightly more forgiving cache policy while iterating UI/audio behavior.
    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def guess_type(self, path: str) -> str:
        # Ensure correct mime in all environments.
        if path.endswith(".mp3"):
            return "audio/mpeg"
        return super().guess_type(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run local server for Frequenzjaeger")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="Bind port (default: 8000)")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    os.chdir(root)

    server = ThreadingHTTPServer((args.host, args.port), AppHandler)
    url = f"http://{args.host}:{args.port}/index.html"
    print(f"Serving {root}")
    print(f"Open: {url}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
