from django.contrib import admin
import nested_admin

from .models import *

class FourInline(nested_admin.NestedStackedInline):
    model = Four
    extra = 0

class ThreeInline(nested_admin.NestedStackedInline):
    model = Three
    extra = 0
    inlines = [FourInline]

class TwoInline(nested_admin.NestedStackedInline):
    model = Two
    extra = 0
    inlines = [ThreeInline]

class OneInline(nested_admin.NestedStackedInline):
    model = One
    extra = 0
    inlines = [TwoInline]

class CategoriesAdmin(nested_admin.NestedModelAdmin):
    inlines = [OneInline]


admin.site.register(TransactionType, CategoriesAdmin)
admin.site.register(Currency)
admin.site.register(Transaction)
admin.site.register(Bank)