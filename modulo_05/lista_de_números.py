def separar_pares_impares_dinamico():
    """
    Coleta uma lista de números do usuário, identifica quais são pares e ímpares, 
    e exibe as duas listas separadamente.
    """
    
    numeros_coletados = []
    
    print("\n--- 🔢 Coleta de Números para Análise ---")
    print("Digite um número por vez. Digite 'fim' para terminar a coleta e analisar.")
    
    # 1. Coleta Dinâmica de Números
    while True:
        entrada = input("Digite um número inteiro (ou 'fim'): ").strip()
        
        # Condição de parada do loop
        if entrada.lower() == 'fim':
            if not numeros_coletados:
                print("⚠️ A lista está vazia. Adicione pelo menos um número para continuar.")
                continue
            break
        
        try:
            # Tenta converter a entrada em um número inteiro
            numero = int(entrada)
            numeros_coletados.append(numero)
            print(f"Número {numero} adicionado.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

    # 2. Processamento e Separação dos Números
    pares = []
    impares = []
    
    for num in numeros_coletados:
        # A lógica principal: um número é par se o resto da divisão por 2 for 0
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    # 3. Exibição dos Resultados
    print("\n\n--- 📊 Resultado da Análise ---")
    print("---------------------------------------")
    print(f"Conjunto original de números: {numeros_coletados}")
    
    print(f"\n✅ **Números Pares ({len(pares)}):**")
    if pares:
        print(pares)
    else:
        print("Nenhum número par encontrado.")

    print(f"\n❌ **Números Ímpares ({len(impares)}):**")
    if impares:
        print(impares)
    else:
        print("Nenhum número ímpar encontrado.")
    
    print("---------------------------------------")

# Executa a função para iniciar o programa
separar_pares_impares_dinamico()