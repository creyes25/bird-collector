from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("birds/", views.birds_index, name="birds_index"),
    path('birds/<int:bird_id>/', views.birds_details, name='birds_details'),
    path('birds/create/' , views.BirdCreate.as_view(), name='birds_create'),
    path('birds/<int:pk>/update', views.BirdUpdate.as_view(), name='birds_update'),
    path('birds/<int:pk>/delete', views.BirdDelete.as_view(), name='birds_delete'),
    # feeding
    path('birds/<int:bird_id>/add_feeding/', views.add_feeding, name='add_feeding')
]