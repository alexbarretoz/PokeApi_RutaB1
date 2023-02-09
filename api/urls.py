from django.urls import path
from .views import PokemonView


urlpatterns = [
    path('pokemon/',PokemonView.getPokemones,name='lista_pokemones'),
]
