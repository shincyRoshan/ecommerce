from . import views
from django.urls import path, include
app_name='cart_app'
urlpatterns = [
    path('add/<int:product_id>/', views.addCart, name='addCart'),
    path('', views.cart_details,name='cart_details'),
    path('remove/<int:product_id>/', views.CartRemove,name='CartRemove'),
    path('full_remove/<int:product_id>/', views.full_remove,name='full_remove'),

]
