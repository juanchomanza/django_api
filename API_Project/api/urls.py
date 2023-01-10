from django.urls import path
from .views import GamesView

urlpatterns = [
    path('games/', GamesView.as_view(), name='games_list'),
    path('games/<int:id>', GamesView.as_view(), name='game'),
    
]
