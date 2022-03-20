# 总路由
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  # 后端
    path('', include("Glasneaker.urls")),  # 前端 在当前的总路由文件中导入子路由文件，方便管理
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
