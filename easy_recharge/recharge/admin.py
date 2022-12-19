from django.contrib import admin

# Register your models here.
from .models import Plan, RechagreHistory

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('validity', 'data', 'price',)

@admin.register(RechagreHistory)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('mobile_number', 'created_at',)