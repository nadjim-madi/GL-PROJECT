from django.urls import path,include
from . import views

urlpatterns = [
    path('alllawyers', views.get_all_lawyers),
    path('lawyer/<int:lawyer_id>/', views.get_lawyer_by_id, name='get_lawyer_by_id'),
    path('appointments/<int:lawyer_id>/', views.get_appointments_by_lawyer, name='get_appointments_by_lawyer'),
    path('search_lawyers/', views.search_lawyers, name='search_lawyers'),

]
