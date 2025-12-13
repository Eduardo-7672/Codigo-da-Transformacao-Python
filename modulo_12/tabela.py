# =================================================================
# ATIVIDADE 1: Criar Tabela Clientes (SQLite)
# =================================================================

import sqlite3
import os

def criar_tabela_clientes():
    """Cria um banco de dados e a tabela Clientes com as colunas id, nome e email."""
    
    # 1. Coleta o nome do banco de dados do usuário
    nome_db = input("Digite o nome do arquivo do banco de dados (ex: clientes.db): ").strip()
    if not nome_db.endswith('.db'):
        nome_db += '.db'
        
    # Conexão com o banco de dados (será criado se não existir)
    conn = None
    try:
        conn = sqlite3.connect(nome_db)
        cursor = conn.cursor()

        # 2. Comando SQL para criar a tabela
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        """)

        # Confirma a transação
        conn.commit()
        print(f"\n✅ Banco de dados '{nome_db}' e tabela 'Clientes' criados com sucesso!")
        
    except sqlite3.Error as e:
        print(f"\n❌ Erro ao criar a tabela: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    criar_tabela_clientes()