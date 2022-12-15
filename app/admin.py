from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Buyer)
admin.site.register(Marketer)
admin.site.register(Product)
admin.site.register(BuyerProduct)
admin.site.register(MarketerProduct)