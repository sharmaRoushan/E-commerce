from django.db import models

class Category(models.Model):
    category_name=models.CharField(max_length=150)
    def __str__(self):
        return self.category_name
class sub_category(models.Model):
    sub_category_name=models.CharField(max_length=150)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    

# Create your models here.
