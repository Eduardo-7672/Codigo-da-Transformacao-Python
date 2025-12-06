# A base de armazenamento de dados (dicionário global que contém todos os logins e senhas)
dados_login = {}

def verificar_existencia_usuario(usuario):
    """Verifica se um nome de usuário já existe na base de dados."""
    return usuario in dados_login

def validar_senha(senha):
    """Verifica se a senha tem no mínimo 8 caracteres."""
    return len(senha) >= 8

def cadastrar_usuario():
    """
    Solicita cadastro de usuário e senha, validando se o usuário já existe 
    e se a senha tem o tamanho mínimo (8 caracteres).
    """
    global dados_login
    print("\n--- 🔒 CADASTRO DE NOVO USUÁRIO ---")
    
    while True:
        novo_usuario = input("Escolha um nome de usuário: ").strip()
        if not novo_usuario:
            print("❌ O nome de usuário não pode ser vazio.")
            continue
        
        # Base de Dados: Verifica se o nome já existe
        if verificar_existencia_usuario(novo_usuario):
            print("⚠️ Usuário já cadastrado. Por favor, escolha outro nome.")
            continue
        break

    while True:
        nova_senha = input("Escolha uma senha (mínimo 8 caracteres): ").strip()
        if not nova_senha:
            print("❌ A senha não pode ser vazia.")
            continue
        
        if not validar_senha(nova_senha):
            print("❌ Senha muito curta. A senha deve ter no mínimo 8 caracteres.")
            continue
        break
    
    # Base de Dados: Armazena o novo par (login: senha)
    dados_login[novo_usuario] = nova_senha
    print(f"\n✅ Usuário '{novo_usuario}' cadastrado com sucesso na base de dados!")

def validar_login(usuario, senha):
    """
    Verifica se o usuário existe e se a senha está correta na base de dados.
    """
    if verificar_existencia_usuario(usuario):
        # Base de Dados: Compara a senha fornecida com a senha armazenada
        if dados_login[usuario] == senha:
            return True
    return False

# --- FUNÇÃO PRINCIPAL SOLICITADA ---
def redefinir_senha():
    """
    Acessa a base de dados para verificar a existência do usuário e permite
    a redefinição da senha com validação de 8 caracteres.
    """
    global dados_login
    print("\n--- 🔑 REDEFINIR SENHA ---")
    
    usuario_redefinir = input("Digite seu nome de usuário: ").strip()

    # Base de Dados: Verifica a existência do usuário
    if verificar_existencia_usuario(usuario_redefinir):
        print(f"Usuário '{usuario_redefinir}' encontrado na base.")
        
        while True:
            nova_senha = input("Digite a NOVA senha (mínimo 8 caracteres): ").strip()
            
            if not validar_senha(nova_senha):
                print("❌ Senha muito curta. A senha deve ter no mínimo 8 caracteres.")
                continue
            
            # Base de Dados: ATUALIZA a senha para o usuário existente
            dados_login[usuario_redefinir] = nova_senha
            print(f"\n✅ Senha do usuário '{usuario_redefinir}' redefinida com sucesso!")
            break
    else:
        print(f"❌ Erro: Usuário '{usuario_redefinir}' não encontrado na base de dados.")
# -----------------------------------

def realizar_login():
    """
    Gerencia a tentativa de login.
    """
    print("\n--- 🔑 TENTATIVA DE LOGIN ---")
    
    login_usuario = input("Nome de usuário: ").strip()
    login_senha = input("Senha: ").strip()
    
    if validar_login(login_usuario, login_senha):
        print("\n==================================")
        print(f"🎉 LOGIN BEM-SUCEDIDO! Bem-vindo(a), {login_usuario}.")
        print("==================================")
        return True
    else:
        print("❌ Falha no login: Usuário ou senha incorretos.")
        return False

def sistema_login_principal():
    """
    Função principal que gerencia o menu de interação.
    """
    print("Bem-vindo(a) ao Sistema de Gerenciamento de Usuários!")
    
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print(f"Total de usuários cadastrados: {len(dados_login)}")
        print("1. Cadastrar Novo Usuário")
        print("2. Fazer Login")
        print("3. Redefinir Senha")
        print("4. Sair")
        print("----------------------")
        
        escolha = input("Escolha uma opção (1-4): ").strip()
        
        if escolha == '1':
            cadastrar_usuario()
        elif escolha == '2':
            if realizar_login():
                break
        elif escolha == '3':
            redefinir_senha()
        elif escolha == '4':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("❌ Opção inválida. Por favor, escolha um número entre 1 e 4.")

# Inicia o sistema
sistema_login_principal()