# --- 1. GERENCIADOR DINÂMICO DE LISTA DE COMPRAS (Função Interativa) ---
def gerenciador_lista_compras():
    """Gerencia uma lista de compras interativa."""
    lista_de_compras = []

    while True:
        print("\n--- 🛒 Lista de Compras ---")
        print("1. Adicionar Item")
        print("2. Remover Item")
        print("3. Visualizar Lista")
        print("4. Sair")

        escolha = input("Escolha uma opção (1-4): ")

        if escolha == '1':
            item = input("Digite o item a adicionar: ").strip().capitalize()
            if item:
                lista_de_compras.append(item)
                print(f"'{item}' adicionado à lista.")

        elif escolha == '2':
            if not lista_de_compras:
                print("A lista está vazia, nada para remover.")
                continue

            print("\nItens Atuais:")
            for i, item in enumerate(lista_de_compras):
                print(f"{i + 1}. {item}")

            try:
                indice_remover = int(input("Digite o número do item que deseja remover: ")) - 1
                
                if 0 <= indice_remover < len(lista_de_compras):
                    item_removido = lista_de_compras.pop(indice_remover)
                    print(f"'{item_removido}' removido da lista.")
                else:
                    print("Número de item inválido.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        elif escolha == '3':
            if lista_de_compras:
                print("\nLista de Compras Atual:")
                for item in lista_de_compras:
                    print(f"- {item}")
            else:
                print("A lista de compras está vazia.")

        elif escolha == '4':
            print("Saindo do Gerenciador de Lista de Compras. Boas compras!")
            break

        else:
            print("Opção inválida.")


# --- 2. ARMAZENANDO DADOS DE UM ALUNO EM UM DICIONÁRIO ---
def exibir_dados_aluno():
    """Armazena e exibe dados de um aluno usando um dicionário."""
    dados_aluno = {
        "nome": "Maria Silva",
        "idade": 21,
        "curso": "Engenharia de Software",
        "notas": {
            "Matemática": 9.5,
            "Programação": 10.0,
            "História": 7.8
        }
    }

    print("\n\n--- 🧑‍🎓 Dados do Aluno ---")
    for chave, valor in dados_aluno.items():
        if chave == "notas":
            print(f"**Notas:**")
            for materia, nota in valor.items():
                print(f"  - {materia}: {nota}")
        else:
            print(f"**{chave.capitalize()}:** {valor}")


# --- 3. SEPARANDO NÚMEROS PARES E ÍMPARES ---
def separar_pares_impares():
    """Percorre um conjunto de números e separa pares e ímpares."""
    conjunto_de_numeros = [12, 7, 25, 4, 30, 1, 9, 22, 16]

    pares = []
    impares = []

    for numero in conjunto_de_numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    print("\n\n--- 🔢 Separação de Pares e Ímpares ---")
    print(f"Conjunto original: {conjunto_de_numeros}")
    print(f"**Números Pares:** {pares}")
    print(f"**Números Ímpares:** {impares}")


# --- 4. DESAFIO EXTRA: SISTEMA DE AGENDA DE CONTATOS (Função Interativa) ---
def sistema_agenda_contatos():
    """Desenvolve um sistema de agenda de contatos usando dicionários."""
    agenda = {}

    while True:
        print("\n--- 📞 Agenda de Contatos ---")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Buscar Contato")
        print("4. Listar Todos")
        print("5. Sair")

        escolha = input("Escolha uma opção (1-5): ")

        if escolha == '1':
            nome = input("Digite o NOME do contato: ").strip()
            telefone = input("Digite o TELEFONE do contato: ").strip()

            if nome and telefone:
                agenda[nome] = telefone
                print(f"Contato '{nome}' adicionado com sucesso.")

        elif escolha == '2':
            nome = input("Digite o NOME do contato para remover: ").strip()
            if nome in agenda:
                del agenda[nome]
                print(f"Contato '{nome}' removido.")
            else:
                print(f"Erro: Contato '{nome}' não encontrado na agenda.")

        elif escolha == '3':
            nome = input("Digite o NOME do contato para buscar: ").strip()
            telefone = agenda.get(nome) 

            if telefone:
                print(f"**{nome}:** {telefone}")
            else:
                print(f"Erro: Contato '{nome}' não encontrado.")

        elif escolha == '4':
            if agenda:
                print("\n--- Todos os Contatos ---")
                for nome, telefone in agenda.items():
                    print(f"**{nome}:** {telefone}")
            else:
                print("A agenda de contatos está vazia.")

        elif escolha == '5':
            print("Saindo do Sistema de Agenda. Até logo!")
            break

        else:
            print("Opção inválida.")


# ===============================================
# === EXECUÇÃO DOS PROGRAMAS (Rode um por vez) ===
# ===============================================

# 1. Execute o programa da Lista de Compras (Interativo)
# gerenciador_lista_compras() 

# 2. Execute o programa de Dados do Aluno (Simples)
exibir_dados_aluno()

# 3. Execute o programa de Pares e Ímpares (Simples)
separar_pares_impares()

# 4. Execute o programa da Agenda de Contatos (Interativo)
# sistema_agenda_contatos()