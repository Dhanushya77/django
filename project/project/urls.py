"""
URL configuration for project project.

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
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.fun1),
    path('fun2/<int:year>/<int:salary>',views.fun2),
    path('fun3/<int:digit>',views.fun3),
    path('fun4/<int:unit>',views.fun4),
    path('fun5/<city>',views.fun5),
    path('fun6/<int:no>',views.fun6),
    path('fun7/<int:cp>',views.fun7),
    path('fun8/',views.fun8),
    path('add_std',views.add_std),
    path('edit/<id>',views.edit_std),
    path('delete/<id>',views.delete_std),
    
]
