from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate,DeleteView,CustomloginView,Registerpage,TaskRecorder
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse


def custom_logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
 
urlpatterns = [
  path('logout/', custom_logout_view, name='logout'),
  path('login/', CustomloginView.as_view(), name='login'),  
  path('register/', Registerpage.as_view(), name='register'),  

   
  path('',TaskList.as_view(),name='tasks'),
  path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
  path('create-task/',TaskCreate.as_view(),name='task-create'),
  path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
  path('task-delete/<int:pk>/',DeleteView.as_view(),name='task-delete'),
  path('task-recorder/', TaskRecorder.as_view(), name='task-recorder'),




]