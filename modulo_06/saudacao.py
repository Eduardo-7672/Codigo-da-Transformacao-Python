def saudacao(nome):
    """
    Função que recebe um nome como parâmetro e imprime uma saudação personalizada.

    Parâmetros:
        nome (str): O nome da pessoa a ser saudada.
    """
    if nome:
        print(f"🎉 Olá, {nome}! Que bom te ver. Tenha um excelente dia!")
    else:
        # Fallback
        print("👋 Olá! É um prazer tê-lo(a) por aqui.")

# --- Execução Dinâmica e Validação (Robusta) ---

print("--- Saudação Personalizada ---")

while True:
    # 1. Solicita o nome ao usuário
    # Remove espaços em branco nas extremidades
    nome_do_usuario_bruto = input("Por favor, digite seu nome: ").strip()
    
    # Capitaliza (apenas para exibição futura)
    nome_do_usuario = nome_do_usuario_bruto.capitalize()

    # 2. NOVA VALIDAÇÃO: Verifica se a string não está vazia E se contém pelo menos uma letra.
    # O 'any(c.isalpha() for c in nome_do_usuario_bruto)' garante que não são aceitos apenas números ou sinais.
    if nome_do_usuario_bruto and any(c.isalpha() for c in nome_do_usuario_bruto):
        
        # Se o nome for válido (contém letras), chama a função e sai do loop
        saudacao(nome_do_usuario)
        break
    else:
        # 3. Se o nome estiver vazio ou só tiver números/sinais, exibe a mensagem de erro
        print("\n⚠️ Entrada inválida. Você deve digitar um nome que contenha pelo menos uma letra.")
        
        # Solicita a ação de reinício
        tentar_novamente = input("Deseja tentar novamente? (s/n ou sim/não): ").strip().lower()

        if tentar_novamente in ('s', 'sim'):
            # Reinicia a pergunta
            print("Reiniciando a pergunta...")
            continue
            
        elif tentar_novamente in ('n', 'não', 'nao'):
            # Sai do programa
            print("Saindo do programa de saudação. Até logo!")
            break
            
        else:
            # Encerra o programa devido à resposta inválida
            print("❌ Resposta inválida. O programa será encerrado.")
            break