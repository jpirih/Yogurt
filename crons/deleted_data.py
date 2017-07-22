import datetime

from handlers.base import BaseHandler
from models.yogurt import Yogurt
from google.appengine.api import mail


class DeleteYogurtProductionsCron(BaseHandler):
    def get(self):
        deleted_data = Yogurt.query(Yogurt.deleted == True,
                                    Yogurt.updated < datetime.datetime.now() - datetime.timedelta(days=30)).fetch()

        counter = len(deleted_data)

        for item in deleted_data:
            item.key.delete()

        # send email when cron job is finished
        mail.send_mail(sender="janko.pirih@gmail.com",
                       to="janko.pirih@gmail.com",
                       subject="Yogurt App - delete cron",
                       body="Cron job completed successfully. number of items older then 30 days {0}".format(counter))
