from django.views import View
from django.utils.decorators import method_decorator
from .models import Games
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class GamesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            games = list(Games.objects.filter(id=id).values())
            if len(games) > 0:
                game = games[0]
                datos = {'message':'Success', 'game':game}
            else:
                datos = {'message':'Game not found...'}
            return JsonResponse(datos)
        else:  
            games = list(Games.objects.values())
            if len(games) > 0:
                datos = {'message':'Success', 'games':games}
            else:
                datos = {'message':'Games not found...'}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Games.objects.create(name=jd["name"], company=jd["company"], website=jd["website"], foundation=jd["foundation"] )
        datos = {'mesagge':'succes'}
        return JsonResponse(datos)



    def put(self, request, id):
        jd=json.loads(request.body)
        games = list(Games.objects.filter(id=id).values())
        if len(games) > 0:
            game = Games.objects.get(id=id)
            game.name = jd["name"]
            game.company = jd["company"]
            game.website = jd["website"]
            game.foundation = jd["foundation"]
            game.save()
            datos = {'message':'Success'}
        else: 
            datos = {'message':'Game not found...'}
        return JsonResponse(datos)


    def delete(self, request, id):
        game = list(Games.objects.filter(id=id).values())
        if len(game) > 0:
            Games.objects.filter(id=id).delete()
            datos = {'message':'Success'}
        else:
            datos = {'message':'Game not found...'}
        return JsonResponse(datos) 