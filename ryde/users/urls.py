from django.urls import path

from .views import UsersView, ListUsersView

urlpatterns = [
    path('', ListUsersView.as_view(), name='all_users'),
    path('<str:id>/', UsersView.as_view(), name='users')
]