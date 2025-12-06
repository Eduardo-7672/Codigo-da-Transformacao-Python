def sistema_agenda_contatos():
    """
    Desenvolve um sistema de agenda de contatos interativo usando um dicionário.
    Permite adicionar, remover, buscar e listar contatos.
    """
    # Inicializa o dicionário vazio que será a nossa agenda
    agenda = {}

    while True:
        # Exibe o menu principal
        print("\n--- 📞 Sistema de Agenda de Contatos ---")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Buscar Contato")
        print("4. Listar Todos os Contatos")
        print("5. Sair")
        print("-----------------------------------------")

        escolha = input("Escolha uma opção (1-5): ")

        # --- 1. Adicionar Contato ---
        if escolha == '1':
            nome = input("Digite o NOME do novo contato: ").strip().capitalize()
            # O nome é usado como chave, então deve ser único e não vazio
            if not nome:
                print("❌ O nome do contato não pode ser vazio.")
                continue
            
            # Garante que não está adicionando um contato já existente
            if nome in agenda:
                print(f"⚠️ O contato '{nome}' já existe. Número atual: {agenda[nome]}")
                print("Se deseja alterar, remova e adicione novamente.")
                continue
                
            telefone = input(f"Digite o TELEFONE de {nome}: ").strip()
            
            if telefone:
                # Adiciona o nome como chave e o telefone como valor
                agenda[nome] = telefone
                print(f"✅ Contato '{nome}' adicionado com sucesso.")
            else:
                print("❌ O telefone não pode ser vazio.")


        # --- 2. Remover Contato ---
        elif escolha == '2':
            nome = input("Digite o NOME do contato para remover: ").strip().capitalize()
            # Verifica se a chave (nome) existe no dicionário antes de tentar remover
            if nome in agenda:
                del agenda[nome]
                print(f"🗑️ Contato '{nome}' removido.")
            else:
                print(f"❌ Erro: Contato '{nome}' não encontrado na agenda.")

        # --- 3. Buscar Contato ---
        elif escolha == '3':
            nome = input("Digite o NOME do contato para buscar: ").strip().capitalize()
            
            # O método .get(chave) busca o valor, retornando None se a chave não existir
            telefone = agenda.get(nome) 

            if telefone:
                print(f"\n✅ Contato Encontrado:")
                print(f"**Nome:** {nome}")
                print(f"**Telefone:** {telefone}")
            else:
                print(f"❌ Contato '{nome}' não encontrado na agenda.")

        # --- 4. Listar Todos os Contatos ---
        elif escolha == '4':
            if agenda:
                print("\n--- 📝 Lista Completa de Contatos ---")
                # Itera sobre os pares chave-valor do dicionário
                for nome, telefone in agenda.items():
                    print(f"**{nome}**: {telefone}")
            else:
                print("⚠️ A agenda de contatos está vazia.")

        # --- 5. Sair ---
        elif escolha == '5':
            print("👋 Fechando o Sistema de Agenda. Até logo!")
            break

        # --- Opção Inválida ---
        else:
            print("❌ Opção inválida. Por favor, escolha um número entre 1 e 5.")

# Executa a função principal para iniciar o sistema
sistema_agenda_contatos()