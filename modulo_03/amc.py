# --- 1. Operadores Aritméticos ---

print("--- Demonstração de Operadores Aritméticos ---")

try:
    num1 = float(input("Digite o primeiro número (A): "))
    num2 = float(input("Digite o segundo número (B): "))
    
    # 1. Soma
    soma = num1 + num2
    print(f"\nSoma (A + B): {soma}")
    
    # 2. Subtração
    diferenca = num1 - num2
    print(f"Diferença (A - B): {diferenca}")
    
    # 3. Multiplicação
    multiplicacao = num1 * num2
    print(f"Multiplicação (A * B): {multiplicacao}")
    
    # 4. Divisão
    if num2 != 0:
        divisao = num1 / num2
        print(f"Divisão (A / B): {divisao}")
        
        # 5. Módulo (Resto da Divisão)
        # Note: O módulo com float pode ter resultados de ponto flutuante, 
        # mas é mais comum em inteiros.
        modulo = num1 % num2
        print(f"Módulo/Resto (A % B): {modulo}")
    else:
        print("Divisão e Módulo: Não é possível dividir por zero.")
        
except ValueError:
    print("\nERRO: Entrada inválida. Certifique-se de digitar números.")




    # --- 2. Comparação de Números ---

print("\n" + "="*40)
print("--- Programa: Qual é o Maior Número? ---")

try:
    num_a = int(input("Digite o primeiro número inteiro: "))
    num_b = int(input("Digite o segundo número inteiro: "))
    
    print("-" * 30)
    
    if num_a > num_b:
        print(f"O primeiro número ({num_a}) é maior que o segundo ({num_b}).")
    elif num_b > num_a:
        print(f"O segundo número ({num_b}) é maior que o primeiro ({num_a}).")
    else:
        print(f"Os dois números são iguais: {num_a} = {num_b}.")
        
except ValueError:
    print("\nERRO: Entrada inválida. Por favor, digite apenas números inteiros.")





    # --- 3. Classificação de Idade ---

print("\n" + "="*40)
print("--- Programa: Classificador de Idade ---")

try:
    idade = int(input("Digite sua idade: "))
    
    print("-" * 30)
    
    if idade < 0:
        print("Idade inválida.")
    elif idade <= 12:
        print("Classificação: Criança.")
    elif idade <= 17:
        print("Classificação: Adolescente.")
    elif idade <= 59:
        print("Classificação: Adulto.")
    elif idade >= 60:
        print("Classificação: Idoso.")
        
except ValueError:
    print("\nERRO: Entrada inválida. Por favor, digite um número inteiro para a idade.")






    # --- 4. Desafio Extra: Menu Interativo ---

def somar(a, b):
    """Calcula a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Calcula a subtração de dois números."""
    return a - b

def menu_interativo():
    """Gerencia o menu principal e o loop de execução."""
    
    executando = True 
    
    while executando:
        # Exibe o menu
        print("\n" + "="*40)
        print("     MENU INTERATIVO DE CÁLCULOS")
        print("="*40)
        print("1. Soma")
        print("2. Subtração")
        print("3. Sair")
        print("-" * 40)
        
        escolha = input("Escolha uma opção (1, 2 ou 3): ")
        
        if escolha in ('1', '2'):
            print("\n--- Preparando Operação ---")
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if escolha == '1':
                    resultado = somar(num1, num2)
                    print(f"\nResultado da SOMA: {num1} + {num2} = {resultado}")
                elif escolha == '2':
                    resultado = subtrair(num1, num2)
                    print(f"\nResultado da SUBTRAÇÃO: {num1} - {num2} = {resultado}")

            except ValueError:
                print("\nERRO: Entrada inválida. Por favor, digite apenas números.")
            
            input("\nPressione ENTER para voltar ao menu...")
        
        elif escolha == '3':
            executando = False
            print("\nEncerrando o programa. Até logo!")
            
        else:
            print("\nOpção inválida. Por favor, escolha 1, 2 ou 3.")

# Inicia o programa
if __name__ == "__main__":
    menu_interativo()