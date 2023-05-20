from django.contrib import admin
from django.urls import path

#There are generic views created by Django so you don't have to create your own views you just need to pass the templates to these views.
from django.contrib.auth import views as accountsViews
from accounts.views import register


"""
YOUR CODE

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logout, name="logout"),
    path('timeline', views.timeline, name="timeline"),
]
"""

#Added generic the generic views to these urls so you don't have to create them, they work great and you just need to pass the templates and specify where you want the user to
#be redirected when they log out, in this case I added the 'timeline' which is the name of the URL for timeline
urlpatterns = [
    path('login/', accountsViews.LoginView.as_view(template_name='accounts/login.html'), {'next_page' : 'timeline'}, name='login'),
    path('logout/', accountsViews.LogoutView.as_view(), {'next_page' : 'home'}, name='logout'),
    path('register/', register, name="register"),

]

