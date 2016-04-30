from django.contrib.auth.models import User
from django.db import models


class UserNew(User):
    birthday = models.DateField()
    random_number = models.IntegerField()
