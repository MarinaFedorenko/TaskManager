from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('next', views.next, name="next"),
    path('previous', views.previous, name="previous"),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete")
]
