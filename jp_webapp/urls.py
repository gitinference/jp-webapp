from tkinter.font import names
from django.contrib import admin
from django.urls import path
from django.urls import include
from web_app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_app.urls')),
]
