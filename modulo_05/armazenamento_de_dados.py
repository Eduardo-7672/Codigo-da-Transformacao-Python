def armazenar_e_exibir_dados_aluno_dinamico():
    """
    Solicita ao usuário os dados de um aluno (nome, idade e notas), 
    armazena em um dicionário e exibe as informações.
    """
    
    print("\n--- 📝 Coleta de Dados do Aluno ---")

    # 1. Coleta do Nome e Idade
    # Usamos .strip() para remover espaços em branco extras
    nome = input("Digite o nome completo do aluno: ").strip()
    
    while True:
        try:
            idade = int(input(f"Digite a idade de {nome}: "))
            if idade <= 0:
                 print("A idade deve ser um número positivo.")
                 continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

    # 2. Coleta das Notas (usando um loop para coletar múltiplas notas)
    notas = {}
    print("\n--- Cadastro de Notas ---")
    print("Digite 'fim' para terminar a adição de notas.")
    
    while True:
        materia = input("Digite o nome da disciplina (ou 'fim'): ").strip()
        
        if materia.lower() == 'fim':
            if not notas:
                print("⚠️ Nenhuma nota foi adicionada. Por favor, adicione pelo menos uma disciplina.")
                continue
            break
        
        while True:
            try:
                # Usamos float para permitir notas com casas decimais
                nota = float(input(f"Digite a nota de '{materia}': "))
                if 0 <= nota <= 10:
                    notas[materia] = nota
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número para a nota.")

    # 3. Criação do Dicionário Final
    dados_aluno = {
        "nome": nome,
        "idade": idade,
        "notas": notas
    }

    # 4. Exibição dos Dados Armazenados
    print("\n\n--- 📊 Dados Finais Armazenados ---")
    print("---------------------------------------")
    
    print(f"**Nome:** {dados_aluno['nome']}")
    print(f"**Idade:** {dados_aluno['idade']} anos")

    print("\n**Notas por Disciplina:**")
    # Itera sobre o dicionário de notas
    for materia, nota in dados_aluno['notas'].items():
        print(f"- {materia}: {nota}")
    
    print("---------------------------------------")

# Executa a função para iniciar o processo de entrada de dados
armazenar_e_exibir_dados_aluno_dinamico() 