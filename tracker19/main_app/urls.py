from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('health/create/', views.HealthCreate.as_view(), name='health_create'),
  path('health/<int:pk>/update/', views.HealthUpdate.as_view(), name='health_update'),
  path('health/', views.health_index, name='health_index'),
   path('health/<int:health_id>/', views.health_detail, name='health_detail'),





  path('health/anonymous/', views.anonymous, name='anonymous'),
  



  path('entry/', views.entry_index, name='entry_index'),
  # path('entry/date/', views.date_entry,name='date_entry'),
  path('entry/<int:entry_id>/', views.entry_detail, name='detail'),
  path('entry/create/', views.FormCreate.as_view(), name='form_create'),
  path('entry/<int:pk>/update/', views.EntryUpdate.as_view(), name='entry_update'),
  path('entry/<int:pk>/delete/', views.EntryDelete.as_view(), name='entry_delete'),
]