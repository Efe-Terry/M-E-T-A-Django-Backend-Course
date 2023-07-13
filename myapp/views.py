from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader 

from myapp.forms import InputForm

def home(request):
    content = "Hello From Little Lemon Resturant"
    return HttpResponse(content)

def index(request): 
    template = loader.get_template('form.html') 
    context={}  
    return HttpResponse(template.render(context, request)) 

def indexx(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content)

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

def food(request, n, name):
    item = [
        {
        'burger':'meat and bread',
        'Garri':'cassava flakes',
        'boli':'roasted plantain'
        },
        {
        'burger':'meat and bread',
        'Garri':'cassava flakes',
        'boli':'roasted plantain'
        }
    ]
    des = item[n][name]

    return HttpResponse(f'<h1>FOOD</h1><br/><h3>{item[n]}</h3><br/><p>Position: {n} - Name of food:{name}</p>' + f'Discription: {des}')

def form_view(request):
    form = InputForm()
    context = {"form": form}
    return render(request, "form_little_leamon.html", context)