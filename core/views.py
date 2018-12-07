from django.shortcuts import render, redirect
#from django.contrib.auth import authenticate, login
from .forms import PessoaForm
from .models import Pessoa

# Create your views here.
def index(request):
    return render(request, 'core/index.html', {})

def list_pessoas(request):
    pessoas =  Pessoa.objects.all()
    return render(request, "core/list_pessoas.html", {'pessoas':pessoas})

def new_pessoas(request):
    form = PessoaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('url_list_pessoas')
            # listagem(request) #repete o formulário e insere dado repetido pq na url fica com o nome /Nova

    return render(request, 'core/new_pessoas.html', {'form': form})


def edit_pessoas(request,pk):
    data = {}
    pessoa = Pessoa.objects.get(pk=pk)
    form = PessoaForm(request.POST or None, instance=pessoa)

    if form.is_valid():
        form.save()
        return redirect('url_list_pessoas')
        #listagem(request) #repete o formulário e insere dado repetido pq na url fica com o nome /Nova

        # data['transacao'] = transacao
    return render(request, 'core/edit_pessoas.html', {'form': form})

def delete_pessoas(request,pk):
#    return render(request, 'core/index.html', {})
    pessoa = Pessoa.objects.get(pk=pk)
    pessoa.delete()
    return redirect('url_list_pessoas')






    #pessoa = get_object_or_404(Pessoas, pk=pk)
    # if request.method == "POST":
    #     form = PessoaForm(request.POST, instance=pessoa)
    #     if form.is_valid():
    #         pessoa = form.save(commit=False)
    #         pessoa.nome = request.user
    #         pessoa.endereco = request.endereco
    #         pessoa.save()
    #         return redirect('core/edit_pessoa', pk=pessoa.pk)
    #     else:
    #         form = PessoaForm(instance=post)
    #         return render(request, 'core/edit_pessoas.html', {'form':form})

    #return render(request, 'core/index.html', {})

    # post = get_object_or_404(Post, pk=pk)
    # if request.method == "POST":
    #     form = PostForm(request.POST, instance=post)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.author = request.user
    #         post.published_date = timezone.now()
    #         post.save()
    #         return redirect('post_detail', pk=post.pk)
    # else:
    #     form = PostForm(instance=post)
    # return render(request, 'core/post_edit.html', {'form': form})


#def login_view(request):
#    username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(username=username, password=password)
#    if user is not None:
#        if user.is_active:
#            login(request, user)
#            # Redirecione para uma página de sucesso.
#            
#        else:
#            # Retorna uma mensagem de erro de 'conta desabilitada' .
#            print("conta errada")
#    else:
#        # Retorna uma mensagem de erro 'login inválido'.
#        print("Teste")