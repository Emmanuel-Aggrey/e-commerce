

from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.blog, name="blog"),
    path('create', views.blog_create, name="blog_create"),
    path('details/<int:id>/', views.blog_details, name="blog_detailpage"),
    path('update/<int:id>/', views.blog_update, name="blog_update"),
    path('delete/', views.blog_delete, name="blog_delete"),

]
