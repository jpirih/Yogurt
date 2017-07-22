#!/usr/bin/env python
import webapp2

from handlers.base import MainHandler, CookieAlertHandler, AboutHandler
from handlers.yogurt_productions import YogurtProductionCreate, YogurtProductionUpdate, YogurtProductionDelete
from handlers.yogurt_productions import YogurtDeletedItems, YogurtProductionRestore

app = webapp2.WSGIApplication([
    webapp2.Route('/', handler=MainHandler, name="main-page"),
    webapp2.Route('/about', handler=AboutHandler, name="about-page"),
    webapp2.Route('/set-cookie', handler=CookieAlertHandler, name="set-cookie"),
    webapp2.Route('/yogurt-deleted', handler=YogurtDeletedItems, name="yogurt-deleted-list"),
    webapp2.Route('/yogurt/production/create',handler=YogurtProductionCreate, name="yogurt-production-create"),
    webapp2.Route('/yogurt/production/<yogurt_id:\d+>/update', handler=YogurtProductionUpdate,name="yogurt-production-update"),
    webapp2.Route('/yogurt/production/<yogurt_id:\d+>/delete', handler=YogurtProductionDelete,name="yogurt-production-delete"),
    webapp2.Route('/yogurt/production/<yogurt_id:\d+>/restore', handler=YogurtProductionRestore,name="yogurt-production-restore"),
], debug=True)

