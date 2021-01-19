from django.conf.urls import url
from django.contrib.auth import views as av
from . import views

app_name = 'account'

urlpatterns = [
	url(r'login/$',av.LoginView.as_view(template_name='account/login.html'),name='login'),
	url(r'logout/$',av.LogoutView.as_view(),name='logout'),
	url(r'signup/$',views.SignUp.as_view(), name='signup')
]