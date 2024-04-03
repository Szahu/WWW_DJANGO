from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/profile/', views.logged_in, name='logged_in'),
    path('logout/', views.logout_view, name='logout_view'),
    path('pic/<int:pic_id>/', views.pic_view, name='pic_view'),
    path('pic_clear/<int:pic_id>/', views.pic_clear, name='pic_clear'),
    path('pic_add_rect/<int:pic_id>/', views.pic_add_rect, name='pic_add_rect'),
]