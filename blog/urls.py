from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='blog-home'),
    path('blog/', views.myblog,name='blog-myblog'),
    path('about/', views.about,name='blog-about'),
    path('photography/', views.photography,name='blog-photography'),
    path('image-to-pattern/', views.imagetopattern,name='blog-Image-to-pattern'),
    
    
]
