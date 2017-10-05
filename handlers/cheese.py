"""Fresh cheese production handlers """
from handlers.base import BaseHandler
from models.cheese import Cheese
from utils.decorators import login_required, validate_csrf
from utils.helpers import str_to_date


class CheeseHandler(BaseHandler):
    """ Main cheese production page handler """
    @login_required
    def get(self):
        """Cheese index page view controller """
        cheese_list = Cheese.get_all()
        params = {'cheese_list': cheese_list}
        return self.render_template_with_csrf("cheese/index.html", params=params)


class StoreCheeseHandler(BaseHandler):
    """Store new fresh cheese production data to the database"""
    @login_required
    @validate_csrf
    def post(self):
        """Handles data from web form"""
        date_prod = self.request.get('production_date')
        milk = float(self.request.get('milk_quantity'))
        quantity = int(self.request.get('quantity'))
        prod_date = str_to_date(date_prod)

        Cheese.create(prod_date=prod_date, milk_liters=milk, quantity=quantity)
        return self.redirect_to('cheese-index')


class UpdateCheeseHandler(BaseHandler):
    def post(self, cheese_id):
        # data from update form
        production_date = self.request.get('production_date')
        milk_liters = float(self.request.get('milk_liters'))
        quantitiy = int(self.request.get('quantity'))
        updated_date = str_to_date(production_date)

        cheese = Cheese.get_by_id(int(cheese_id))

        Cheese.update(cheese=cheese, prod_date=updated_date, milk_liters=milk_liters, quantity=quantitiy)
        return self.redirect_to('cheese-index')


