from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Restaurant, Signup
from .forms import Restaurantform, Regform
from django.contrib.auth.models import User
def insert(request):
    if request.method == 'POST':
        form = Restaurantform(request.POST,request.FILES)  # Pass request.FILES for file uploads
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        # Provide initial data for the form fields
        initial_data = {
            'restaurant_name': '',
            'food_name': '',
            'place': '',
        }
        form = Restaurantform(initial=initial_data)

    return render(request, 'insert.html', {'form': form})
def show(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'show.html', {'restaurants': restaurants})

def delete(request, id):
    restaurant = Restaurant.objects.get(id=id)
    restaurant.delete()
    return redirect('show')

def update(request, id):
    restaurant = Restaurant.objects.get(id=id)
    if request.method == 'POST':
        form = Restaurantform(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = Restaurantform(instance=restaurant)
    return render(request, 'update.html', {'form': form, 'restaurant': restaurant})

def admin_restaurant_details(request, id):
    restaurant = Restaurant.objects.get( id=id)
    return render(request, 'admin_details.html', {'restaurant': restaurant})

def user_restaurant_details(request, id):
    restaurant = Restaurant.objects.get( id=id)
    return render(request, 'user_details.html', {'restaurant': restaurant})

def user_search(request):
    if request.method=="POST":
        search = request.POST['search']
        searched = Restaurant.objects.filter(restaurant_name__startswith = search)

        return render(request,'user_search.html',{'search':search, 'searched':searched})
    else:
        return render(request,'user_search.html',{})

def admin_search(request):
    if request.method=="POST":
        search = request.POST['search']
        searched = Restaurant.objects.filter(restaurant_name__startswith = search)

        return render(request,'admin_search.html',{'search':search, 'searched':searched})
    else:
        return render(request,'admin_search.html',{})
    
def login(request):
    if request.method == "POST":
        z=request.POST['id']
        a=request.POST['pswd']
        
        for i in range(len(Signup.objects.all().values('Rid'))):
            if (z == Signup.objects.all().values('Rid')[i]['Rid'] and a == Signup.objects.all().values('Rpswd')[i]['Rpswd']):
                print('inner if enetred')
                return HttpResponseRedirect('/show')
        return render(request, 'Login.html', {'failed': 'Admin Authentication failed'})
    return render(request, 'Login.html',{'form': Signup})

def register(request):
    if request.method == "POST":
        form = Regform(request.POST)
        z=request.POST['Rid']
        a=request.POST['Rpswd']
        
        if form.is_valid():
            for i in range(len(Signup.objects.all().values('Rid'))):
                if (z == Signup.objects.all().values('Rid')[i]['Rid'] or a == Signup.objects.all().values('Rpswd')[i]['Rpswd']):
                    return render(request, 'Register.html', {'failed': 'User exists already'})
            form.save()
            return redirect('/show')
    else:
        # Provide initial data for the form fields
        initial_data = {
            'Rid': '',
            'Rpswd': '',
        }
        form = Regform(initial=initial_data)
    return render(request,'Register.html', {'form': Signup})


def user(request):
    restaurants = Restaurant.objects.all()
    return render(request,'user.html', {'restaurants': restaurants})