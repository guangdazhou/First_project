from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$',views.index,name='Homepage'),# 首页
    url(r'^register/$', views.register, name='register'), # 注册
    url(r'^login/$', views.login, name='login'), # 登录
    url(r'^logout/$', views.logout, name='logout'), # 退出
    url(r'^Men/$',views.Men,name='Men'),# 商品部分展示，点击图片获取详细信息
    url(r'^shoppingbag/$', views.shoppingbag, name='shoppingbag'), # 没完成 购物袋
    url(r'^GoodsDetails/(\w+)/$', views.GoodsDetails, name='GoodsDetails'),# 商品详细信息展示页面
    # url(r'^showgoods/(\w+)/$',views.showgoods,name='showgoods'),# 点击得到的商品详情页面，自己创建的

]
