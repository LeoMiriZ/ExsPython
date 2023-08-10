#Exercício 1

dep = float(input("Digite o valor de depósito:"));

saq = float(input("Digite o valor de saque:"));

res = dep - saq;

if dep > saq:
  print("Saldo positivo em: R$", res)
elif dep < saq:
  print("Saldo negativo em: R$", res)
elif dep == saq:
  print("Saldo zerado!")
else:
  print("Operação inválida!");

#Exercício 2

hrdia = int(input("Informe a parte INTEIRA da hora entre 0 e 24 horas:"));

if hrdia >= 0 and hrdia < 12:
  print("Bom dia!")
elif hrdia >= 12 and hrdia < 18 and hrdia != 17:
  print("Boa tarde!")
elif hrdia == 17:
  print("Hora do chá!")
elif hrdia >= 18 and hrdia < 24:
  print("Boa noite!")
else:
  print("Hora inválida!");

#Exercício 3

cla = input("Classificação? (V/L/A): ")
ver = int(input("Quantos Vermelhos estão aguardando? "))
lar = int(input("Quantos Laranjas estão aguardando? "))
azu = int(input("Quantos Azuis estão aguardando? "))

if cla == "V":
    min = ver * 7
elif cla == "L":
    min = lar * 5 + ver * 7
elif cla == "A":
    min = ver * 7 + lar * 5 + azu * 5
else:
    print("Classificação inválida")

print("Tempo de espera é de", min, "minutos.")

#Exercício 4

print("Responda sim ou nao para as perguntas a seguir ")
contagemPontos = 0
formacaoEcono = input("Tem formação na área econômica? ")
if formacaoEcono == "sim":
  contagemPontos = contagemPontos + 1
patrimonio = input("Já tem patrimônio consolidado? ")
if patrimonio == "sim":
  contagemPontos = contagemPontos + 1
investirTrinta = input("Pretende investir mais que 30% de seus rendimentos? ")
if investirTrinta == "sim":
  contagemPontos = contagemPontos + 1
derivativos = input("Já operou em derivativos anteriormente? ")
if derivativos == "sim":
  contagemPontos = contagemPontos + 1
perdas = input("Está disposto a ter perdas relevantes a curto prazo? ")
if perdas == "sim":
  contagemPontos = contagemPontos + 1

match contagemPontos:
  case 0 :
    print("Inexperiente")
  case 1 : 
    print("Inexperiente")
  case 2 : 
    print("Conservador")
  case 3 : 
    print("Ousado")
  case 4 : 
    print("Ousado")
  case 5 : 
    print("Agressivo")