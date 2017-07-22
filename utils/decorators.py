from google.appengine.api import users, memcache
from functools import wraps


def login_required(handler):
    @wraps(handler)
    def wrapper(self, *args, **kwargs):
        user = users.get_current_user()

        if not user:
            return self.redirect_to('about-page')
        elif user.nickname() != "janko.pirih":
            return self.redirect_to('about-page')
        else:
            return handler(self, *args, **kwargs)
    return wrapper


def validate_csrf(handler):
    def wrapper(self, *args, **kwargs):
        csrf_token = self.request.get("csrf_token")
        mem_token = memcache.get(key=csrf_token)

        if mem_token:
            return handler(self, *args, **kwargs)
        else:
            return self.write("You are hacker!")
    return wrapper

