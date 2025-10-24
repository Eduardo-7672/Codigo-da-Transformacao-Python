print ("\n--------------------")
print ("\fBem vindo ae paezão! o_o")
print ("\n--------------------")

nome_pessoa = str (input ("Qual o seu nome? "))
print(f"Olá, {nome_pessoa}! ")

idade_pessoa = int(
    input("Qual é sua idade? ")
)
if idade_pessoa >= 18:
    print ("Muito bem, você é maior de idade! Cuidado para não ser preso, 'Adulto' ^-^ ")

else:
    print ("Aah, que pena! Você é menor de idade. Pelo menos não pode ir pra cadeia u_u ")

altura_pessoa = float(input ("Qual é sua altura? "))
#print(f"Sua altura é {altura_pessoa}! ")
print(f"Muito bem! Sua altura é {altura_pessoa}, Seu nome é {nome_pessoa} e você tem {idade_pessoa}! ")


print ("\n--------------------------------------------------------------------------------------------------edueue")
print("Seja muito bem vindo, sinta se a vontade! Agora vamos fazer algumas contas com a calculadora ^-^")
print ("\n--------------------------------------------------------------------------------------------------")

def somar(a, b):
    """Calcula a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Calcula a subtração de dois números."""
    return a - b

def menu_principal():
    """Exibe o menu e gerencia as interações do usuário."""
    
    # Define a variável de controle do loop
    executando = True 
    
    while executando:
        # Exibe o menu
        print("-" * 30)
        print("     CALCULADORA INTERATIVA")
        print("-" * 30)
        print("1. Soma")
        print("2. Subtração")
        print("3. Sair")
        print("-" * 30)
        
        # Solicita a opção ao usuário
        escolha = input("Escolha uma opção (1, 2 ou 3): ")
        
        # Bloco para processar a escolha
        if escolha == '1':
            print("\n--- Opção: SOMA ---")
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = somar(num1, num2)
                print(f"\nResultado da Soma: {num1} + {num2} = {resultado}")
            except ValueError:
                print("\nERRO: Entrada inválida. Por favor, digite apenas números.")
        
        elif escolha == '2':
            print("\n--- Opção: SUBTRAÇÃO ---")
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = subtrair(num1, num2)
                print(f"\nResultado da Subtração: {num1} - {num2} = {resultado}")
            except ValueError:
                print("\nERRO: Entrada inválida. Por favor, digite apenas números.")
                
        elif escolha == '3':
            # Altera a variável de controle para sair do loop
            executando = False
            print("\nSaindo da calculadora. Obrigado por usar!")
            
        else:
            # Opção inválida
            print("\nOpção inválida. Por favor, escolha 1, 2 ou 3.")
            
        # Adiciona uma pausa e um separador para melhor visualização antes do próximo loop
        if executando:
            input("\nPressione ENTER para continuar para o menu...")

# Chama a função principal para iniciar o programa
if __name__ == "__main__":
    menu_principal()