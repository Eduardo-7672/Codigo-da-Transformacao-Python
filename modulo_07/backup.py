import shutil
import os
from datetime import datetime

def realizar_backup():
    print("\n--- 📂 Sistema de Backup com Shutil ---")
    
    # 1. Solicita os caminhos ao usuário
    # Dica: O usuário deve fornecer o caminho completo (ex: C:/Documentos/Projeto)
    origem = input("Digite o caminho da pasta de ORIGEM: ").strip()
    destino_base = input("Digite o caminho da pasta de DESTINO (Backup): ").strip()

    # 2. Valida se a pasta de origem existe
    if not os.path.exists(origem):
        print(f"❌ Erro: A pasta de origem '{origem}' não foi encontrada.")
        return

    # 3. Organização: Criar uma subpasta com a data atual dentro do destino
    # Isso evita que um backup sobrescreva o anterior
    data_hoje = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pasta_final_backup = os.path.join(destino_base, f"backup_{data_hoje}")

    try:
        # 4. Verifica se o destino base existe, se não, cria
        if not os.path.exists(destino_base):
            os.makedirs(destino_base)
            print(f"📁 Pasta de destino base criada em: {destino_base}")

        # 5. Realiza a cópia de toda a árvore de diretórios
        # shutil.copytree copia a pasta inteira e seus arquivos
        print(f"⏳ Iniciando backup de '{origem}' para '{pasta_final_backup}'...")
        
        shutil.copytree(origem, pasta_final_backup)
        
        print("\n==========================================")
        print(f"✅ BACKUP CONCLUÍDO COM SUCESSO!")
        print(f"📍 Local: {pasta_final_backup}")
        print(f"📊 Total de arquivos: {len(os.listdir(pasta_final_backup))}")
        print("==========================================")

    except FileExistsError:
        print(f"❌ Erro: Já existe um backup sendo feito neste exato segundo.")
    except PermissionError:
        print("❌ Erro de Permissão: Verifique se você tem acesso às pastas ou se algum arquivo está aberto.")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

# --- EXECUÇÃO ---
if __name__ == "__main__":
    realizar_backup()