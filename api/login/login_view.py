from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_view(request):
    template_name = "authentication-login.html"

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, template_name, {'error': 'credenciales invalidas'})
    return render(request,template_name)

# crear vista registro
def register_view(request):
    template_name = "authentication-register.html"
    return render(request,template_name)

# crear vista recuperar contraseña
def forgotPass_view(request):
    template_name = "auth-forgot-password.html"
    return render(request,template_name)

def logout_view(request):
    logout(request)
    return redirect('login_vista')    