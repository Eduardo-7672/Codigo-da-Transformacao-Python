def maior_menor(lista_numeros):
    """
    Recebe uma lista de números e retorna o maior e o menor valor.

    Parâmetros:
        lista_numeros (list): Uma lista de números (int ou float).

    Retorna:
        tuple: Uma tupla contendo o maior e o menor número (maior, menor).
    """
    if not lista_numeros:
        return None, None
    
    maior_valor = max(lista_numeros)
    menor_valor = min(lista_numeros)
    
    return maior_valor, menor_valor

def analisar_e_reiniciar(numeros_coletados):
    """
    Analisa os números, exibe o maior e o menor, e pergunta ao usuário se 
    deseja reiniciar a lista ou continuar.
    
    Parâmetros:
        numeros_coletados (list): A lista atual de números.
        
    Retorna:
        list: A lista atualizada (limpa se o usuário reiniciar, ou a mesma se continuar).
    """
    if not numeros_coletados:
        print("\n❌ Nenhuma número foi inserido para análise.")
        return [] # Retorna lista vazia se não havia nada para analisar
    
    # Execução da Função maior_menor
    maior, menor = maior_menor(numeros_coletados)
    
    # Exibição dos Resultados
    print("\n--- 📊 Resultado da Análise ---")
    print(f"Lista de números fornecida: {numeros_coletados}")
    print(f"**O MAIOR número é:** {maior} ⭐")
    print(f"**O MENOR número é:** {menor} 👇")
    print("---------------------------------------")
    
    # Pergunta de Reinício
    while True:
        print("\nO que deseja fazer agora?")
        print("1. Continuar adicionando à lista atual.")
        print("2. Reiniciar (limpar a lista e começar de novo).")
        print("3. Sair do programa.")
        
        escolha = input("Escolha uma opção (1, 2 ou 3): ").strip()
        
        if escolha == '1':
            print("Continuando com a lista atual.")
            return numeros_coletados # Retorna a lista atual
        elif escolha == '2':
            print("Lista limpa. Começando uma nova lista.")
            return [] # Retorna uma nova lista vazia
        elif escolha == '3':
            print("Saindo do programa. Até logo!")
            exit() # Encerra o programa
        else:
            print("❌ Opção inválida. Por favor, escolha 1, 2 ou 3.")

def coletar_numeros_e_encontrar_extremos():
    """
    Loop principal para coletar números dinamicamente e gerenciar a lista.
    """
    
    numeros_coletados = []
    
    print("\n--- 🔎 Encontrar Maior e Menor Número ---")
    
    while True:
        # Se a lista estiver vazia, avisa o usuário
        if not numeros_coletados:
            print("\n**LISTA VAZIA.** Comece adicionando o primeiro número.")
        else:
            print(f"\nLista atual ({len(numeros_coletados)} itens): {numeros_coletados}")
            
        print("Digite um número, 'analisar' para calcular, ou 'fim' para sair.")

        entrada = input("Ação ou Número: ").strip().lower()
        
        if entrada == 'fim':
            print("Saindo do programa. Até logo!")
            break
        
        if entrada == 'analisar':
            # Chama a função que analisa e decide se reinicia ou continua
            numeros_coletados = analisar_e_reiniciar(numeros_coletados)
            continue # Volta para o início do loop para nova coleta

        try:
            # Tenta converter a entrada em um número
            numero = float(entrada)
            numeros_coletados.append(numero)
            print(f"Número {numero} adicionado.")
        except ValueError:
            print("❌ Entrada inválida. Digite um número, 'analisar' ou 'fim'.")

# Executa o programa principal
coletar_numeros_e_encontrar_extremos()