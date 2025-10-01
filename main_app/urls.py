from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('calendar', views.calendar_view, name='calendar'),
    path('calendar/<int:year>/<int:month>/', views.calendar_view, name='calendar')
]
