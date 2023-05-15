"""backend URL Configuration

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
from django.urls import path
from django.conf.urls.static import static
from django.urls import include, re_path
from django.views.static import serve

from backend import settings
from backendapi.views import NewsApiView, PinsApiView, DocumentsApiView, BenefitsApiView, StudentsContactsApiView, \
    TeachersContactsApiView, DocumentApiView, NewApiView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/newslist/', NewsApiView.as_view()),
    path('api/newslist/<int:pk>/', NewApiView.as_view()),

    path('api/pinslist/', PinsApiView.as_view()),

    path('api/documentslist/', DocumentsApiView.as_view()),
    path('api/documentslist/<int:pk>/', DocumentApiView.as_view()),

    path('api/benefitslist/', BenefitsApiView.as_view()),

    path('api/studentscontactslist/', StudentsContactsApiView.as_view()),

    path('api/teacherscontactslist/', TeachersContactsApiView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
