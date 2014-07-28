from tornado import gen
from tornado.web import asynchronous

from app.handlers.base import BaseHandler
from tornadotools.route import Route
from app.lib import stamp_manager


@Route("/stamps/?")
class StampCollection(BaseHandler):

    @asynchronous
    @gen.engine
    def get(self):

        response = yield gen.Task(stamp_manager.list)
        self.write({"stamps": response})
        self.finish()

    @asynchronous
    @gen.engine
    def post(self):
        if self.params.get("name") is None:
            self.set_status(400)
            self.write({"error": "name must be set"})

        response = yield gen.Task(stamp_manager.create, self.params.get("name"))
        self.write({"stamp": response})


        self.finish()


@Route("/stamps/([a-z0-9-]*)")
class StampInstance(BaseHandler):

    @asynchronous
    @gen.engine
    def get(self, id):
        response = yield gen.Task(stamp_manager.get, id)
        if not response:
            self.write({"error": "Stamp not found", "id": id})
        else:
            self.write({"stamp": response})

        self.finish()
