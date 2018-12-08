from django.shortcuts import render, redirect
#from django.contrib.auth import authenticate, login
from .forms import PessoaForm, EnderecoForm, ItemForm, CessaoForm
from .models import Pessoa, Endereco, Item, Cessao


# Create your views here.
def index(request):
    return render(request, 'core/index.html', {})


def list_pessoas(request):
    pessoas =  Pessoa.objects.all()
    return render(request, "core/list_pessoas.html", {'pessoas': pessoas})


def new_pessoas(request):
    form = PessoaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('url_list_enderecos')
            # listagem(request) #repete o formulário e insere dado repetido pq na url fica com o nome /Nova

    return render(request, 'core/new_enderecos.html', {'form': form})


def edit_pessoas(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    form = PessoaForm(request.POST or None, instance=pessoa)

    if form.is_valid():
        form.save()
        return redirect('url_list_pessoas')
        #listagem(request) #repete o formulário e insere dado repetido pq na url fica com o nome /Nova

        # data['transacao'] = transacao
    return render(request, 'core/edit_pessoas.html', {'form': form})


def delete_pessoas(request, pk):
#    return render(request, 'core/index.html', {})
    pessoa = Pessoa.objects.get(pk=pk)
    pessoa.delete()
    return redirect('url_list_pessoas')


def list_enderecos(request):
    enderecos = Endereco.objects.all()
    return render(request, "core/list_enderecos.html", {'enderecos': enderecos})


def new_enderecos(request):
    form = EnderecoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('url_list_pessoas')
            # listagem(request) #repete o formulário e insere dado repetido pq na url fica com o nome /Nova

    return render(request, 'core/new_enderecos.html', {'form': form})


def edit_enderecos(request, pk):
    endereco = Endereco.objects.get(pk=pk)
    form = EnderecoForm(request.POST or None, instance=endereco)

    if form.is_valid():
        form.save()
        return redirect('url_list_enderecos')
        #listagem(request) #repete o formulário e insere dado repetido pq na url fica com o nome /Nova

    return render(request, 'core/edit_enderecos.html', {'form': form})


def delete_enderecos(request, pk):
    endereco = Endereco.objects.get(pk=pk)
    endereco.delete()
    return redirect('url_list_enderecos')


def list_itens(request):
    itens = Item.objects.all()
    return render(request, "core/list_itens.html", {'itens': itens})


def new_itens(request):
    form = ItemForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('url_list_itens')
            # listagem(request) #repete o formulário e insere dado repetido pq na url fica com o nome /Nova

    return render(request, 'core/new_itens.html', {'form': form})


def edit_itens(request, pk):
    item = Item.objects.get(pk=pk)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('url_list_itens')
        #listagem(request) #repete o formulário e insere dado repetido pq na url fica com o nome /Nova

    return render(request, 'core/edit_itens.html', {'form': form})


def delete_itens(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return redirect('url_list_itens')


def list_cessoes(request):
    cessoes = Cessao.objects.all()
    return render(request, "core/list_cessoes.html", {'cessoes': cessoes})


def new_cessoes(request):
    form = CessaoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('url_list_cessoes')
            # listagem(request) #repete o formulário e insere dado repetido pq na url fica com o nome /Nova

    return render(request, 'core/new_cessoes.html', {'form': form})


def edit_cessoes(request, pk):
    cessao = Cessao.objects.get(pk=pk)
    form = CessaoForm(request.POST or None, instance=cessao)

    if form.is_valid():
        form.save()
        return redirect('url_list_cessoes')
        #listagem(request) #repete o formulário e insere dado repetido pq na url fica com o nome /Nova

    return render(request, 'core/edit_cessoes.html', {'form': form})


def delete_cessoes(request, pk):
    cessao = Cessao.objects.get(pk=pk)
    cessao.delete()
    return redirect('url_list_cessoes')




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