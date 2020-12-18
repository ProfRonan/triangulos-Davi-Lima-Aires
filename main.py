"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    a = float(input('Digite um dos lados do triangulo:'))
    b = float(input('Digite outro lado do triangulo:'))
    c = float(input('Digite o último lado do triangulo:'))
    if a<b+c and b<a+c and c<a+b:
     if a==b and b==c and c==a:
       print('O triângulo é equilátero.')
     elif (a==b and b!=c) or (b==c and c!=a) or (c==a and b!=a):
       print('O triângulo é isósceles.')
     elif a!=b and a!=c and b!=c:
       print('O triângulo é escaleno.')
    else:
       print('Os valores informados não formam um triângulo.')
    
if __name__ == '__main__':
    main()
   