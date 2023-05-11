from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

from .models import Person

class PersonAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            person = Person.objects.get(username=username)
        except Person.DoesNotExist:
            return None

        if person.password == password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username)
                user.set_unusable_password()
                user.save()

            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None