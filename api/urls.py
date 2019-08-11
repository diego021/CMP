from django.urls import path
from api import views

namespace = 'api'
urlpatterns = [
    path('search/', views.search, name='search'),
]
