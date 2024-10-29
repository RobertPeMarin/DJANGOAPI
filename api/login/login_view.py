from django.shortcuts import render

# Create your views here.
def login_view(request):
    template_name = "authentication-login.html"
    return render(request,template_name)

# crear vista registro
def register_view(request):
    template_name = "authentication-register.html"
    return render(request,template_name)

# crear vista recuperar contraseña
def forgotPass_view(request):
    template_name = "auth-forgot-password.html"
    return render(request,template_name)
    