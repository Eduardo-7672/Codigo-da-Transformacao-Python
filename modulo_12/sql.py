# =================================================================
# ATIVIDADE 3: Executar Consultas SQL para Filtrar Dados
# =================================================================

import sqlite3

def executar_consulta_filtrada():
    """Permite ao usuário digitar uma condição SQL para filtrar clientes."""
    
    nome_db = input("Digite o nome do arquivo do banco de dados (ex: clientes.db): ").strip()
    if not nome_db.endswith('.db'):
        nome_db += '.db'
        
    conn = None
    try:
        conn = sqlite3.connect(nome_db)
        cursor = conn.cursor()

        print("\n--- 🔎 Filtro de Clientes (Consultas Avançadas) ---")
        print("Exemplos: nome LIKE 'A%' (nomes que começam com A)")
        print("          email LIKE '%@gmail.com' (e-mails do gmail)")
        
        # Coleta a condição de filtro do usuário
        condicao_where = input("Digite a condição SQL (cláusula WHERE, ex: nome LIKE 'A%'): ").strip()
        
        if not condicao_where:
            print("❌ Condição de filtro não fornecida.")
            return

        # Constrói o comando SQL completo
        sql = f"SELECT id, nome, email FROM Clientes WHERE {condicao_where}"
        
        cursor.execute(sql)
        clientes = cursor.fetchall()
        
        print(f"\n✅ Resultados da Consulta (WHERE {condicao_where}):")
        
        if not clientes:
            print("Nenhum cliente encontrado com este filtro.")
            return

        print(f"{'ID':<5} {'Nome':<20} {'Email':<30}")
        print("-" * 55)
        for id, nome, email in clientes:
            print(f"{id:<5} {nome:<20} {email:<30}")
            
    except sqlite3.OperationalError as e:
        print(f"❌ Erro de Operação SQL: {e}. Verifique se a sintaxe da sua condição SQL está correta.")
    except sqlite3.Error as e:
        print(f"❌ Erro no banco de dados: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    executar_consulta_filtrada()