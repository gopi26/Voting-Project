from django.urls import path,include
from django.contrib import admin
from . import views
from django.views.generic.base import TemplateView

urlpatterns=[
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path("vote",views.vote,name="vote"),
    path("result",views.result,name="result"),
    path("addcanditate",views.addcanditate,name="add"),
    path('', TemplateView.as_view(template_name='registration/home.html'), name='home'),
]