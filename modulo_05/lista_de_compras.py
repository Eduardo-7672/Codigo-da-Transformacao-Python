def gerenciador_lista_compras():
    """
    Gerencia uma lista de compras interativa.
    Permite ao usuário adicionar, remover e visualizar itens.
    """
    # A lista vazia onde os itens serão armazenados.
    lista_de_compras = []

    while True:
        # Exibe o menu
        print("\n--- 🛒 Gerenciador de Lista de Compras ---")
        print("1. Adicionar Item")
        print("2. Remover Item")
        print("3. Visualizar Lista")
        print("4. Sair")
        print("-----------------------------------------")

        escolha = input("Escolha uma opção (1-4): ")

        # --- 1. Adicionar Item ---
        if escolha == '1':
            item = input("Digite o item a adicionar: ").strip().capitalize()
            if item:
                lista_de_compras.append(item)
                print(f"✅ '{item}' adicionado à lista.")
            else:
                print("❌ Entrada inválida. O item não pode ser vazio.")

        # --- 2. Remover Item ---
        elif escolha == '2':
            if not lista_de_compras:
                print("⚠️ A lista está vazia, não há itens para remover.")
                continue

            print("\nItens Atuais:")
            # Exibe a lista com índices numerados (começando em 1) para a escolha do usuário
            for i, item in enumerate(lista_de_compras):
                print(f"{i + 1}. {item}")

            try:
                # O usuário digita o número, subtraímos 1 para obter o índice real (começa em 0)
                indice_remover = int(input("Digite o NÚMERO do item que deseja remover: ")) - 1
                
                # Verifica se o índice é válido
                if 0 <= indice_remover < len(lista_de_compras):
                    # O método .pop() remove o item pelo índice e retorna o valor removido
                    item_removido = lista_de_compras.pop(indice_remover)
                    print(f"🗑️ '{item_removido}' removido da lista.")
                else:
                    print("❌ Número de item inválido.")
            except ValueError:
                print("❌ Entrada inválida. Por favor, digite um número.")

        # --- 3. Visualizar Lista ---
        elif escolha == '3':
            if lista_de_compras:
                print("\nLista de Compras Atual:")
                for item in lista_de_compras:
                    print(f"⭐ {item}")
            else:
                print("⚠️ A lista de compras está vazia.")

        # --- 4. Sair ---
        elif escolha == '4':
            print("👋 Fechando o Gerenciador de Lista de Compras. Até mais!")
            break

        # --- Opção Inválida ---
        else:
            print("❌ Opção inválida. Por favor, escolha um número entre 1 e 4.")

# Executa a função principal do programa
gerenciador_lista_compras()

