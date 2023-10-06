from django.db import models

class Category(models.Model):
    category_name=models.CharField(max_length=150)
    def __str__(self):
        return self.category_name
class sub_category(models.Model):
    sub_category_name=models.CharField(max_length=150)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.sub_category_name
class Product (models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    s_category=models.ForeignKey(sub_category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='Ecommerce/image')
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.product_name
# Create your models here.
