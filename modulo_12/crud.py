# =================================================================
# ATIVIDADE 2: Implementar Operações CRUD
# =================================================================

import sqlite3

# Função auxiliar para conectar
def conectar_db(nome_db):
    try:
        conn = sqlite3.connect(nome_db)
        return conn
    except sqlite3.Error as e:
        print(f"❌ Erro de conexão com o banco de dados: {e}")
        return None

# --- Operações CRUD ---

def inserir_cliente(conn):
    """Insere um novo registro de cliente."""
    print("\n--- Inserir Novo Cliente ---")
    nome = input("Digite o nome do cliente: ").strip()
    email = input("Digite o email do cliente: ").strip()
    
    if not nome or not email:
        print("⚠️ Nome e e-mail são obrigatórios.")
        return

    sql = "INSERT INTO Clientes (nome, email) VALUES (?, ?)"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (nome, email))
        conn.commit()
        print(f"✅ Cliente '{nome}' inserido com sucesso! ID: {cursor.lastrowid}")
    except sqlite3.IntegrityError:
        print(f"❌ Erro de integridade: O e-mail '{email}' já está em uso.")
    except sqlite3.Error as e:
        print(f"❌ Erro ao inserir cliente: {e}")

def consultar_clientes(conn):
    """Consulta e exibe todos os registros de clientes."""
    sql = "SELECT id, nome, email FROM Clientes"
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        clientes = cursor.fetchall()
        
        print("\n--- Lista de Clientes ---")
        if not clientes:
            print("Nenhum cliente cadastrado.")
            return

        print(f"{'ID':<5} {'Nome':<20} {'Email':<30}")
        print("-" * 55)
        for id, nome, email in clientes:
            print(f"{id:<5} {nome:<20} {email:<30}")
            
    except sqlite3.Error as e:
        print(f"❌ Erro ao consultar clientes: {e}")

def atualizar_cliente(conn):
    """Atualiza o nome e/ou email de um cliente existente."""
    print("\n--- Atualizar Cliente ---")
    try:
        cliente_id = int(input("Digite o ID do cliente a ser atualizado: ").strip())
    except ValueError:
        print("❌ ID inválido. Por favor, digite um número.")
        return

    novo_nome = input("Novo nome (deixe vazio para manter): ").strip()
    novo_email = input("Novo email (deixe vazio para manter): ").strip()
    
    if not novo_nome and not novo_email:
        print("⚠️ Nenhuma alteração fornecida.")
        return

    # Constrói o comando SQL dinamicamente
    updates = []
    params = []
    
    if novo_nome:
        updates.append("nome = ?")
        params.append(novo_nome)
    if novo_email:
        updates.append("email = ?")
        params.append(novo_email)

    if updates:
        sql = f"UPDATE Clientes SET {', '.join(updates)} WHERE id = ?"
        params.append(cliente_id)
        
        try:
            cursor = conn.cursor()
            cursor.execute(sql, tuple(params))
            conn.commit()
            
            if cursor.rowcount > 0:
                print(f"✅ Cliente ID {cliente_id} atualizado com sucesso.")
            else:
                print(f"⚠️ Cliente ID {cliente_id} não encontrado.")
                
        except sqlite3.IntegrityError:
             print(f"❌ Erro de integridade: O novo e-mail '{novo_email}' já está em uso.")
        except sqlite3.Error as e:
            print(f"❌ Erro ao atualizar cliente: {e}")


def deletar_cliente(conn):
    """Deleta um registro de cliente."""
    print("\n--- Deletar Cliente ---")
    try:
        cliente_id = int(input("Digite o ID do cliente a ser deletado: ").strip())
    except ValueError:
        print("❌ ID inválido. Por favor, digite um número.")
        return
    
    sql = "DELETE FROM Clientes WHERE id = ?"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (cliente_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"✅ Cliente ID {cliente_id} deletado com sucesso.")
        else:
            print(f"⚠️ Cliente ID {cliente_id} não encontrado.")
            
    except sqlite3.Error as e:
        print(f"❌ Erro ao deletar cliente: {e}")

# --- Menu Principal ---

def menu_crud():
    """Função principal que orquestra o menu CRUD."""
    
    nome_db = input("Digite o nome do arquivo do banco de dados (ex: clientes.db) para o CRUD: ").strip()
    if not nome_db.endswith('.db'):
        nome_db += '.db'

    conn = conectar_db(nome_db)
    if not conn:
        return

    # Garante que a tabela exista antes de operar (chamada da Atividade 1)
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"❌ Não foi possível garantir a criação da tabela Clientes: {e}")
        conn.close()
        return

    while True:
        print("\n" + "="*40)
        print(f"GERENCIAMENTO DE CLIENTES ({nome_db})")
        print("="*40)
        print("1. Inserir Novo Cliente")
        print("2. Consultar Todos os Clientes")
        print("3. Atualizar Cliente (Nome/Email)")
        print("4. Deletar Cliente")
        print("5. Sair")
        print("-" * 40)
        
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == '1':
            inserir_cliente(conn)
        elif opcao == '2':
            consultar_clientes(conn)
        elif opcao == '3':
            atualizar_cliente(conn)
        elif opcao == '4':
            deletar_cliente(conn)
        elif opcao == '5':
            print("Encerrando o gerenciamento do banco de dados.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

    conn.close()

if __name__ == "__main__":
    menu_crud()