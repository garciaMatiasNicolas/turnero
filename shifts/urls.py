from django.urls import path
from .views import Shift, Users

urlpatterns = [
    # Home view
    path('', Shift.home, name= 'home'),
    # Profile view
    path('user/<int:id>', Users.profile , name= 'profile'),
    # Users methods views (login-signup)
    path('signup/', Users.signup, name= 'signup'),
    path('login/', Users.signin, name= 'login'),
    path('logout/', Users.signout, name= 'logout')
]