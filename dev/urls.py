from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^register$', views.AddUser.as_view(), name='add-user'),
    url(r'^login$', views.UserLogin.as_view(), name='login-user'),
    url(r'^addproject$', views.AddProject.as_view(), name='add-project'),
    url(r'^logout$', views.logout_user, name='logout'),
    url(r'^delete/(?P<pk>[0-9]+)$', views.ProjectDelete.as_view(), name='project-delete'),
    url(r'^(?P<pk>[0-9]+)$', views.ViewUser.as_view(), name='user-detail')
]
