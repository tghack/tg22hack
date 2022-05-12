#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sanic import Sanic, response
from sanic_useragent import SanicUserAgent

app = Sanic(__name__)
SanicUserAgent.init_app(app)

@app.route("/")
async def index(request):
    if "curl" in request.headers['user-agent']:
        return await response.file("install.sh")
    else:
        return await response.file("notthatsimple.png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1339, auto_reload=False, debug=False)