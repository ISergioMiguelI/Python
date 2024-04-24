import random

def adivinhar_numero():
    
    numero_secreto = random.randint(0, 20)
    
    tentativas = 0
    while True:
        
        tentativa = int(input("Adivinhe o número entre 0 e 20: "))
        
        # Verifica se a tentativa está correta
        if tentativa == numero_secreto:
            print("Parabéns! Você acertou o número em", tentativas, "tentativas!")
            break
        elif tentativa < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")
        
        tentativas += 1

# Chamando a função principal
adivinhar_numero()
