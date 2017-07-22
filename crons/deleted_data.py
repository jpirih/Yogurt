import datetime

from handlers.base import BaseHandler
from models.yogurt import Yogurt


class DeleteYogurtProductionsCron(BaseHandler):
    def get(self):
        deleted_data = Yogurt.query(Yogurt.deleted == True,
                                    Yogurt.updated < datetime.datetime.now() - datetime.timedelta(days=30)).fetch()

        for item in deleted_data:
            item.key.delete()
