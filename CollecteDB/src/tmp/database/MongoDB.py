from .base import DatabaseEngine


class MongoEngine(DatabaseEngine):
    type = "Mongo Motor"

    @classmethod
    def InitDatabase(cls, **kwargs):
        pass