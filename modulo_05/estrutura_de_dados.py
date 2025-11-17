# =================================================================
# 1. Lista de Compras Dinâmica
# =================================================================
def gerenciar_lista_compras():
    """Gerencia uma lista de compras, permitindo adicionar, remover e visualizar itens."""
    lista_compras = []
    print("\n--- 🛒 Gerenciador de Lista de Compras ---")

    while True:
        print("\nOpções:")
        print("  1. Adicionar item")
        print("  2. Remover item")
        print("  3. Visualizar lista")
        print("  4. Sair do gerenciador")

        escolha = input("Escolha uma opção (1-4): ")

        if escolha == '1':
            item = input("Digite o nome do item a adicionar: ")
            lista_compras.append(item)
            print(f"✅ '{item}' adicionado à lista.")
        
        elif escolha == '2':
            if not lista_compras:
                print("⚠️ A lista de compras está vazia.")
                continue

            print("\nLista atual:")
            for i, item in enumerate(lista_compras):
                print(f"  {i+1}: {item}")
            
            try:
                indice_remover = int(input("Digite o número do item a remover: ")) - 1
                if 0 <= indice_remover < len(lista_compras):
                    item_removido = lista_compras.pop(indice_remover)
                    print(f"❌ '{item_removido}' removido da lista.")
                else:
                    print("🚫 Número inválido.")
            except ValueError:
                print("🚫 Entrada inválida. Digite um número.")

        elif escolha == '3':
            if lista_compras:
                print("\n📋 Sua Lista de Compras Atual:")
                for item in lista_compras:
                    print(f"- {item}")
            else:
                print("⚠️ A lista de compras está vazia.")

        elif escolha == '4':
            print("👋 Saindo do Gerenciador de Lista de Compras.")
            break

        else:
            print("🚫 Opção inválida. Por favor, tente novamente.")

# =================================================================
# 2. Armazenar Dados de Aluno em Dicionário
# =================================================================
def armazenar_dados_aluno():
    """Armazena e exibe dados (nome, idade, notas) de um aluno em um dicionário."""
    print("\n--- 🧑‍🎓 Dados do Aluno ---")
    
    # Coletando os dados
    nome = input("Digite o nome do aluno: ")
    try:
        idade = int(input("Digite a idade do aluno: "))
        nota1 = float(input("Digite a Nota 1 (ex: 8.5): "))
        nota2 = float(input("Digite a Nota 2 (ex: 9.0): "))
        
        # Criando o dicionário
        aluno = {
            "nome": nome,
            "idade": idade,
            "notas": [nota1, nota2],
            "media": (nota1 + nota2) / 2
        }
        
        # Exibindo os dados
        print("\n✅ Dados do Aluno Armazenados:")
        print(f"  Nome: **{aluno['nome']}**")
        print(f"  Idade: **{aluno['idade']}** anos")
        print(f"  Notas: **{aluno['notas']}**")
        print(f"  Média: **{aluno['media']:.2f}**")

    except ValueError:
        print("🚫 Entrada inválida para Idade ou Notas. Por favor, use números.")

# =================================================================
# 3. Percorrer Conjunto de Números (Pares/Ímpares)
# =================================================================
def separar_pares_impares():
    """Identifica e exibe números pares e ímpares de um conjunto."""
    print("\n--- 🔢 Separador de Pares e Ímpares ---")
    
    # Conjunto de números (pode ser alterado)
    conjunto_numeros = [1, 14, 7, 22, 5, 30, 9, 8, 11, 4]
    
    # Inicializando as listas
    pares = []
    impares = []
    
    print(f"Conjunto de números original: {conjunto_numeros}")
    
    # Percorrendo o conjunto com um loop
    for numero in conjunto_numeros:
        # Se o resto da divisão por 2 for 0, é par
        if numero % 2 == 0:
            pares.append(numero)
        # Caso contrário, é ímpar
        else:
            impares.append(numero)
            
    # Exibindo os resultados separadamente
    print("\n✅ Resultados:")
    print(f"  Números Pares: **{pares}**")
    print(f"  Números Ímpares: **{impares}**")

# =================================================================
# Desafio Extra: Sistema de Agenda de Contatos
# =================================================================
def gerenciar_agenda_contatos():
    """Cria um sistema de agenda de contatos usando dicionários."""
    agenda = {}
    print("\n--- 📞 Agenda de Contatos (Desafio Extra) ---")

    while True:
        print("\nOpções da Agenda:")
        print("  1. Adicionar Contato")
        print("  2. Remover Contato")
        print("  3. Buscar Contato")
        print("  4. Visualizar Todos")
        print("  5. Sair da Agenda")

        escolha = input("Escolha uma opção (1-5): ")
        
        if escolha == '1':
            nome = input("Digite o NOME do contato: ").strip().title()
            telefone = input("Digite o NÚMERO de telefone: ").strip()
            agenda[nome] = telefone
            print(f"✅ Contato '{nome}' adicionado.")

        elif escolha == '2':
            nome = input("Digite o NOME do contato para remover: ").strip().title()
            if nome in agenda:
                del agenda[nome]
                print(f"❌ Contato '{nome}' removido.")
            else:
                print(f"⚠️ Contato '{nome}' não encontrado na agenda.")

        elif escolha == '3':
            nome = input("Digite o NOME do contato para buscar: ").strip().title()
            if nome in agenda:
                print(f"🔎 Contato encontrado: **{nome}** - Telefone: **{agenda[nome]}**")
            else:
                print(f"⚠️ Contato '{nome}' não encontrado na agenda.")

        elif escolha == '4':
            if agenda:
                print("\nLista de Contatos:")
                for nome, telefone in agenda.items():
                    print(f"  - **{nome}**: {telefone}")
            else:
                print("⚠️ A agenda está vazia.")

        elif escolha == '5':
            print("👋 Saindo da Agenda de Contatos.")
            break

        else:
            print("🚫 Opção inválida. Por favor, tente novamente.")

# =================================================================
# Menu Principal para Executar as Atividades
# =================================================================
def menu_principal():
    """Exibe o menu principal e executa a função escolhida."""
    while True:
        print("\n=============================================")
        print("          Menu de Atividades Python          ")
        print("=============================================")
        print("1. 🛒 Lista de Compras Dinâmica")
        print("2. 🧑‍🎓 Dados de Aluno em Dicionário")
        print("3. 🔢 Separar Pares/Ímpares")
        print("4. 📞 DESAFIO EXTRA: Agenda de Contatos")
        print("5. Sair do Programa")
        print("---------------------------------------------")

        escolha = input("Escolha uma atividade para executar (1-5): ")

        if escolha == '1':
            gerenciar_lista_compras()
        elif escolha == '2':
            armazenar_dados_aluno()
        elif escolha == '3':
            separar_pares_impares()
        elif escolha == '4':
            gerenciar_agenda_contatos()
        elif escolha == '5':
            print("\nPrograma finalizado. Até mais! 👋")
            break
        else:
            print("🚫 Opção inválida. Digite um número de 1 a 5.")

# Execução do menu principal ao rodar o script
if __name__ == "__main__":
    menu_principal()