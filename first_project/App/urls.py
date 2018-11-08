from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$',views.index,name='Homepage'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^Men/$',views.Men,name='Men'),
    url(r'^shoppingbag/$', views.shoppingbag, name='shoppingbag'),
    url(r'^GoodsDetails/$', views.GoodsDetails, name='GoodsDetails'),



]
