#!/usr/bin/env python
import webapp2

from handlers.base import MainHandler, CookieAlertHandler, AboutHandler, DashboardHandler
from handlers.cheese import CheeseHandler, StoreCheeseHandler
from handlers.yogurt_api import YogurtProductionApi
from handlers.yogurt_productions import YogurtProductionCreate, YogurtProductionUpdate, YogurtProductionDelete
from handlers.yogurt_productions import YogurtDeletedItems, YogurtProductionRestore, YogurtHandler
from crons.deleted_data import DeleteYogurtProductionsCron
from crons.yogurt_expired import YogurtExpiredCron


app = webapp2.WSGIApplication([

    # application routes - static pages
    webapp2.Route('/', handler=MainHandler, name="main-page"),
    webapp2.Route('/about', handler=AboutHandler, name="about-page"),
    webapp2.Route('/set-cookie', handler=CookieAlertHandler, name="set-cookie"),
    webapp2.Route('/dashboard', handler=DashboardHandler, name="dashboard"),

    # fresh cheese
    webapp2.Route('/cheese/production', handler=CheeseHandler, name="cheese-index"),
    webapp2.Route('/cheese/production/create', handler=StoreCheeseHandler, name="cheese-production-create"),

    # yogurt
    webapp2.Route('/yogurt-deleted', handler=YogurtDeletedItems, name="yogurt-deleted-list"),
    webapp2.Route('/yogurt/production', handler=YogurtHandler, name="yogurt-index"),
    webapp2.Route('/yogurt/production/create', handler=YogurtProductionCreate, name="yogurt-production-create"),
    webapp2.Route('/yogurt/production/<yogurt_id:\d+>/update', handler=YogurtProductionUpdate,name="yogurt-production-update"),
    webapp2.Route('/yogurt/production/<yogurt_id:\d+>/delete', handler=YogurtProductionDelete, name="yogurt-production-delete"),
    webapp2.Route('/yogurt/production/<yogurt_id:\d+>/restore', handler=YogurtProductionRestore, name="yogurt-production-restore"),

    # api routes
    webapp2.Route('/api/yogurt/production-list', handler=YogurtProductionApi, name="yogurt-api-production-list"),

    # cron jobs
    webapp2.Route('/cron/delete-data', handler=DeleteYogurtProductionsCron, name='cron-delete-yogurt-data'),
    webapp2.Route('/cron/yogurt-expired', handler=YogurtExpiredCron, name='cron-yogurt-expired'),
], debug=True)

