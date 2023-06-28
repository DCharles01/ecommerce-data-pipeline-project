from django.db import models

# Create your models here.



class Aisles(models.Model):
    aisle_id = models.IntegerField(primary_key=True)
    aisle = models.CharField(max_length=255)

class Departments(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=255)

class Products(models.Model):
    # use IntegerField when you want to incrememnt field automatically
    # product_id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    aisle = models.ForeignKey('Aisles', on_delete=models.CASCADE) # models.cascade means when object is deleted, all other objects that are related to this object will be deleted
    department = models.ForeignKey('Departments', on_delete=models.CASCADE)
    # build webscraper to get product price on instacart TODO: put product name in search bar, if first result matches our query then scrape the price, if not, check next product
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    eval_set = models.CharField(max_length=255)
    order_number = models.IntegerField()
    order_dow = models.IntegerField(null=True, blank=True)
    order_hour_of_day = models.IntegerField(null=True, blank=True)
    days_since_prior_order = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=1, default=0.0)
    total_price_usd = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

class OrderProducts(models.Model):
    order = models.ForeignKey('Orders', on_delete=models.CASCADE)
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    add_to_cart_order = models.IntegerField(null=True, blank=True)
    reordered = models.BooleanField(null=True, blank=True)

    class Meta:
        unique_together = (('order', 'product'),)

class Inventory(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    aisle = models.ForeignKey('Aisles', on_delete=models.CASCADE)
    department = models.ForeignKey('Departments', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField()

    class Meta:
        unique_together = (('product', 'aisle', 'department'),)