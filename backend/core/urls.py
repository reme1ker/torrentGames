from django.urls import path
from backend.core import views
from backend.core.api import GamesDV
from backend.core.views import GameDetailView
from backend.users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('game/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
    path('games/api/', GamesDV.as_view(), name='games'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path("review/", views.ReviewCreateView.as_view()),
    path("review/<int:pk>/", GameDetailView.as_view()),
    path('card/', views.card),
]
