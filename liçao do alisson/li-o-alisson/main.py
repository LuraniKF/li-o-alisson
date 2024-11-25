nota1 = int(input("digite sua primeira nota aqui "))
nota2 = int(input("digite sua segunda nota aqui "))
nota3 = int(input("digite sua terceira nota aqui "))
nota4 = int(input("digite sua quarta nota aqui "))

soma = nota1 + nota2 + nota3 + nota4

média = soma/4 
if média < 6:
    print("sua média é menor que 6, reprovado", média)
if média >= 6:
    print("sua média é maior que 6, aprovado", média)


