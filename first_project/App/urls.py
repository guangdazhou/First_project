from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    # url(r'^logout/$', views.logout, name='logout'),
    url(r'^shoppingbag/$', views.shoppingbag, name='shoppingbag'),
]
