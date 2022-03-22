from unicodedata import name
from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('brands/',views.brands,name='brands'),
    path('attributes/',views.attributes,name='attributes'),
    path('category/',views.category,name='category'),
    path('reports/',views.reports,name='reports'),
    path('stores/',views.stores,name='stores'),
    path('groups/',views.groups,name='groups'),
    path('register/',views.reg,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),


]