"""ratatoskr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    # This is probably not the best idea ever.
    # path('accounts/', include('allauth.urls')), 
    # Effectively only import the urls needed to do google auth
    path('accounts/', include('allauth.socialaccount.providers.google.urls')),
    path('logout', LogoutView.as_view(), name="logout"),
    path('tinymce/', include('tinymce.urls')),
]

handler404 = 'app.errors.error404'
handler400 = 'app.errors.error400'
handler403 = 'app.errors.error403'
handler500 = 'app.errors.error500'
