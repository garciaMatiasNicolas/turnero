from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from .forms import ShiftForm

# SHIFTS METHODS #
class Shift():
    def home(request):
        # If user is logged in then...
        if request.user.is_authenticated:
            # Render home
            return render(request, 'home.html', {
                'form': ShiftForm
            })
        else:
            # Else redirect to login
            return redirect('login')


# USERS METHODS #
class Users():
    def signup(request):
        # If the request method is GET type then..
        if request.method == 'GET':
            # Return to the view the signup form
            return render(request, 'signup.html')
        # If the request method is POST type then...
        else:
            # If passwords match then..
            if request.POST['password1'] == request.POST['password2']:
                try:
                    # Use the user class for create a new user and save it
                    user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
                    user.save()
                    # Create cookie session
                    login(request, user)
                    return redirect('home')
                except IntegrityError:
                    # Return error if user already exists
                    return render(request, 'signup.html', {
                        'error': 'El usuario ya existe, inicie sesion'
                    })
            else:
                # Return error
                return render(request, 'signup.html', {
                    'error': 'Las contraseñas deben coincidir'
                })
    
    def signin(request):
        # If the request method its GET type then..
        if request.method == 'GET':
            # Render login form
            return render(request, 'login.html')
        # If the request method its POST type then..
        else:
            # Verify in the database if user and pass match
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'] )
            print(user)
            return redirect('login')
            # If they didn't match then.. 
            """ if user is None:
                context = {
                'error': 'Usuario o contraseña invalido'
                }
                return render(request, 'login.html', context)
            else:
                login(request, user)
                return redirect('home') """

    # This method verify if there's an user authenticated, if not, returns none
    def UserLoggedIn(request):
        if request.user.is_authenticated == True:
            username = request.user.username
        else:
            username = None
        return username

    def signout(self, request):
        # Use the method previously created
        username = self.UserLoggedIn(request)
        if username != None:
            logout(request)
            return redirect('login')

    def profile(request):
        if request.user.is_authenticated:
            return render(request, 'profile.html')
        else:
            redirect('login')