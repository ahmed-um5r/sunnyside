from django.urls import include, path
from . import views

urlpatterns = [ 
    path('',views.home, name="home"),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
