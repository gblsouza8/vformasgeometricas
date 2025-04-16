def paralelepipedo():
    l = int(input("Digite a largura: "))
    c = int(input("Digite o comprimento: "))
    a = int(input("Digite a altura: "))
    v = l*c*a
    return ("O volume do seu paralelepipedo é: ", v)

def prismaRetangular():
    l = int(input("Digite a largura: "))
    c = int(input("Digite o comprimento: "))
    a = int(input("Digite a altura: "))
    v = c*l*a
    return ("O volume do seu prisma retangular é: ", v)

def cubo():
    a = int(input("Digite a aresta:"))
    v = a*a*a
    return ("O volume do seu cubo é: ", v)

def esfera():
    r = int(input("Insira o raio: "))
    r = r*r*r
    v = 4*3.14*r/3
    return ("O volume da sua esfera é: ", v)


pergunta = int(input("Qual forma geométrica você gostaria de calcular o volume?\n1. Paralelepipedo\n2. Prisma Retangular\n 3. Cubo\n 4. Esfera"))
if pergunta == 1:
    print(paralelepipedo())
elif pergunta == 2:
    print(prismaRetangular())
elif pergunta == 3:
    print(cubo())
elif pergunta == 4:
    print(esfera())
else:
    print("Escolha inválida... por favor, escolhar uma opção válida...")