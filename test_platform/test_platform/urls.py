from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user_app.urls',namespace="user_app")),
    path('manage/',include('project_app.urls',namespace="project_app")),
]
