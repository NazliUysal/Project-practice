"""
URL configuration for network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from artwork.views import timeline

"""
When you are importing a group of urls from an app in this case:
    path('', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('', include('artwork.urls')),

    You neeed to set a main url that group them together. I'm going to change them to what would be the best
    option in this case

"""

"""

YOUR PREVIOUS CODE
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('', include('artwork.urls')),
]
"""

#Recommendation
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('artwork/', include('artwork.urls')),
    path('', timeline, name='timeline'),
]

#I deleted the auth.urls because we are going to call those urls inside account, there's no need to call it here
#Divide and conquer!. It's important to keep things separate so it's easier for you to debugg and find errors, etc..

urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)