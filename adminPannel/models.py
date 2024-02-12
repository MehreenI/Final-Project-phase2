from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User

RATING = (
    (1,'★☆☆☆☆'),
    (2,'★★☆☆☆'),
    (3,'★★★☆☆'),
    (4,'★★★★☆'),
    (5,'★★★★★'),
)

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    def __str__(self):
        return self.category_name
    
    def category_image(self):
        return mark_safe('<img src="%s" width="100" height="100"/>' % self.image.url)


class Product(models.Model):
    name = models.CharField(max_length=200)
    original_price = models.IntegerField(null=True)
    stock = models.IntegerField()
    description = models.TextField()
    short_description = models.TextField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)
    for_sale = models.BooleanField(default=False)
    discounted_price = models.IntegerField(null=True)
    image = models.ImageField(upload_to='products_images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
        
    def product_image(self):
        return mark_safe('<img src="%s" width="100" height="100"/>' % self.image.url)

    def get_percantage(self):
        if self.discounted_price and self.original_price:
            percentage = ((self.original_price - self.discounted_price) / self.original_price) * 100
            return round(percentage, 2)
        return 0 

class Slider(models.Model):
    image = models.ImageField(upload_to='slider_images/', null=True, blank=True)
    heading = models.CharField(max_length=200)
    

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
       return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="product")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(choices=RATING, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)
    