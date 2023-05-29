from django.contrib import admin
from django.urls import path, include
from app.views import *
from app.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

