from django.db import models

# Create your models here.

STATUS_CHOICE = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

STOCK_CHOICE = (
    ('In Stock', 'In Stock'),
    ('Out of Stock', 'Out of Stock'),
)


class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True,
                              upload_to="img/Categories/")
    available = models.CharField(
        default='yes', choices=STATUS_CHOICE, max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    old_price = models.DecimalField(
        max_length=1000, decimal_places=2, max_digits=6)
    new_price = models.DecimalField(
        max_length=1000, decimal_places=2, max_digits=6)
    stock = models.CharField(
        default='In Stock', choices=STOCK_CHOICE, max_length=20)
    image = models.ImageField(blank=True, null=True, upload_to='img/Products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
