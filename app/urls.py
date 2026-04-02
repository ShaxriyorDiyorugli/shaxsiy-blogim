from django.urls import path
from .views import index, blog, about

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
]