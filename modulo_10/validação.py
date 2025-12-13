# =================================================================
# ATIVIDADE 3: Validação de Entradas (Número Positivo)
# =================================================================

def validar_numero_positivo(prompt, tipo=float):
    """
    Garante que a entrada do usuário seja um número válido e positivo.
    Trata erros de tipo (ValueError) e verifica a condição (> 0).
    """
    while True:
        try:
            # Coleta e limpa a entrada
            entrada = input(prompt).strip().replace('"', '').replace("'", "").replace(',', '.')
            if not entrada:
                raise ValueError("A entrada não pode ser vazia.")
                
            # Tenta converter para o tipo (float ou int)
            valor = tipo(entrada)
            
            # Garante que o número seja positivo
            if valor > 0:
                return valor
            else:
                print("❌ Erro de Validação: O valor deve ser um número positivo (> 0).")
                
        except ValueError:
            # Trata erros de conversão (se o usuário digitar texto)
            print("❌ Erro de Entrada: Entrada inválida. Por favor, digite um número.")


def demonstrar_validacao():
    """Demonstra a função de validação para idade e valor."""
    print("\n--- ✅ Demonstração de Validação de Input ---")
    
    # Exemplo 1: Validar Idade (deve ser um inteiro positivo)
    print("\nTeste de Validação: Idade")
    idade = validar_numero_positivo("Digite sua idade (deve ser um inteiro positivo): ", tipo=int)
    print(f"✅ Idade validada com sucesso: {idade} anos.")

    # Exemplo 2: Validar Valor Monetário (deve ser um float positivo)
    print("\nTeste de Validação: Valor Monetário")
    valor = validar_numero_positivo("Digite um valor monetário (ex: 150.75): ", tipo=float)
    print(f"✅ Valor validado com sucesso: R$ {valor:.2f}.")

if __name__ == "__main__":
    demonstrar_validacao()