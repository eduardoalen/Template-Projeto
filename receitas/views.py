from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Receita, Categoria
from .forms import ReceitaForm, CategoriaForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth import logout



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo(a), {username}!')
                return redirect('index')
        messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'registrar.html', {'form': form})

def index(request):
    receitas = Receita.objects.all()
    categorias = Categoria.objects.all()
    
    # Filtro por categoria (condicional)
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        receitas = receitas.filter(categoria_id=categoria_id)
    
    # Filtro por dificuldade (condicional)
    dificuldade = request.GET.get('dificuldade')
    if dificuldade:
        receitas = receitas.filter(dificuldade=dificuldade)
    
    context = {
        'receitas': receitas,
        'categorias': categorias,
    }
    return render(request, 'index.html', context)

def detalhes_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)
    context = {
        'receita': receita,
    }
    return render(request, 'detalhes_receita.html', context)

@login_required
def cadastrar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST, request.FILES)
        if form.is_valid():
            receita = form.save(commit=False)
            receita.autor = request.user
            receita.save()
            messages.success(request, 'Receita cadastrada com sucesso!')
            return redirect('index')
    else:
        form = ReceitaForm()
    
    context = {
        'form': form,
    }
    return render(request, 'cadastrar_receita.html', context)

@login_required
def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria cadastrada com sucesso!')
            return redirect('index')
    else:
        form = CategoriaForm()
    
    return render(request, 'cadastrar_categoria.html', {'form': form})


@login_required  # Adicione esta linha antes da view
def cadastrar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST, request.FILES)
        if form.is_valid():
            receita = form.save(commit=False)
            receita.autor = request.user  # Garante que o autor seja o usuário logado
            receita.save()
            messages.success(request, 'Receita cadastrada com sucesso!')
            return redirect('index')
    else:
        form = ReceitaForm()
    
    return render(request, 'cadastrar_receita.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após logout

