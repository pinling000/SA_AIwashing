"""sa_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path ,re_path
#from sa_django.sa_final.views import mode
from sa_final import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index), #首頁
    path('unlock', views.unlock), #香味解鎖
    path('map', views.map), #洗衣地圖
    path('history', views.history), #歷史紀錄
    path('detail', views.detail),#訂單詳情
    re_path(r'detail/(?P<detail_id>\d+)/$',views.detail,name='detail'),
    path('solve', views.question), #問題回報
    path('bag', views.bag), #洗衣袋紀錄
    path('order',views.orders), #確認訂單
    path('wash', views.wash), #開始洗衣
    path('preference', views.preference), #洗衣偏好
    path('setpreference', views.setpreference), #偏好設定
    path('cash', views.cash), #信用卡設定
    path('lock', views.lock_test),#鎖櫃
    path('Delivery', views.Delivery),#選擇送洗方式
    path('Uber', views.Uber),#外送
    path('login2/', views.login2_view),#LINE登入
    path('api2/', views.api2),
    path('GDPR', views.GDPR),#個資使用條款
    # path('login', views.login),#登入
    path('sms', views.sms),#手機登入
    path('payment',views.PAYPAL,name='paypal-ipn'),
    path('paypal-reverse',views.paypal_reverse,name='paypal-reverse'),
    path('paypal-cancel',views.paypal_cancel,name='paypal-cancel'),
    path('qrcode', views.qrcode),
    path('qrcode_take', views.qrcode_take),
    path('established', views.established),
    path('Uber_order', views.Uber_order),
]
