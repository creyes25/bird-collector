from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path("birds/", views.birds_index, name="birds_index"),
    path('birds/<int:bird_id>/', views.birds_details, name='birds_details'),
    path('birds/create/' , views.BirdCreate.as_view(), name='birds_create'),
    path('birds/<int:pk>/update', views.BirdUpdate.as_view(), name='birds_update'),
    path('birds/<int:pk>/delete', views.BirdDelete.as_view(), name='birds_delete'),
    # feeding
    path('birds/<int:bird_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    #care
    path('cares/create', views.CareCreate.as_view(), name='cares_create'),
    path('cares/', views.CareList.as_view(), name='cares_index'),
    path('cares/<int:pk>/', views.CareDetail.as_view(), name='care_details'),
    path('cares/<int:pk>/update/', views.CareUpdate.as_view(), name='cares_update'),
    path('cares/<int:pk>/delete/', views.CareDelete.as_view(), name='cares_delete'),
    path('birds/<int:bird_id>/assoc_care/<int:care_id>/', views.assoc_care, name='assoc_care'),
    # signup
    path('accounts/signup/', views.signup, name='signup'),
]