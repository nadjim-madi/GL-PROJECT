from django.urls import path,include
from . import views

urlpatterns = [
    path('alllawyers', views.get_all_lawyers),
    path('lawyer/<int:lawyer_id>/', views.get_lawyer_by_id, name='get_lawyer_by_id'),

]