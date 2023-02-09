from django.http.response import JsonResponse
from django.views import View
from django.core.paginator import Paginator,  EmptyPage, PageNotAnInteger
from .models import Pokemon



class PokemonView(View):
    
    def getPokemones(request):
        pokemons = list(Pokemon.objects.values())
        
        paginator = Paginator(pokemons, 20) 
        page = request.GET.get('page')
        try:
            pokemons = paginator.page(page)
        except PageNotAnInteger:
            pokemons = paginator.page(1)
        except EmptyPage:
            pokemons = paginator.page(paginator.num_pages)

        lista_pokemones = list(pokemons)

        response = {
            'pagina_anterior': None,
            'pagina_siguiente': None,
            'pokemones': lista_pokemones,
        }

        if pokemons.has_previous():
            response['pagina_anterior'] = f'/api/pokemon?page={pokemons.previous_page_number()}'

        if pokemons.has_next():
            response['pagina_siguiente'] = f'/api/pokemon?page={pokemons.next_page_number()}'

        return JsonResponse(response)
    
    def getPokemonId(self,id):
        pokemon = list(Pokemon.objects.filter(id=id).values())
        if len(pokemon)>0:
            pokeid = pokemon[0]
            dato = {"resultado":pokeid}
        return JsonResponse(dato)
    
