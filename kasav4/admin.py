from django.contrib import admin
import nested_admin

from .models import *

class FiveInline(nested_admin.NestedStackedInline):
    model = Five
    extra = 0

class FourInline(nested_admin.NestedStackedInline):
    model = Four
    extra = 0
    inlines = [FiveInline]

class ThreeInline(nested_admin.NestedStackedInline):
    model = Three
    extra = 0
    inlines = [FourInline]

class TwoInline(nested_admin.NestedStackedInline):
    model = Two
    extra = 0
    inlines = [ThreeInline]


class CategoriesAdmin(nested_admin.NestedModelAdmin):
    inlines = [TwoInline]


admin.site.register(One, CategoriesAdmin)
admin.site.register(Two)
admin.site.register(Three)
admin.site.register(Four)
admin.site.register(Five)
admin.site.register(Currency)
admin.site.register(Transaction)