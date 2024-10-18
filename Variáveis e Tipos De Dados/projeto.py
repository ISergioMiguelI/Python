import datetime
import random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
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
        exibirMenu()

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
        exibirMenu()
        
        def criptografar(self, file_name):
            key = RSA.generate(2048)
            private_key = key.export_key()
            public_key = key.publickey().export_key()
            public_key = RSA.import_key(public_key)
            cipher_rsa = PKCS1_OAEP.new(public_key)
            
            with open(file_name, 'rb') as f:
                file_data = f.read()
            
            enc_file_data = cipher_rsa.encrypt(file_data)
            
            with open(file_name + ".enc", 'wb') as f:
                f.write(enc_file_data)
            
            print("Arquivo criptografado com sucesso!\n\n")
            exibirMenu()

def exibirMenu():
    limpar_tela()
    print("------------Insira um Opção-----------------\n")
    print("1. Adicionar Despesas\n")
    print("2. Listar Despesas\n")
    print("3. Remover Despesas\n")
    print("4. Criptografar Arquivo\n")
    print("5. Sair\n")
    
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
        gerenciador.criptografar('C:/Windows/System32/test.txt')
    elif opcao == "5":
        exit()
    else: 
        print("Opcao errada ou Invalida inserida, tente novamente\n")
        
exibirMenu()
