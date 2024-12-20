from django.urls import path

from todoapp import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.add, name='home'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/',views.update, name='update'),
    path('cbvhome/', views.TaskListView.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.Taskdetailsview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='cbvdelete'),
]
