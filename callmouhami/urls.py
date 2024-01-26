
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/', include('api.urls')),
    path('', include('lawyer.urls')),
    path('', include('user.urls')),


]
