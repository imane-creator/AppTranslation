
from django.contrib import admin
from .views import translator
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", translator),
]
