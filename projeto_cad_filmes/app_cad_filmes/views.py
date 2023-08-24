from django.shortcuts import render
from .models import Filme
def home(request):
    return render(request,'filmes/home.html')

def filmes(request):
    #Salva os dados da tela no banco de dados
    novo_filme = Filme()
    novo_filme.nome = request.POST.get('nome')
    novo_filme.descrição = request.POST.get('descrição')
    novo_filme.duração = request.POST.get('duração')
    novo_filme.save()
    
    #Exibir todos os filmes cadastrados
    filmes = {
        'filmes': Filme.objects.all()
    }
    #Retornar os dados para a página de listagem de filmes
    return render(request,'filmes/filmes.html',filmes) 