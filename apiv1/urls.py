from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('blacklist', views.BlackUrlViewSet)  # ここはapiv1/の後ろのやつがblacklist/になる。

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
]
