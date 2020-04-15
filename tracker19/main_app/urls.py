from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('entry/', views.entry_index, name='entry_index'),
  # path('entry/date/', views.date_entry,name='date_entry'),
  path('entry/<int:entry_id>/', views.entry_detail, name='detail'),
  path('entry/create/', views.FormCreate.as_view(), name='form_create'),
  path('entry/<int:pk>/update/', views.EntryUpdate.as_view(), name='entry_update'),
  path('entry/<int:pk>/delete/', views.EntryDelete.as_view(), name='entry_delete'),
]