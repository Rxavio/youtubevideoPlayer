from django.shortcuts import render
from .models import Item


def video(request):
    obj= Item.objects.all()
    context= {'obj': obj,
            
            }
        
      
    return render(request, 'player_app/videos.html', context)