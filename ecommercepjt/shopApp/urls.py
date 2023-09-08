

from . import views
from django.urls import path, include
app_name='shopApp'
urlpatterns = [
    path('', views.AllProdCat,name='AllProdCat'),
    path('<slug:c_slug>/', views.AllProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.product_details,name='product_cat_details'),

]
