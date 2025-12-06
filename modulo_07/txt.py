# Define o nome do arquivo que será usado
NOME_ARQUIVO = "dados_usuario_telefone_puro.txt"

def validar_e_coletar(prompt, tipo='texto'):
    """
    Função auxiliar que solicita entrada ao usuário e aplica validações rigorosas
    baseadas no tipo de dado esperado.
    """
    while True:
        entrada_bruta = input(prompt).strip()
        
        # 1. Validação de Vazio
        if not entrada_bruta:
            print("❌ Este campo não pode ser deixado em branco.")
            continue
        
        # 2. Validação Específica por Tipo
        
        if tipo == 'numero':
            # *** ALTERAÇÃO AQUI: APENAS DÍGITOS SÃO PERMITIDOS ***
            if entrada_bruta.isdigit():
                return entrada_bruta
            else:
                print("❌ ENTRADA INVÁLIDA. Digite APENAS números para este campo (sem hífens ou letras).")
        
        elif tipo == 'email':
            # Validação simples: deve conter '@' e '.'
            if '@' in entrada_bruta and '.' in entrada_bruta:
                return entrada_bruta.lower()
            else:
                print("❌ E-mail inválido. Certifique-se de incluir '@' e '.'.")

        elif tipo == 'texto':
            # Validação Rigorosa para Nome/Cidade: APENAS letras e espaços.
            if all(c.isalpha() or c.isspace() for c in entrada_bruta):
                return entrada_bruta.capitalize()
            else:
                print("❌ ENTRADA INVÁLIDA. Este campo deve conter APENAS letras e espaços (sem números ou sinais).")

        elif tipo == 'endereco':
            # Validação Flexível para Endereço: Permite letras, números, espaços e sinais comuns.
            caracteres_permitidos = ".,-/#º" 
            
            if all(c.isalnum() or c.isspace() or c in caracteres_permitidos for c in entrada_bruta):
                return entrada_bruta.capitalize()
            else:
                print("❌ ENDEREÇO INVÁLIDO. Use letras, números e pontuações comuns (como . , -).")

def coletar_dados_usuario():
    """
    Solicita informações completas ao usuário usando validação rigorosa.
    """
    print("\n--- 📝 Coleta de Dados para Arquivo (Rigorosa) ---")
    
    # Coleta e Validação Rigorosa
    nome = validar_e_coletar("Digite seu nome (apenas letras): ", tipo='texto')
    idade = validar_e_coletar("Digite sua idade (apenas números): ", tipo='numero')
    cidade = validar_e_coletar("Digite sua cidade (apenas letras): ", tipo='texto')
    email = validar_e_coletar("Digite seu e-mail: ", tipo='email')
    
    # Campo Endereço (Flexível)
    endereco = validar_e_coletar("Digite seu endereço completo (letras, números e pontuação permitidos): ", tipo='endereco')
    
    # *** CAMPO TELEFONE: AGORA SOMENTE NÚMEROS ***
    telefone = validar_e_coletar("Digite seu número de telefone (SOMENTE NÚMEROS, ex: 99999999999): ", tipo='numero')
    
    # Formata as informações para gravação
    dados_formatados = [
        f"Nome: {nome}\n",
        f"Idade: {idade}\n",
        f"Cidade: {cidade}\n",
        f"E-mail: {email}\n",
        f"Endereço: {endereco}\n",
        f"Telefone: {telefone}\n",
        "--- Fim dos Dados ---\n"
    ]
    return dados_formatados

def gravar_arquivo(dados):
    """Grava as informações fornecidas no arquivo, sobrescrevendo o conteúdo."""
    try:
        with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(dados)
        print(f"\n✅ Informações gravadas com sucesso no arquivo '{NOME_ARQUIVO}'.")
    except IOError:
        print(f"\n❌ Erro ao gravar o arquivo '{NOME_ARQUIVO}'.")

def ler_arquivo():
    """Lê todo o conteúdo do arquivo e o imprime no console."""
    try:
        with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        
        print(f"\n--- Conteúdo Lido de '{NOME_ARQUIVO}' ---")
        print(conteudo)
        print("-----------------------------------------")
        
    except FileNotFoundError:
        print(f"\n❌ Erro: O arquivo '{NOME_ARQUIVO}' não foi encontrado.")
    except IOError:
        print(f"\n❌ Erro ao ler o arquivo '{NOME_ARQUIVO}'.")

# --- EXECUÇÃO DO PROGRAMA ---

# 1. Coleta os dados, garantindo que sejam válidos
dados_do_usuario = coletar_dados_usuario()

# 2. Grava os dados
gravar_arquivo(dados_do_usuario)

# 3. Lê o conteúdo
ler_arquivo()