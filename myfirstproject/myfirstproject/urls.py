from django.contrib import admin
from django.urls import path,include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('day2app.urls')),
    path('day3app/', include('day3app.urls')),
    path('day4app/', include('day4app.urls')),
    
]
