from django.urls import path
from .views import index, blog, about, category_detail, post_detail, projects_list, project_detail

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('category/<int:pk>/', category_detail, name='category_detail'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('projects/', projects_list, name='projects'),
    path('projects/<int:pk>/', project_detail, name='project_detail'),
]