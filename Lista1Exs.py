#Exercício 1

x = 0;

while x < 8:
  print("ESPM-O INUSITADO EM CONSTANTE MOVIMENTO")
  x = x + 1
    
#Exercício 2

import time;

x = 10;
y = 1;

while x >= 0:
  print(x);
  time.sleep(y);
  x = x - 1;

#Exercício 3

v = [];

i = [];

while True:
  c = float(input('Informe o valor de sua compra--> '));
  k = int(input('Informe o número de itens adquiridos--> '));
  v.append(c);
  i.append(k);
  if(input('Deseja continuar? [Enter para Sim, N para parar]:') == 'N'):
    break;


mediav = sum(v) / len(v);
mediai = sum(i) /len(i);

maisv = max(v);
maisi = max(i);



print();
print('Média do valor total de compra dos clientes--> $', mediav);
print('Média do número de itens adquiridos--> ', mediai);
print('Maior valor total de compra dos clientes, ou seja, o cliente que gastou mais--> ', maisv);
print('Maior número de itens adquiridos em uma compra, ou seja, o cliente que comprou mais itens--> ', maisi);