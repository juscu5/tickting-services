from django.urls import path
from . import views

urlpatterns = [ 
    path('get/', views.GetUser),
    path('add/<str:username>&<str:password>', views.AddUser),
    path('edit/<int:user_id>&<str:username>&<str:password>', views.EditUser),
    path('delete/<int:user_id>', views.DeleteUser)
]