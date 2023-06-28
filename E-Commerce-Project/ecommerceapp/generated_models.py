# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EcommerceApp2Aisles(models.Model):
    aisle_id = models.IntegerField(primary_key=True)
    aisle = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ecommerce_app2_aisles'


class EcommerceApp2Departments(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ecommerce_app2_departments'


class EcommerceApp2Inventory(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.IntegerField()
    last_updated = models.DateTimeField()
    aisle = models.ForeignKey(EcommerceApp2Aisles, models.DO_NOTHING)
    department = models.ForeignKey(EcommerceApp2Departments, models.DO_NOTHING)
    product = models.ForeignKey('EcommerceApp2Products', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ecommerce_app2_inventory'


class EcommerceApp2Orderproducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    add_to_cart_order = models.IntegerField(blank=True, null=True)
    reordered = models.BooleanField(blank=True, null=True)
    order = models.ForeignKey('EcommerceApp2Orders', models.DO_NOTHING)
    product = models.ForeignKey('EcommerceApp2Products', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ecommerce_app2_orderproducts'


class EcommerceApp2Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    eval_set = models.CharField(max_length=255)
    order_number = models.IntegerField()
    order_dow = models.IntegerField(blank=True, null=True)
    order_hour_of_day = models.IntegerField(blank=True, null=True)
    days_since_prior_order = models.IntegerField(blank=True, null=True)
    total_price_usd = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ecommerce_app2_orders'


class EcommerceApp2Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    aisle = models.ForeignKey(EcommerceApp2Aisles, models.DO_NOTHING)
    department = models.ForeignKey(EcommerceApp2Departments, models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ecommerce_app2_products'
