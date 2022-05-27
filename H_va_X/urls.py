from django.contrib import admin
from django.urls import path

from App.views import Result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Result, name="home"),
]
