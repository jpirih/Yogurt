from handlers.base import BaseHandler
from models.yogurt import Yogurt
from utils.helpers import str_to_date, good_until_calculate
from utils.decorators import login_required, validate_csrf


class YogurtHandler(BaseHandler):
    """Yogurt production view controller"""

    def get(self):
        """ Main application page view add, edit, delete """
        yogurt_list = Yogurt.get_all()
        params = {"yogurt_list": yogurt_list}
        return self.render_template_with_csrf("yogurt/index.html", params=params)


class YogurtProductionCreate(BaseHandler):
    @login_required
    @validate_csrf
    def post(self):
        """Create new yogurt production  gets data from  add form on main page"""
        prod_date = self.request.get('production_date')
        milk_quantity = float(self.request.get('milk_quantity'))
        cups = int(self.request.get('cups_num'))
        date = str_to_date(prod_date)
        good_until = good_until_calculate(date)
        Yogurt.create(production_date=date, milk_quantity=milk_quantity, cups=cups, good_until=good_until)
        return self.redirect_to('yogurt-index')


class YogurtProductionUpdate(BaseHandler):
    @login_required
    @validate_csrf
    def post(self, yogurt_id):
        """ Update yogurt production, gets data from modal click edit btn """
        yogurt = Yogurt.get_by_id(int(yogurt_id))

        # updated data from form
        production_date = self.request.get('production_date')
        milk_quantity = float(self.request.get('milk_quantity'))
        cups = int(self.request.get('cups'))
        empty = bool(self.request.get("empty"))
        prod_date = str_to_date(production_date)
        good_until = good_until_calculate(prod_date)

        Yogurt.update(yogurt=yogurt,production_date=prod_date, milk_quantity=milk_quantity,
                      cups=cups, good_until=good_until, empty=empty)

        return self.redirect_to('yogurt-index')


class YogurtProductionDelete(BaseHandler):
    """ Softly delete of yogurt production data"""
    @login_required
    @validate_csrf
    def post(self, yogurt_id):
        yogurt = Yogurt.get_by_id(int(yogurt_id))
        Yogurt.delete(yogurt)
        return self.redirect_to('main-page')


class YogurtProductionRestore(BaseHandler):
    """Restore softly deleted data back to life """
    @login_required
    @validate_csrf
    def post(self, yogurt_id):
        yogurt = Yogurt.get_by_id(int(yogurt_id))
        Yogurt.restore(yogurt)
        return self.redirect_to('main-page')


class YogurtDeletedItems(BaseHandler):
    """ Gets list of all softly deleted Yogurt productions data """
    @login_required
    def get(self):
        deleted_items = Yogurt.get_deleted()
        params = {"deleted_items": deleted_items}
        return self.render_template_with_csrf("base/yogurt_deleted_list.html", params=params)
