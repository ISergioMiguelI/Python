import datetime
import random
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class Despesas:
    def __init__(self, valor, descricao, id):
        self.id = id
        self.valor = valor
        self.descricao = descricao
        self.data = datetime.datetime.now()

class GerenciadorDespesas:
    def __init__(self):
        self.despesas = []

    def adicionar_despesa(self, descricao, valor):
        id = random.randint(1, 1000)  # Gerar um ID aleatório para a despesa
        nova_despesa = Despesas(valor, descricao, id)
        self.despesas.append(nova_despesa)
        print("Despesa adicionada com sucesso!\n\n")
        return

    def listar_despesas(self):
        for despesa in self.despesas:
            print("Descrição:", despesa.descricao)
            print("Valor:", despesa.valor)
            print("Data:", despesa.data)
        exibirMenu()

    def remover_despesa(self):
        id = int(input("Informe o ID da despesa que deseja remover: "))
        for despesa in self.despesas:
            if despesa.id == id:
                self.despesas.remove(despesa)
                print("Despesa removida com Sucesso!\n\n")
                exibirMenu()
                return
        print("Despesa com o ID informado não encontrada.")

def exibirMenu():
    limpar_tela()
    print("------------Insira um Opção-----------------\n")
    print("1. Adicionar Despesas\n")
    print("2. Listar Despesas\n")
    print("3. Remover Despesas\n")
    print("4. Sair\n")
    
    gerenciador = GerenciadorDespesas()
    opcao = input("Opcao:")
    
    if opcao == "1":
        descricao = input("Descrição:\n")
        valor = float(input("Valor da despesa:\n"))
        gerenciador.adicionar_despesa(descricao, valor)
    elif opcao == "2":
        gerenciador.listar_despesas()
    elif opcao == "3":
        gerenciador.remover_despesa()
    elif opcao == "4":
        print("Saindo do Programa, Obrigado por usar :)")
    else: 
        print("Opcao errada ou Invalida inserida, tente novamente\n")

exibirMenu()
