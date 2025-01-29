from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Produto
from django.shortcuts import render, get_object_or_404, redirect


# Lista de Produtos
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/lista_produtos.html', {'produtos': produtos})

# Detalhes do Produto
def detalhe_produto(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, 'loja/detalhe_produto.html', {'produto': produto})

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_produtos')
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos')
    else:
        form = AuthenticationForm()
    return render(request, 'loja/login.html', {'form': form})

# Cadastro
def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login')
        else:
            messages.error(request, 'Erro no cadastro. Tente novamente.')
    else:
        form = UserCreationForm()
    return render(request, 'loja/cadastro.html', {'form': form})

# Carrinho
def carrinho_view(request):
    # Simulação de um carrinho vazio, você pode integrar com o modelo de carrinho
    carrinho = []  # Aqui você deve pegar os produtos no carrinho do usuário
    return render(request, 'loja/carrinho.html', {'carrinho': carrinho})

