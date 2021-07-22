from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='blog-home'),
    path('blog/', views.myblog,name='blog-myblog'),
    path('image-to-pattern/', views.imagetopattern,name='blog-Image-to-pattern'),
    
    
]
