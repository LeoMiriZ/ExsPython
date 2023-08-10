#Exercício 1

modcar = str(input("Digite o modelo do carro:"));
anocar = int(input("Digite o ano de fabricação do carro:"));
precar = float(input("Digite o preço do carro:"));

if precar < 30000:
  comissao = precar * 0.05
    
else:
  comissao = precar * 0.07
print();
print("Você irá receber R$", comissao, "de comissão pela venda do carro", modcar, ", fabricado em", anocar, ".");

#Exercício 2

num = int(input("Digite um valor entre 1 e 7: "));
print();
match num:
  
  case 1:
    print("Segunda-feira")
  case 2:
    print("Terça-feira")
  case 3:
    print("Quarta-feira")
  case 4:
    print("Quinta-feira")
  case 5:
    print("Sexta-feira")
  case 6:
    print("Sábado")
  case 7:
    print("Domingo")
  case other:
    print("Número inválido")
    
#Exercício 3

import random
escolha_jogador = input("Digite a sua escolha (pedra, papel, tesoura): ")

possiveis_escolhas = ["pedra", "papel", "tesoura"]
escolha_computador = random.choice(possiveis_escolhas)

print("Você escolheu", escolha_jogador, "\nO computador escolheu", escolha_computador)
print();

if escolha_jogador == "pedra" and escolha_computador == "pedra" or escolha_jogador == "papel" and escolha_computador == "papel" or escolha_jogador == "tesoura" and escolha_computador == "tesoura":
  print("Empate")
elif escolha_jogador == "pedra" and escolha_computador == "papel":
  print("Computador venceu!")
elif escolha_jogador == "pedra" and escolha_computador == "tesoura":
  print("Jogador venceu!")
elif escolha_jogador == "papel" and escolha_computador == "pedra":
  print("Jogador venceu!")
elif escolha_jogador == "papel" and escolha_computador == "tesoura":
  print("Computador venceu!")
elif escolha_jogador == "tesoura" and escolha_computador == "papel":
  print("Jogador venceu!")
elif escolha_jogador == "tesoura" and escolha_computador == "pedra":
  print("Computador venceu!")