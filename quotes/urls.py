from django.urls import path
from .views import get_quote, index

urlpatterns = [
    path('', index, name='index'),  
    path('quote/', get_quote, name='get_quote'),
]
