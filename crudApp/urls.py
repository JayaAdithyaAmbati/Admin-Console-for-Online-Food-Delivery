from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('show',views.show,name='show'),
    path('insert',views.insert,name='insert'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('admin_details/<int:id>', views.admin_restaurant_details, name='admin_details'),
    path('user_details/<int:id>', views.user_restaurant_details, name='user_details'),
    path('user_search/', views.user_search, name='user_search'),
    path('admin_search/', views.admin_search, name='admin_search'),
    path('user/', views.user, name='user'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
]
 