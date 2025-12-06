import json
import os # Importamos 'os' para verificar se o arquivo existe

# Define o nome do arquivo JSON
NOME_ARQUIVO = "clientes.json"

def coletar_dados_cliente():
    """
    Coleta dados de um novo cliente dinamicamente do usuário.
    
    Retorna:
        dict: Um dicionário contendo os dados do cliente.
    """
    print("\n--- 👤 Cadastro de Novo Cliente ---")
    
    # Coleta de dados
    nome = input("Digite o nome completo do cliente: ").strip()
    email = input("Digite o e-mail do cliente: ").strip()
    telefone = input("Digite o telefone do cliente: ").strip()
    
    # Retorna os dados formatados
    return {
        "nome": nome,
        "email": email,
        "telefone": telefone
    }

def salvar_dados_json(dados):
    """
    Salva o dicionário de dados (clientes) em um arquivo JSON.
    
    Parâmetros:
        dados (dict): O dicionário de dados a ser salvo.
    """
    try:
        # Abrimos o arquivo no modo de escrita ('w')
        with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
            # json.dump() converte o dicionário Python para JSON e grava no arquivo
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        
        print(f"\n✅ Dados salvos com sucesso no arquivo '{NOME_ARQUIVO}'.")
    except IOError:
        print(f"\n❌ Erro ao salvar o arquivo '{NOME_ARQUIVO}'.")

def carregar_dados_json():
    """
    Carrega o dicionário de clientes de um arquivo JSON.
    
    Retorna:
        dict: O dicionário de clientes carregado, ou um dicionário vazio se falhar.
    """
    if not os.path.exists(NOME_ARQUIVO):
        print(f"\n⚠️ Arquivo '{NOME_ARQUIVO}' não encontrado. Iniciando com uma base vazia.")
        return {}
        
    try:
        # Abrimos o arquivo no modo de leitura ('r')
        with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            # json.load() lê o JSON do arquivo e o converte em um dicionário Python
            dados_carregados = json.load(arquivo)
            print(f"\n✅ Dados carregados com sucesso de '{NOME_ARQUIVO}'.")
            return dados_carregados
            
    except json.JSONDecodeError:
        print(f"\n❌ Erro: O arquivo '{NOME_ARQUIVO}' está corrompido ou não é um JSON válido.")
        return {}
    except IOError:
        print(f"\n❌ Erro ao ler o arquivo '{NOME_ARQUIVO}'.")
        return {}

def sistema_clientes_principal():
    """
    Função principal que gerencia o fluxo de coleta, salvamento e carregamento.
    """
    
    # 1. Carrega os dados existentes (se houver) para trabalhar com eles
    clientes_base = carregar_dados_json()
    
    # Se a base estiver vazia, inicializamos como um dicionário
    if not clientes_base:
        clientes_base = {}

    print(f"\n--- 💾 Sistema de Gerenciamento JSON ---")
    
    # 2. Coleta de Novos Dados (Dinamicamente)
    novo_cliente = coletar_dados_cliente()
    
    # Usamos o nome do cliente como uma chave única para armazenar o dicionário de dados
    chave_cliente = novo_cliente['nome'].strip().lower().replace(" ", "_")
    
    # Adiciona o novo cliente ao dicionário principal
    clientes_base[chave_cliente] = novo_cliente
    
    # 3. Salva a base de dados atualizada no arquivo JSON
    salvar_dados_json(clientes_base)
    
    # --- Demonstração de Carregamento e Exibição ---
    
    print("\n--- 📖 EXIBINDO DADOS APÓS CARREGAMENTO ---")
    
    # Carrega os dados novamente (simulando a reabertura do programa)
    dados_finais = carregar_dados_json()
    
    # Exibe os dados finais formatados
    if dados_finais:
        for chave, cliente in dados_finais.items():
            print(f"\nID da Base: {chave}")
            print(f"  Nome: {cliente['nome']}")
            print(f"  Email: {cliente['email']}")
            print(f"  Telefone: {cliente['telefone']}")
    else:
        print("Nenhum dado válido para exibir.")

# Executa o sistema
sistema_clientes_principal()