from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView
from .views import user_login

from .views import custom_logout


urlpatterns = [
    path('', views.index, name='index'),
    path('receita/<int:pk>/', views.detalhes_receita, name='detalhes_receita'),
    path('cadastrar-receita/', views.cadastrar_receita, name='cadastrar_receita'),
    path('cadastrar-categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registrar/', views.registrar, name='registrar'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', custom_logout, name='logout'),
]