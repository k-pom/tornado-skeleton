import uuid
from app.config import config
from tornado import gen
from tornado.ioloop import IOLoop

stamps = {}

@gen.engine
def list(callback):
    callback(stamps)


@gen.engine
def get(id, callback):
    callback(stamps.get(id, None))


@gen.engine
def create(name, callback):

    id = str(uuid.uuid1())

    stamps[id] = {
        "id": id,
        "name": name,
        "status": "creating"
    }

    callback(stamps[id])
    IOLoop.instance().add_callback(_do_create, id, name)


def _do_create(id, name):

    stamps[id]['status'] = "done"
    stamps[id]['secret'] = config['some_key']
