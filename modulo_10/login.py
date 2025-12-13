# =================================================================
# DESAFIO EXTRA: Sistema de Login com Múltiplas Tentativas
# =================================================================

class CredenciaisInvalidasError(Exception):
    """Exceção levantada quando o login ou senha estão incorretos."""
    pass

def sistema_login():
    """Simula um login com tratamento de erros, exceção e limite de tentativas."""
    print("\n--- 🔐 Sistema de Login ---")
    
    # 1. Usuário define as credenciais corretas (sem dados prontos)
    print("Por favor, defina as credenciais do sistema (para teste):")
    USUARIO_CORRETO = input("   Defina o nome de usuário CORRETO: ").strip()
    SENHA_CORRETA = input("   Defina a senha CORRETA: ").strip()
    MAX_TENTATIVAS = 3
    
    if not USUARIO_CORRETO or not SENHA_CORRETA:
        print("⚠️ Usuário e Senha não podem ser vazios. Abortando login.")
        return

    tentativas = 0
    while tentativas < MAX_TENTATIVAS:
        print(f"\nTentativa {tentativas + 1} de {MAX_TENTATIVAS}:")
        
        # 2. Usuário tenta logar
        usuario_digitado = input("   Usuário: ").strip()
        senha_digitada = input("   Senha: ").strip()
        
        try:
            if usuario_digitado != USUARIO_CORRETO or senha_digitada != SENHA_CORRETA:
                # Levanta a exceção personalizada quando há falha
                raise CredenciaisInvalidasError("Usuário ou senha incorretos.")
            
            # Se o login for bem-sucedido
            print(f"\n🎉 Login bem-sucedido! Bem-vindo(a), {USUARIO_CORRETO}!")
            return
            
        except CredenciaisInvalidasError as e:
            # Captura a exceção, incrementa o contador e informa o erro
            tentativas += 1
            print(f"❌ Erro de Login: {e}. Tente novamente.")
            
        except Exception as e:
            # Trata qualquer outro erro
            print(f"❌ Ocorreu um erro inesperado durante o login: {e}")
            break
        
    # Se o loop terminar sem sucesso
    if tentativas == MAX_TENTATIVAS:
        print(f"\n🛑 Número máximo de tentativas ({MAX_TENTATIVAS}) excedido. Acesso bloqueado.")

if __name__ == "__main__":
    sistema_login()