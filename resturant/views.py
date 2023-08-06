from django.shortcuts import render

# Create your views here for menu.
def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request, "about.html", {'content': about_content})
    #this concept uses a dict inside a dict

def menu(request):
    menu_itemns = ['yam', 'amala', 'rice', 'beans', 'garri']
    return render(request, "menu.html", {'items': menu_itemns})

def name(request):
    person = {'first_name': 'Itiola', 'last_name': 'Terry' , 'number' : 'Canada'}
    return render(request, "menu.html", {'hr': person})

def index(request):
    check = {'user' : 'admin'}
    return render(request, "menu.html", check)