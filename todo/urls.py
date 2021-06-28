from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall'),
    url(r'^register/$',views.register,name='register'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'user_login/$',views.user_login,name='user_login'),
    url(r'export/$',views.export,name='export'),
]
