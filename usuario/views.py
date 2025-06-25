from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
def login_view(request):
    return render(request,'login.html',{})
def registro_view(request):

    if request.method == 'GET':
        print("enviando formulario")
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],
                                    password=request.POST['password1'],)
            user.save()
        return HttpResponse('COntraseña no coinciden')
    


    return render(request,'registro.html',{
    'form': UserCreationForm()
    })