
# 总路由
from django.urls import path,include


urlpatterns = [
    path('', include("Glasneaker.urls")),  # 在当前的总路由文件中导入子路由文件，方便管理
    path('login/', include("Glasneaker.urls")),
    path('register/', include("Glasneaker.urls")),
    path('airjordan/', include("Glasneaker.urls")),
    path('yeezy/', include("Glasneaker.urls")),
    path('detail/', include("Glasneaker.urls")),
    path('order/', include("Glasneaker.urls")),
    path('finished/', include("Glasneaker.urls")),
    path('cart/', include("Glasneaker.urls")),
]
