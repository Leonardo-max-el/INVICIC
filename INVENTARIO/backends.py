from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import work

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = work.objects.get(correo=username)
            if check_password(password, user.contraseña):
                return user
        except work.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return work.objects.get(pk=user_id)
        except work.DoesNotExist:
            return None
