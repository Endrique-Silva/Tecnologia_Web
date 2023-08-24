from django.contrib import admin
from django.urls import path
from app_cad_filmes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('filmes/',views.filmes,name='listagem_filmes'),
]
