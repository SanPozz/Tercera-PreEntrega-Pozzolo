from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('App_Coder/', include('App_Coder.urls')),
]
