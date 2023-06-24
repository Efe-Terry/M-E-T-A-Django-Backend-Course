from django.shortcuts import render
from django.http import HttpResponse 

def home(request):
    content = "Hello From Little Lemon Resturant"
    return HttpResponse(content)

def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.")

def pathview(request, name, id, cnt): 
    #return HttpResponse("Name:{} UserID:{}".format(name, id))
    return HttpResponse(f"Name is: {name} UserID is: {id} Location: {cnt}")

def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id))  

def showform(request): 
    return render(request, "form.html")

def getform(request):
    if request.method == "POST": 
        id = request.POST['id'] 
        name = request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id))

def coffe(request, name):
    items = {
        'capoccini': 'Italiam Drink',
        'agbo': 'Nigerian Herbs'
    }
    des = items[name]
    return HttpResponse(f"<h1>{name}</h1>" + des)