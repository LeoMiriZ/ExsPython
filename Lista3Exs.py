#Exercício 1

x = 1;

while x < 12:
    print('O aluno Leonardo Miri Baptista cursa Sistemas de Informação na unidade Joaquim Távora (TECH)');
    x = x + 1;
    


#Exercício 2

numero = int(input('Digite um número inteiro positivo: '));

x = 1;
y = 2;

while y <= numero:
    x  = x * y;
    y = y + 1;
    
print();
print('O fatorial desse número é', x);


#Exercício 3


l = [];

while True:
  c = float(input('Informe a cotação do Bitcoin--> '));
  if c == 0:
    print();
    print('Operação finalizada com sucesso!');
    break;
  else:
    l.append(c);

maiorc = max(l);
menorc = min(l);
mediac = sum(l) / len(l);

print();
print('A maior cotação é $', maiorc);
print('A menor cotação é $', menorc);
print('A média das cotações é $', mediac);