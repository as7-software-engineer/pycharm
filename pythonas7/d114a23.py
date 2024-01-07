'''Crie um código em python que teste se o site Pudim está acessível pelo computador usado.
'''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('O site não está acessível no momento')
else:
    print('consegui acessar com sucesso')
    print(site.read())

