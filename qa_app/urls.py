from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('', views.base, name='base'),
	path('category/<int:category_id>/', views.question_list, name='question_list'),
	path('', views.feed, name='feed'),
	path('popular/', views.popular, name='popular'),
	path('recent/', views.recent, name='recent'),
	path('search/', views.search, name='search'),
	path('register/', views.register, name='register'),
	path('question/<int:id>/', views.question_detail, name='question_detail'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('login/', views.login_view, name='login'),

]
