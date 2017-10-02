from google.appengine.ext import ndb


class Cheese(ndb.Model):

    """Fresh cheese production datastore model """
    prod_date = ndb.DateProperty()
    milk_liters = ndb.FloatProperty()
    quantity = ndb.IntegerProperty()
    deleted = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def get_all(cls):
        """ Gets all cheese production data from datastore"""
        return cls.query(cls.deleted == False).order(-cls.prod_date).fetch()

    @classmethod
    def get_deleted(cls):
        """Gets only deleted cheese production data from data store"""
        return cls.query(cls.deleted == True).order(-cls.prod_date).fetch()

    @classmethod
    def create(cls, prod_date, milk_liters, quantity):
        """Creates new cheese production object and saves it to datastore """
        new_cheese = cls(prod_date=prod_date, milk_liters=milk_liters, quantity=quantity)
        new_cheese.put()
        return new_cheese

