
# 总路由
from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    path('', include("Glasneaker.urls")),  # 在当前的总路由文件中导入子路由文件，方便管理
    path('login/', include("Glasneaker.urls")),
    path('register/', include("Glasneaker.urls")),
    path('admin/', admin.site.urls),
]
