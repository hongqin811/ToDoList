from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path('index/', views.index),
	path('actions/', views.index, name='index'),
	path('member/', views.member_view, name='member_view'),
	path('register/', views.register_view, name='register_view'),
	path('member/<int:member_id>/', views.personal_view, name='personal_view' ),
	path('member/<int:member_id>/add/', views.addWork_view, name='addWork_view' ),
	path('login/', views.login_view, name='login_view'),
	path('logout/', views.logout_view, name='logout_view'),
	path('addAction/', views.addAction_view, name='addAction_view'),
	path('', views.home_view, name='home_view'),
	path('/edit/<list_id>/', views.edit_list_view, name="edit_view"),
	path('/delete/<list_id>', views.delete_view, name="delete_view"),
	path('changepw/', views.changepw_view, name="changepw_view")
]

urlpatterns += staticfiles_urlpatterns()