#Exercício 1

pv = float(input("Preço de venda unitário do produto:"));
cv = float(input("Custo variável unitário: "));
cf = float(input("Custo fixo total: "));
print();

pe = (cf) / (pv - cv);

print("O ponto de equilíbrio é: ", pe);

#Exercício 2

pa = float(input("Insira o poder de ataque: "));
nv = float(input("Insira o nível de ataque: "));
pd = float(input("Insira o poder de defesa: "));
print();

dano = (((2 * nv) / (5) + 2) * (pa)) / (pd + 2);

print("O dano causado pelo ataque é: ", dano);

#Exercício 3

pdq = int(input("Insira a quantidade de pães de queijo que deseja fazer: "));
gra = float(input("Insira o peso de cada pão de queijo, em gramas: "));
print();

mult = pdq * gra;

x1 = (500 * mult) /(1000);
x2 = (2 * mult) / (500);
x3 = (1 * mult) / (1000);

print("Quantidade de polvilho doce necessária: ", x1, "g");
print("Quantidade de ovos necessária: ", x2, " ovo(s)");
print("Quantidade de copos de leite necessária: ", x3, " copo(s) de leite");
print("Quantidade de colheres de chá de sal necessária: ", x3, " colher(es) de chá de sal");