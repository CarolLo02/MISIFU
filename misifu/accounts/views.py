from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib import messages

def home_view(request):
    return render(request, 'home.html')


def nosotros_view(request):
    return render(request, 'nosotros.html')

def contact_view(request):
    if request.method == 'POST':
        # Aquí podrías manejar el envío del formulario, por ejemplo, enviando un correo electrónico.
        # Por simplicidad, solo mostraremos un mensaje de éxito.
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        mensaje = request.POST.get('mensaje')
        
        # Aquí puedes agregar la lógica para manejar el mensaje, como enviarlo por correo electrónico.
        
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ingreso')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def ingreso_view(request):
    context = {
        'is_ingreso': True
    }
    return render(request, 'accounts/ingreso.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Usuario creado exitosamente.')
                return redirect('login')  # Redirige a la página de inicio u otra página después del registro exitoso
            else:
                messages.error(request, 'Error en la autenticación. Verifique sus credenciales e intente nuevamente.')
        else:
            messages.error(request, 'Error al crear el usuario. Verifique los datos e intente nuevamente.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

