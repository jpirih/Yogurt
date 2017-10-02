from google.appengine.ext import ndb


class Yogurt(ndb.Model):
    """ Yogurt production  datastore model with all necessary methods """
    production_date = ndb.DateProperty()
    milk_quantity = ndb.FloatProperty()
    cups = ndb.IntegerProperty()
    good_until = ndb.DateProperty()
    empty = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)

    @classmethod
    def get_all(cls):
        """ Gets all non deleted data about Yogurt productions from the datastore. """
        return cls.query(cls.deleted == False).order(-cls.production_date).fetch()

    @classmethod
    def get_deleted(cls):
        """ Gets all softly deleted data about Yogurt Productions """
        return cls.query(cls.deleted == True).order(-cls.updated).fetch()

    @classmethod
    def create(cls, production_date, milk_quantity, cups, good_until):
        """ Create new Yogurt production and save to datastore. """
        new_yogurt_production = cls(production_date=production_date, milk_quantity=milk_quantity,
                                    cups=cups, good_until=good_until)
        new_yogurt_production.put()

        return new_yogurt_production

    @classmethod
    def update(cls, yogurt, production_date, milk_quantity, cups, good_until, empty):
        """ Update yogurt productionInsert instance of Yogurt clas to update and all params that you can change """
        yogurt.production_date = production_date
        yogurt.milk_quantity = milk_quantity
        yogurt.cups = cups
        yogurt.good_until = good_until
        yogurt.empty = empty
        yogurt.put()

        return yogurt

    @classmethod
    def delete(cls, yogurt):
        """Yogurt production soft delete"""
        yogurt.deleted = True
        yogurt.put()

        return yogurt

    @classmethod
    def restore(cls, yogurt):
        """ Restores soft deleted yogurt production data """
        yogurt.deleted = False
        yogurt.put()

        return yogurt

    @classmethod
    def destroy(cls, yogurt):
        """ Completely removes yogurt production data from the datastore"""
        return yogurt.key.delte()



