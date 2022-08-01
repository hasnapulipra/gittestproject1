from django.urls import path
from . import views
urlpatterns=[
    path('funnew',views.fun1,name="fun")
]