from django.shortcuts import render
from . import views

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    n1 = int(request.GET.get('num1'))
    n2 =int(request.GET.get('num2'))  
    op = str(request.GET.get('op'))  
    if op == 'plus':
        r = n1 + n2 
    elif op == 'sub':
        r = n1 - n2
    elif op == 'div':
        r = n1 / n2
    else : 
        r = n1 * n2
    
    con = {'result' : r}

    return render(request, 'result.html', con)