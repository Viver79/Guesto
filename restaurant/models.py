from django.db import models

# Create your models here.
from django.db import models
from os import path
from uuid import uuid4


class Category(models.Model):

    title = models.CharField(max_length=50, unique=True)
    category_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Dish(models.Model):

    def get_file_name(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/dishes/', filename)

    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    photo = models.ImageField(upload_to=get_file_name)
    description = models.CharField(max_length=300, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class UsersMessages(models.Model):

    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    message = models.CharField(max_length=200)

    is_processed = models.BooleanField(default=False)
    send_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name}-{self.user_email}: {self.message[:20]}'