from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # ✅ Homepage for tasks
    path('create/', views.task_create, name='task_create'),  # ✅ Create task
    path('<int:task_id>/update/', views.task_update, name='task_update'),  # ✅ Update task
    path('<int:task_id>/delete/', views.task_delete, name='task_delete'),  # ✅ Delete task
]
