import datetime
from handlers.base import BaseHandler
from models.yogurt import Yogurt

from google.appengine.api import mail


class YogurtExpiredCron(BaseHandler):
    def get(self):
        expired_data = Yogurt.query(Yogurt.good_until < datetime.datetime.now(), Yogurt.empty == False).fetch()

        expired_count = len(expired_data)

        content = " Un used Yogurt that is allready too old: \n \n" \
                  "Prod. Date \t Cups \t Expired On\n"
        for item in expired_data:
            content += "{0} \t {1} \t {2} \n".format(item.production_date, item.cups, item.good_until)

        content += "\n Total Expired productions: {0}".format(expired_count)
        content = content

        mail.send_mail(sender="janko.pirih@gmail.com",
                       to="janko.pirih@gmail.com",
                       subject="Yogurt App - Expired Yogurt Reminder",
                       body=content)

