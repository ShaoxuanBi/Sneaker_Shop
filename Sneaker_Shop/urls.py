
# 总路由
from django.urls import path,include


urlpatterns = [
    path('', include("Glasneaker.urls")),  # 在当前的总路由文件中导入子路由文件，方便管理
    path('register/', include("Glasneaker.urls")),
]
