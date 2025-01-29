from django.urls import path
from . import views

urlpatterns = [
   path('', views.lista_produtos, name='lista_produtos'),
    path('produto/<int:id>/', views.detalhe_produto, name='detalhe_produto'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('carrinho/', views.carrinho_view, name='carrinho'),
]
