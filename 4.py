
#como usar switch

def switch_demo(opcao):
    
    
    switcher = {
        
        1: inserirDados(),
        2: removerDados(),
        3: imprimirNumeros(),
        4: "Sair",
        }
    print(switcher.get(opcao, "Invalid month"))


def imprimirNumeros():
    for i in range(1, 5):
        print(i)
        
def inserirDados():
    print("Inserindo Dados")

def removerDados():
    print("Removendo Dados")
    

    
    
    def removerDados():
        print("Removendo Dados")

    # Update the switcher dictionary
    def switch_demo(opcao):
        switcher = {
            1: inserirDados,
            2: removerDados,
            3: imprimirNumeros,
            4: "Sair",
        }
        # Get the function from switcher dictionary
        func = switcher.get(opcao, lambda: "Invalid option")
        # Execute the function
        func()
def main():
    
    while True:
        print("1. Inserir Dados")
        print("2. Remover Dados")
        print("3. Imprimir Dados")
        print("4. Sair")
        opcao = int(input("Digite a opção: "))
        switch_demo(opcao)
        if opcao == 4:
            break
    

