from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    route_name = models.CharField(max_length=20, db_index=True)
    add_time = models.DateTimeField(auto_now_add=True, db_index=True)
    modify_time = models.DateTimeField(auto_now=True, db_index=True)
    category = models.ForeignKey(Category, default=0)

    def __str__(self):
        return self.title
