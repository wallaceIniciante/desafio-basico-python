num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
operacao = input("Qual operacao? ex(+,-,*,/) ")

if operacao == "+":
    print(num1 + num2)

elif operacao == "-":
    print(abs(num1 - num2))

elif operacao == "*":
    print(num1 * num2)

elif operacao == "/":
    print(num1 / num2)

else:
    print("Operacao Inválida!")