#!/usr/bin/env python
from tornado.options import define, options
import tornado
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornadotools.route import Route
from app.handlers import example

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, Route.routes())


def main():
    tornado.options.parse_command_line()
    http_server = HTTPServer(Application())
    http_server.listen(options.port)
    IOLoop.instance().start()


if __name__ == "__main__":
    main()
