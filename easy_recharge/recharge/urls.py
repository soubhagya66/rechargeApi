
from django.urls import path
from .import views
app_name='store'

urlpatterns=[
    path('', views.allPlans, name='allPlans'),
    path('recharge/', views.recharge, name='rechageplan'),    
    path('recharge/history/', views.rechargeHistory)  
]

# https://documenter.getpostman.com/view/24991538/2s8YzZQzfS