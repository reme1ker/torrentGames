from django.urls import path
from backend.core import views
from backend.core.api import GamesDV
from backend.users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('category/<int:category_id>/', views.index, name='category'),
    path('filtered/<int:filtered>/', views.index, name='filtered'),
    path('game/<int:pk>/', views.game_detail, name='game_detail'),
    path('reviews/<int:pk>/', views.add_review, name='add_review'),
    path('games/api/', GamesDV.as_view(), name='games'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('baskets/add/<int:game_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
    path('order/add/<int:total>/', views.order_add, name='order_add'),
    path('orderpdf/<int:order_id>/', views.orderpdf, name='orderpdf'),
]
