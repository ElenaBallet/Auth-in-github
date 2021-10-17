from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views as integers_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'home.html'), name = 'home'),
    path('social-auth/', include('social_django.urls', namespace='social')),
         # Login and Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    path('settings/', integers_views.SettingsView.as_view(), name='settings'),
    path('settings/password/', integers_views.password, name='password'),
 
]