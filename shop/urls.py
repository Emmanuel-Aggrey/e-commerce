from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'shop'


urlpatterns = [
    path('', views.product_list, name ='product_list'),
    path('uniqpab_faqs',views.unique_faqs,name ='faq'),
    path('related/',views.allCategory,name ='category'),
    path('allrelated/<str:slug>/',views.allRelated,name ='allrelated'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    
]
