from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.GetTicket),
    path('add/<str:ticket_name>&<str:ticket_desc>', views.AddTicket),
    path('add-custom/', views.RawSQLGet),
]