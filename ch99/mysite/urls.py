"""mysite URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from mysite.views import HomeView
from mysite.views import UserCreateView, UserCreateDoneTV
from phone.views import PhoneLV, PhoneDV
from namecard.views import NamecardLV, NamecardDV
from student.views import StudentLV, StudentDV


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),

    path('', HomeView.as_view(), name='home'),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('phone/', include('phone.urls')),
    path('namecard/', include('namecard.urls')),
    path('student/', include('student.urls')),
    path('photo/', include('photo.urls')),

    # class-based views
    path('phone/', PhoneLV.as_view(), name='phoneindex'),
    path('phone/<int:pk>/', PhoneDV.as_view(), name='phonedetail'),
    path('namecard/', NamecardLV.as_view(), name='namecardindex'),
    path('namecard/<int:pk>/', NamecardDV.as_view(), name='namecarddetail'),
    path('student/', StudentLV.as_view(), name='studentindex'),
    path('student/<int:pk>/', StudentDV.as_view(), name='studentdetail'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
