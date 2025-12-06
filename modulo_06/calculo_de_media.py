def calcular_media_e_status(notas):
    """
    Recebe uma lista de notas, calcula a média e determina o status de 
    aprovação (média >= 7.0).

    Parâmetros:
        notas (list): Uma lista contendo as notas do aluno (números float).
    """
    MEDIA_APROVACAO = 7.0
    
    # 1. Verifica se há notas para calcular
    if not notas:
        return "Nenhuma nota fornecida. Média não calculada."
    
    # 2. Calcula a média
    # sum() soma todos os elementos da lista
    # len() conta o número de elementos na lista
    media = sum(notas) / len(notas)
    
    # Arredonda a média para duas casas decimais
    media_arredondada = round(media, 2)
    
    # 3. Determina o status
    if media >= MEDIA_APROVACAO:
        status = "APROVADO! 🎉"
    else:
        status = "REPROVADO. 😔"
        
    # 4. Exibe o resultado
    print("\n--- 📝 Resultado do Aluno ---")
    print(f"Notas registradas: {notas}")
    print(f"Média Final: {media_arredondada}")
    print(f"Status: {status}")
    print("-----------------------------")


def coletar_notas_e_executar():
    """
    Coleta as notas do aluno dinamicamente via input e chama a função de cálculo.
    """
    
    notas_aluno = []
    print("--- 📚 Cálculo de Média e Status ---")
    print("Por favor, digite as notas do aluno.")
    print("Digite 'fim' para parar de adicionar notas e calcular a média.")

    # Loop para coletar notas
    while True:
        entrada = input("Digite a nota (ex: 8.5) ou 'fim': ").strip().lower()
        
        if entrada == 'fim':
            break
        
        try:
            # Tenta converter a entrada em um número de ponto flutuante (float)
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas_aluno.append(nota)
                print(f"Nota {nota} adicionada.")
            else:
                print("⚠️ Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("❌ Entrada inválida. Digite um número válido para a nota ou 'fim'.")

    # Verifica se alguma nota foi coletada antes de chamar a função
    if notas_aluno:
        # Chama a função de cálculo com as notas coletadas
        calcular_media_e_status(notas_aluno)
    else:
        print("\n❌ Nenhuma nota foi inserida. Não foi possível calcular a média.")


# Executa o programa
coletar_notas_e_executar()