"""Djangoreq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from reqapp.views import GetInput,Relationship_test,Result,Add_Location_details,Add_Address_details,Display
urlpatterns = [
    path('admin/', admin.site.urls),
    path('agent/insert',GetInput.as_view(),name='insert'),
    path('agent/addagent',Relationship_test.as_view(),name='addagent'),
    path('agent/dispag',Result.as_view()),
    path('agent/addloc',Add_Location_details.as_view()),
    path('agent/addadd',Add_Address_details.as_view()),
    path('agent/result',Display.as_view()),
    path('agent/agentdet',Display_Agent_Details.as_view()),
         
]
