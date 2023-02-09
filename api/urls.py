from django.urls import path
from .views import PokemonView


urlpatterns = [
    path('pokemon/',PokemonView.getPokemones,name='lista_pokemones'),
    path('pokemon/<int:id>',PokemonView.getPokemonId,name='id_pokemon'),
]
