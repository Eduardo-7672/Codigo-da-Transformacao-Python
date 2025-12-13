# =================================================================
# ATIVIDADE 1: Calculadora com Try-Except
# =================================================================

def calculadora_segura():
    """Realiza a divisão de dois números com tratamento de divisão por zero."""
    print("\n--- 🧮 Calculadora de Divisão Segura ---")
    
    # Coleta de inputs
    try:
        num1 = float(input("Digite o dividendo (primeiro número): ").replace(',', '.'))
        num2 = float(input("Digite o divisor (segundo número): ").replace(',', '.'))
    except ValueError:
        print("❌ Erro: Por favor, digite apenas números válidos.")
        return

    # Bloco try-except para tratamento de erro
    try:
        resultado = num1 / num2
        print(f"\n✅ Resultado da Divisão: {num1} / {num2} = {resultado:.4f}")
        
    except ZeroDivisionError:
        # Captura o erro específico de divisão por zero
        print("\n❌ Erro: Não é possível dividir por zero (ZeroDivisionError capturado).")
    except Exception as e:
        # Captura qualquer outro erro inesperado
        print(f"\n❌ Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    calculadora_segura()