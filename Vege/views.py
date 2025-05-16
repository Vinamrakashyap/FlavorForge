from django.shortcuts import render,redirect
from .models import Receipes
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')  # You’ll create home.html nex
def receipes(request):
    if request.method == "POST":
        data = request.POST
        
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        
        Receipes.objects.create(
            receipe_image = receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            )
        return redirect('/receipes')
    queryset = Receipes.objects.all()
    context = {"receipes" : queryset}
        
    return render(request , "receipes.html", context)

def update_receipe(request , id):
    queryset = Receipes.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        
        if receipe_image:
            queryset.receipe_image = receipe_image
        
        queryset.save()
        return redirect('/receipes')
        
    context = {"receipe" : queryset}
    return render(request , "update_receipes.html", context)

def delete_receipe(request , id):
    queryset = Receipes.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes')

def login_page(request):
    return render(request , 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.error(request, "username already exists")
            return redirect('/register/')
        
        
        user = User.objects.create(username=username, email=email, password=password)
        
        messages.error(request, "Account Created Successfully")
        
        return redirect('/register/')
        
    return render(request , 'register.html')
