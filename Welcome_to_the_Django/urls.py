"""Welcome_to_the_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from website.API import viewset as API_viewset

from . import views

route = routers.DefaultRouter()
route.register('api', API_viewset.AlgumaCoisaViewSet, basename='algumacoisa')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls'), name='index'),
    path('', include(route.urls))
]
