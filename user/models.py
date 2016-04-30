from django.contrib.auth.models import User
from django.db import models


class UserNew(User):
    birthday = models.DateField(unique=False)
    random_number = models.IntegerField(unique=False)
