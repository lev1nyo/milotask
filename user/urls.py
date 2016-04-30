from django.conf.urls import url
from user import views


urlpatterns = [
    url(r'^$', views.user_list, name='user_list'),
    url(r'^view/(?P<user_id>[0-9]*)/$', views.user_view, name='user_view'),
    url(r'^edit/(?P<user_id>[0-9]*)/$', views.user_edit, name='user_edit'),
    url(r'^delete/(?P<user_id>[0-9]*)/$', views.user_delete, name='user_delete'),
]
