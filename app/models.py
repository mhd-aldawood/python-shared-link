from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Create your models here.
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # username = models.CharField(max_length=50, unique=True)
    # USERNAME_FIELD = 'username'

    class Meta:
        abstract = True


# this is the user
class Buyer(BaseModel, AbstractUser):
    balance = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return super().__str__()


class Marketer(BaseModel):
    uu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, default='M', null=True, choices=GENDER_CHOICES)
    percentage_in_marketing = models.IntegerField(default=0, null=False)
    minimum_to_receive = models.IntegerField(default=0, null=False)
    username = models.CharField(max_length=50, default='', null=False, blank=False)

    def __str__(self):
        return super().__str__()


class Product(models.Model):
    name = models.CharField(max_length=255, default='', null=False)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return super().__str__()


class BuyerProduct(models.Model):
    buyer = models.ForeignKey(Buyer, related_name='BuyerProduct', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='BuyerProduct', on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()



class MarketerProduct(models.Model):
    marketer = models.ForeignKey(Marketer, related_name='Marketers', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='Products', on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()

#
# class CustomUser(AbstractUser):
#     uu_id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4,
#         editable=False)
#     total_used = models.IntegerField(default=0, null=False)
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     gender = models.CharField(max_length=1, default='M', choices=GENDER_CHOICES)
#     product = models.CharField(max_length=50, blank=True, null=False)
#     percentage_in_marketing = models.IntegerField(default=0, null=False)
#     minimum_to_receive = models.IntegerField(default=0, null=False)
#
#     def __str__(self):
#         return self.username
