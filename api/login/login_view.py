from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def login_view(request):
    template_name = "authentication-login.html"

    if request.user.is_authenticated and request.user.is_active:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciales invalidas o usuario no activo')
    return render(request,template_name)

# crear vista registro
def register_view(request):
    template_name = "authentication-register.html"
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, template_name)
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
            return render(request,template_name)
        
        user = User(
            username = username,
            email = email,
            password = make_password(password),
            is_active = 0
        )
        user.save()
        messages.success(request, 'Cuenta creada exitosamente')

    return render(request,template_name)

# crear vista recuperar contraseña
def forgotPass_view(request):
    template_name = "auth-forgot-password.html"
    return render(request,template_name)

def logout_view(request):
    logout(request)
    return redirect('login_vista')    