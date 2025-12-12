import os
import sys
import json
import csv
import re
import shutil
from datetime import datetime
from pathlib import Path

# =================================================================
# I. FUNÇÕES DO MÓDULO DE VALIDAÇÃO (utilidades/validadores.py)
# =================================================================

def validar_email(email):
    """Verifica se o email tem um formato básico válido."""
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return bool(re.search(regex, email, re.IGNORECASE))

def validar_cpf(cpf_bruto):
    """Simulação de validação de CPF (Simplificado)."""
    cpf = re.sub(r'\D', '', cpf_bruto)
    return len(cpf) == 11 and cpf != cpf[0] * 11

def validar_dados_usuario(dados_usuario):
    """Verifica nome, email e documento."""
    if not dados_usuario.get('nome'):
        return False, "O nome não pode ser vazio."
    if not validar_email(dados_usuario.get('email', '')):
        return False, "O email é inválido."
    if not validar_cpf(dados_usuario.get('documento', '')):
        return False, "O documento (CPF/SSN) é inválido ou incompleto."
    return True, "Dados válidos."

def obter_caminho_valido(prompt):
    """Função para obter e validar caminhos de pasta (usado no backup)."""
    while True:
        caminho_input = input(prompt).strip().replace('"', '').replace("'", "")
        if not caminho_input:
             print("❌ O caminho não pode ser vazio.")
             continue
        try:
            caminho = Path(caminho_input).resolve()
            if caminho.is_dir():
                return caminho
            # Permite o caminho de destino mesmo que não exista ainda, se for criar
            if "DESTINO" in prompt.upper() and not caminho.exists():
                 return caminho
            
            print(f"❌ Erro: O caminho '{caminho_input}' não é uma pasta válida ou não existe.")
        except Exception as e:
             print(f"❌ Erro ao processar o caminho: {e}")

# =================================================================
# II. FUNÇÕES DO MÓDULO DE EXPORTAÇÃO (utilidades/exportador.py)
# =================================================================

def exportar_para_csv(dados_dict, nome_arquivo):
    """Exporta dados de dicionário para CSV."""
    if not dados_dict:
        return False, "Nenhum dado para exportar."

    dados_lista = [v for k, v in dados_dict.items()]
    chaves = dados_lista[0].keys()

    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=chaves)
            writer.writeheader()
            writer.writerows(dados_lista)
        return True, f"Dados exportados com sucesso para {nome_arquivo}"
    except Exception as e:
        return False, f"Erro na exportação CSV: {e}"

# =================================================================
# III. FUNÇÕES DO MÓDULO DE GERENCIAMENTO (core/gerenciador.py)
# =================================================================

ARQUIVO_DADOS = "data/usuarios.json"

# --- Funções CRUD ---

def carregar_dados():
    """Carrega dados do arquivo JSON ou retorna um dicionário vazio."""
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def salvar_dados(dados):
    """Salva o dicionário de dados no arquivo JSON."""
    try:
        with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        return True
    except IOError:
        return False

def adicionar_usuario(novo_usuario):
    """Adiciona um novo usuário após a validação."""
    valido, mensagem = validar_dados_usuario(novo_usuario)
    if not valido:
        return False, f"Falha na Adição: {mensagem}"
    
    dados = carregar_dados()
    user_id = str(len(dados) + 1)
    dados[user_id] = novo_usuario
    
    if salvar_dados(dados):
        return True, f"Usuário {novo_usuario['nome']} adicionado com ID {user_id}."
    else:
        return False, "Erro ao salvar no disco."

# --- Funções de Backup ---

def realizar_backup_projeto():
    """Realiza o backup do projeto principal (cópia de pastas)."""
    print("\n--- 🛡️ Backup de Pastas do Projeto ---")
    
    try:
        # Pede caminho de ORIGEM (deve existir)
        origem = obter_caminho_valido("📂 Digite o caminho da pasta de ORIGEM para backup: ")
        
        # Pede caminho de DESTINO (pode ou não existir)
        destino_base = obter_caminho_valido("🎯 Digite o caminho da pasta de DESTINO: ")

        data_hoje = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        pasta_final_backup = destino_base / f"backup_manual_{data_hoje}"

        # Garante que a pasta de destino base exista
        destino_base.mkdir(parents=True, exist_ok=True)

        print(f"\n⏳ Iniciando cópia de '{origem}' para '{pasta_final_backup}'...")
        
        shutil.copytree(origem, pasta_final_backup)
        
        return True, f"Backup concluído com sucesso em: {pasta_final_backup}"

    except PermissionError:
        return False, "Erro de Permissão: Verifique se você tem acesso às pastas."
    except Exception as e:
        return False, f"Ocorreu um erro inesperado: {e}"

# =================================================================
# IV. PROGRAMA PRINCIPAL (main.py)
# =================================================================

def coletar_input_usuario():
    """Coleta dados do usuário via input."""
    print("\n--- 📝 Cadastro de Novo Usuário ---")
    
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()
    documento = input("Documento (CPF/SSN - apenas números): ").strip()
    
    return {
        "nome": nome,
        "email": email,
        "documento": documento,
        "data_cadastro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def exibir_usuarios():
    """Lê e exibe todos os usuários do sistema."""
    print("\n--- Usuários Atuais Cadastrados ---")
    dados = carregar_dados()
    if not dados:
        print("Nenhum usuário cadastrado.")
        return

    # Usando formatação de string para alinhamento de tabela
    print(f"{'ID':<5} | {'NOME':<25} | {'E-MAIL':<35} | {'DOCUMENTO':<15}")
    print("-" * 85)
    
    for uid, user in dados.items():
        print(f"{uid:<5} | {user['nome']:<25} | {user['email']:<35} | {user['documento']:<15}")
    print("-" * 85)

def menu_principal():
    """Orquestra o sistema modular."""
    
    # Cria a pasta data/ se ela não existir, para salvar o JSON
    if not os.path.exists("data"):
        os.makedirs("data")

    while True:
        print("\n" + "="*60)
        print("SISTEMA DE GERENCIAMENTO MODULAR UNIFICADO")
        print("="*60)
        print("1. Adicionar Novo Usuário")
        print("2. Exibir Todos os Usuários")
        print("3. Exportar Usuários para CSV")
        print("4. Realizar Backup de Pastas (shutil)")
        print("5. Sair")
        print("-" * 60)

        opcao = input("Escolha a funcionalidade (1-5): ").strip()

        if opcao == '1':
            novo_usuario = coletar_input_usuario()
            sucesso, mensagem = adicionar_usuario(novo_usuario)
            print(f"\n[Status]: {mensagem}")
            
        elif opcao == '2':
            exibir_usuarios()
            
        elif opcao == '3':
            dados = carregar_dados()
            sucesso_export, msg_export = exportar_para_csv(dados, "data/backup_usuarios.csv")
            print(f"\n[Status da Exportação]: {msg_export}")
            
        elif opcao == '4':
            sucesso_backup, msg_backup = realizar_backup_projeto()
            print(f"\n[Status do Backup]: {msg_backup}")
            
        elif opcao == '5':
            print("Encerrando o sistema modular. Até logo!")
            break
            
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()