import math

# --- SEÇÃO DE FUNÇÕES (Simulando o módulo utilidades.py) ---

def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtracao(a, b):
    """Retorna a diferença entre dois números."""
    return a - b

def potencia(base, expoente):
    """Retorna o cálculo de potência."""
    return base ** expoente

def raiz_quadrada(numero):
    """Calcula a raiz quadrada de um número."""
    if numero < 0:
        return "Erro: Não existe raiz real de número negativo"
    return math.sqrt(numero)

def calcular_porcentagem(valor, percentual):
    """Calcula quanto é X por cento de um valor."""
    return (valor * percentual) / 100

# --- PROGRAMA PRINCIPAL (main) ---

def sistema_calculo():
    print("="*40)
    print("✨ SUPER CALCULADORA DINÂMICA ✨")
    print("="*40)

    try:
        # Coleta de dados do usuário
        print("\n[ Configuração de Valores ]")
        x = float(input("Digite o primeiro valor (X): "))
        y = float(input("Digite o segundo valor (Y): "))

        print("\n" + "-"*30)
        print("📊 RESULTADOS DA ANÁLISE")
        print("-"*30)

        # Execução das funções com os inputs do usuário
        res_soma = soma(x, y)
        res_sub  = subtracao(x, y)
        res_pot  = potencia(x, y)
        res_raiz_x = raiz_quadrada(x)
        res_raiz_y = raiz_quadrada(y)
        res_porcent = calcular_porcentagem(x, y)

        # Exibição formatada
        print(f"🔹 **Soma ($x + y$):** {res_soma}")
        print(f"🔹 **Subtração ($x - y$):** {res_sub}")
        print(f"🔹 **Potência ($x^y$):** {res_pot}")
        
        # Tratamento especial para exibição da Raiz Quadrada
        if isinstance(res_raiz_x, str):
            print(f"🔹 **Raiz Quadrada de X ($\sqrt{{x}}$):** {res_raiz_x}")
        else:
            print(f"🔹 **Raiz Quadrada de X ($\sqrt{{x}}$):** {res_raiz_x:.2f}")

        print(f"🔹 **Porcentagem ({y}% de {x}):** {res_porcent}")
        print("-"*30)

    except ValueError:
        print("\n❌ Erro: Por favor, insira apenas números válidos (use ponto para decimais).")

if __name__ == "__main__":
    sistema_calculo()