from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    url(r'^signup$', views.SignUp.as_view(), name='signup'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'login.html', 'next_page': 'login'},
        name='logout'),
]
