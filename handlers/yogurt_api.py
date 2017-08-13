from handlers.base import BaseHandler
from models.yogurt import Yogurt
from utils.api_helpers import DateTimeEncoder

import json


class YogurtProductionApi(BaseHandler):
    def get(self):
        production_list = Yogurt.get_all()
        data = [item.to_dict() for item in production_list]

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(data, cls=DateTimeEncoder, default=str))



