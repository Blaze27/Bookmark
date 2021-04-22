from django.urls import path
from . import views
app_name = 'bookmarkApp'


urlpatterns = [
    path('', views.index, name = "index")
]
