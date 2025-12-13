# =================================================================
# DESAFIO EXTRA: Sistema de Gerenciamento de Tarefas
# =================================================================

import sqlite3

def configurar_tarefas_db():
    """Configura e retorna a conexão com o banco de dados de tarefas."""
    
    nome_db = input("Digite o nome do arquivo do banco de dados de tarefas (ex: tarefas.db): ").strip()
    if not nome_db.endswith('.db'):
        nome_db += '.db'

    conn = None
    try:
        conn = sqlite3.connect(nome_db)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Pendente'
            );
        """)
        conn.commit()
        print(f"\n✅ Banco de dados '{nome_db}' e tabela 'Tarefas' configurados.")
        return conn
    except sqlite3.Error as e:
        print(f"❌ Erro ao configurar o banco de dados: {e}")
        return None

def adicionar_tarefa(conn):
    """Adiciona uma nova tarefa."""
    descricao = input("Digite a descrição da nova tarefa: ").strip()
    if not descricao:
        print("⚠️ A descrição da tarefa não pode ser vazia.")
        return

    sql = "INSERT INTO Tarefas (descricao) VALUES (?)"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (descricao,))
        conn.commit()
        print(f"✅ Tarefa '{descricao}' adicionada com sucesso! (ID: {cursor.lastrowid})")
    except sqlite3.Error as e:
        print(f"❌ Erro ao adicionar tarefa: {e}")

def visualizar_tarefas(conn):
    """Exibe todas as tarefas, mostrando status."""
    sql = "SELECT id, descricao, status FROM Tarefas ORDER BY id"
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        tarefas = cursor.fetchall()
        
        print("\n--- 📋 Lista de Tarefas ---")
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        print(f"{'ID':<5} {'Status':<12} {'Descrição':<50}")
        print("-" * 67)
        for id, descricao, status in tarefas:
            status_display = "✅ CONCLUÍDA" if status == 'Concluída' else "⏳ PENDENTE"
            print(f"{id:<5} {status_display:<12} {descricao:<50}")
            
    except sqlite3.Error as e:
        print(f"❌ Erro ao visualizar tarefas: {e}")

def excluir_tarefa(conn):
    """Exclui uma tarefa pelo ID."""
    try:
        tarefa_id = int(input("Digite o ID da tarefa a ser excluída: ").strip())
    except ValueError:
        print("❌ ID inválido. Por favor, digite um número.")
        return
    
    sql = "DELETE FROM Tarefas WHERE id = ?"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (tarefa_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"✅ Tarefa ID {tarefa_id} excluída com sucesso.")
        else:
            print(f"⚠️ Tarefa ID {tarefa_id} não encontrada.")
            
    except sqlite3.Error as e:
        print(f"❌ Erro ao excluir tarefa: {e}")

def sistema_tarefas():
    """Menu principal do sistema de gerenciamento de tarefas."""
    conn = configurar_tarefas_db()
    if not conn:
        return

    while True:
        print("\n" + "="*45)
        print("GERENCIAMENTO DE TAREFAS (TO-DO LIST)")
        print("="*45)
        print("1. Adicionar Tarefa")
        print("2. Visualizar Todas as Tarefas")
        print("3. Excluir Tarefa (pelo ID)")
        print("4. Sair")
        print("-" * 45)
        
        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == '1':
            adicionar_tarefa(conn)
        elif opcao == '2':
            visualizar_tarefas(conn)
        elif opcao == '3':
            excluir_tarefa(conn)
        elif opcao == '4':
            print("Encerrando o sistema de tarefas.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

    conn.close()

if __name__ == "__main__":
    sistema_tarefas()