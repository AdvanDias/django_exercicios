from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello Word <br> {} de {} anos</h1>'.format(nome,idade))

def soma(request,nome, n1, n2):
    total = n1+n2
    return HttpResponse('<h1>Olá {} Vamos Somar?</h1><br>'
                        '<h2>{} + {}</h2><br>'
                        '<h1>Total: {}</h1>'.format(nome,n1,n2,total))

def subtracao(request,nome, n1, n2):
    total = n1-n2
    return HttpResponse('<h1>Olá {} Vamos Subtrair?</h1><br>'
                        '<h2>{} - {}</h2><br>'
                        '<h1>Total: {}</h1>'.format(nome,n1,n2,total))

def divisao(request,nome, n1, n2):
    total = n1/n2
    return HttpResponse('<h1>Olá {} Vamos Dividir?</h1><br>'
                        '<h2>{} / {}</h2><br>'
                        '<h1>Total: {}</h1>'.format(nome,n1,n2,total))

def multiplicacao(request,nome, n1, n2):
    total = n1*n2
    return HttpResponse('<h1>Olá {} Vamos Multiplicar?</h1><br>'
                        '<h2>{} * {}</h2><br>'
                        '<h1>Total: {}</h1>'.format(nome,n1,n2,total))