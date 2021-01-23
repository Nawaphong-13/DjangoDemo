from django.urls import path
from .views import HomePage, AboutPage

urlpatterns = [
    # localhost:8000/
    path('', HomePage, name='home-page'),
    path('about/', AboutPage, name='about-page')
]