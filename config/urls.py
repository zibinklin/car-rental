"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from core.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from apps.rental.views import *

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',Base.as_view()),
    path('register',Register.as_view()),
    path('register/process',RegisterProcess.as_view()),
    
    path('login',LoginWeb.as_view()),
    path('login/process',LoginProcess.as_view()),
    path('logout',Logout.as_view()),




    #admin
    path('user_admin/',AdminKatalog.as_view()),
    path('Rent_History',CarOut.as_view()),
    path('Rent_History/car_return',CarReturn.as_view()),

    

    #include
    path('car/',include(('apps.cars.urls','cars'),namespace='car')),
    path('customers/',include(('apps.customers.urls','customers'),namespace='customers')),
    path('drivers/',include(('apps.drivers.urls','drivers'),namespace='drivers')),
    path('rental/',include(('apps.rental.urls','rental'),namespace='rental'))


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)