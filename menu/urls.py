from django.urls import path
from .views import MenuPage
app_name = 'menu'
urlpatterns = [
    path('', MenuPage.as_view(), name='index',),

]
