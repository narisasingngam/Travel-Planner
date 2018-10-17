from django.shortcuts import render
from django.http import HttpResponse
from .models import SearchMap

def index(request):
     if request.method == 'POST':
            if request.POST.get('location') and request.POST.get('time'):
                post= SearchMap()
                post.location= request.POST.get('location')
                post.time= request.POST.get('time')
                post.save()
                
                return render(request, 'index.html')  
     else:
        return render(request,'index.html')
