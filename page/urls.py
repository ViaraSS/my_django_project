from django.urls import path
from .views import homePageView, home_view

urlpatterns = [
    path('', homePageView, name='home'),
    path('', home_view, name='home'),
]
