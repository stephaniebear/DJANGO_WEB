"""DJANGO_PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from blogs import views

from django.conf import settings #BOOK FILES
from django.conf.urls.static import static #BOOK FILES

urlpatterns = [
    path('',views.result),
    path('account/', views.formAccount),
    path('admin/', admin.site.urls),
    path('page1/',views.Page1),
    path('formAddResult/',views.formAddResult),
    path('addResult/',views.addResult),
    path('resultForm/',views.result),
    path('createForm/',views.createForm),
    path('addForm/',views.addUser),
    path('loginForm/',views.loginForm),
    path('login/',views.login),
    path('logout/',views.logout),
    path('deleteResult/',views.deleteResult),
    path('editResult/',views.editResult),
    path('formEditResult/',views.formEditResult),
    path('office/',views.office),
    path('likePost/',views.likePost),
    path('getProvinceName/',views.getProvinceName),
    path('getOfficeType/',views.getOfficeType),

    path('getFiles/',views.getFiles),
    path('getResult/',views.getResult),

    path('formAddCheckList/',views.formAddCheckList),
    path('formCheckList/',views.formCheckList),

    #---------- Asset ----------
    path('formAddAsset/',views.formAddAsset),
    path('formAddLocation/',views.formAddLocation),
    path('formAddAssetType/',views.formAddAssetType),
]

#BOOK FILES
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)