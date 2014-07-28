from tornado.web import RequestHandler
import json


class BaseHandler(RequestHandler):

    @property
    def params(self):
        if not hasattr(self, "_params"):
            if not self.request.body:
                self._params = {}
            else:
                self._params = json.loads(self.request.body)

        return self._params
