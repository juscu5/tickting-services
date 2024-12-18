from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "User_Table"