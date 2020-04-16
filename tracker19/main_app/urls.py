from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('entry/', views.entry_index, name='entry_index'),
  path('entry/<int:entry_id>/', views.entry_detail, name='detail'),
  path('entry/create/', views.FormCreate.as_view(), name='form_create'),
  path('entry/<int:entry_id>/assoc_partner/<int:partner_id>/', views.assoc_partner, name='assoc_partner'),
  path('entry/<int:entry_id>/unassoc_partner/<int:partner_id>/', views.unassoc_partner, name='unassoc_partner'),
  path('entry/<int:pk>/update/', views.EntryUpdate.as_view(), name='entry_update'),
  path('entry/<int:pk>/delete/', views.EntryDelete.as_view(), name='entry_delete'),

  # Pick a Location with an Entry(M:M)
  path('entry/<int:entry_id>/picked_location/<int:location_id>/', views.picked_location, name='picked_location'),
  # Unpick a location 
  path('entry/<int:entry_id>/location_unpicked/<int:location_id>/', views.unpicked_location, name='location_unpicked'),
  path('location/', views.LocationList.as_view(), name='location_index'),
  path('location/<int:pk>/', views.LocationDetail.as_view(), name='location_detail'),
  path('location/create/', views.LocationCreate.as_view(), name='location_create'),
  
  path('location/<int:pk>/update/', views.LocationUpdate.as_view(), name='location_update'),
  path('location/<int:pk>/delete/', views.LocationDelete.as_view(), name='location_delete'),


]



#  path('entry/<int:entry_id>/add_partner/', views.add_partner, name='add_partner'),