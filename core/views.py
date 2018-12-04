from django.shortcuts import render
#from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'core/index.html', {})

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