from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('doglist/', views.DogList.as_view(), name="dog_list"),
    path('doglist/new', views.DogCreate.as_view(), name="dog_create"),
    path('doglist/<int:pk>/', views.DogDetail.as_view(), name="dog_detail"),
    path('doglist/<int:pk>/update', views.DogUpdate.as_view(), name="dog_update"),
    path('doglist/<int:pk>/delete', views.DogDelete.as_view(), name="dog_delete"),
]