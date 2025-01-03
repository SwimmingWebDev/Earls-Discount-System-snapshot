"""
URL configuration for Earls_Discount_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def google_login_redirect(request):
    return redirect('/accounts/google/login/?process=login')

# Logout View
def logout_view(request):
    logout(request)  # Clears session and logs out user
    return HttpResponseRedirect('/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),  # For login routes
    path('employee/', include('employee.urls')),  # For employee-related routes
    path('admin_panel/', include('site_admin.urls')),  # For admin panel routes
    path('accounts/', include('allauth.urls')),  # Handles allauth including social accounts
    path('site_admin/', include('site_admin.urls')), 
    path('google-login/', google_login_redirect, name='google-login'),
    path('logout/', logout_view, name='logout'),
]
