from django.urls import path
from project_app.views import project_views,module_views

app_name = 'project_app'
urlpatterns = [
    #项目管理
    path('project_manage/',project_views.project_manage,name="project_manage"),
    path('add_project/',project_views.add_project,name="add_project"),
    path('edit_project/<int:pid>/',project_views.edit_project,name="edit_project"),
    path('delete_project/<int:pid>/',project_views.delete_project,name="delete_project"),

    #模块管理
    path('module_manage/',module_views.module_manage,name="module_manage"),
    path('add_module/',module_views.add_module,name="add_module"),
    path('edit_module/<int:mid>/',module_views.edit_module,name="edit_module"),
    path('delete_module/<int:mid>/',module_views.delete_module,name="delete_module"),
]