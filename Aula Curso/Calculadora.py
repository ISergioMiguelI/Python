def add (x, y):
    return x + y

def sub (x, y):
    return x - y

def mul (x, y):
    return x * y

def div (x, y):
    return x / y

print("Escolhe uma opção:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Escolhe uma opção: (1-4) ")

x = int(input("Escolhe o primeiro número: "))
y = int(input("Escolhe o segundo número: "))

if opcao == 1:
    print(x, "+", y, "=", add(x, y))
elif opcao == 2:
    print(x, "-", y, "=", sub(x, y))
elif opcao == 3:
    print(x, "*", y, "=", mul(x, y))
elif opcao == 4:
    print(x, "/", y, "=", div(x, y))
    
else:
    print("Opção inválida")