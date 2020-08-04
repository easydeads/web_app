from django.db import models


# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=64)
    nickname = models.CharField(max_length=124, unique=True, default=login)

    def __str__(self):
        return f'nickname - {self.nickname}, passkey - {self.password}, login - {self.login}, id - {self.id}'

    def profiles_list(self):
        pass

    def get_name(self):
        return self.nickname
