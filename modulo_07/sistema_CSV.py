import csv
import os

# Nome do arquivo onde os dados serão armazenados
ARQUIVO_CSV = "notas_alunos.csv"

def validar_nota():
    """Garante que a nota digitada seja um número entre 0 e 10."""
    while True:
        try:
            nota = float(input("Digite a nota do aluno (0 a 10): ").replace(',', '.'))
            if 0 <= nota <= 10:
                return nota
            else:
                print("❌ Erro: A nota deve estar entre 0 e 10.")
        except ValueError:
            print("❌ Erro: Por favor, digite um número válido.")

def adicionar_nota():
    """Coleta dados do usuário e salva no arquivo CSV."""
    print("\n--- 📝 Adicionar Nova Nota ---")
    
    # Validação simples de nome (apenas letras)
    while True:
        nome = input("Digite o nome do aluno: ").strip().capitalize()
        if nome and all(c.isalpha() or c.isspace() for c in nome):
            break
        print("❌ Erro: O nome deve conter apenas letras e não pode ser vazio.")

    nota = validar_nota()

    # Verifica se o arquivo já existe para decidir se escreve o cabeçalho
    arquivo_existe = os.path.exists(ARQUIVO_CSV)

    try:
        # 'a' (append) adiciona ao final do arquivo sem apagar o que já existe
        with open(ARQUIVO_CSV, mode='a', newline='', encoding='utf-8') as arquivo:
            campos = ['Nome', 'Nota']
            escritor = csv.DictWriter(arquivo, fieldnames=campos)

            # Se o arquivo for novo, escreve o cabeçalho (Nome, Nota)
            if not arquivo_existe:
                escritor.writeheader()

            # Escreve os dados do aluno
            escritor.writerow({'Nome': nome, 'Nota': nota})
            
        print(f"✅ Nota de {nome} salva com sucesso!")
    except IOError:
        print("❌ Erro ao acessar o arquivo para gravação.")

def exibir_notas():
    """Lê o arquivo CSV e exibe os dados em formato de tabela."""
    print("\n--- 📋 Lista de Notas Cadastradas ---")
    
    if not os.path.exists(ARQUIVO_CSV):
        print("⚠️ O arquivo ainda não existe. Adicione uma nota primeiro.")
        return

    try:
        with open(ARQUIVO_CSV, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            
            # Formatação simples de tabela no console
            print(f"{'NOME':<20} | {'NOTA':<5}")
            print("-" * 28)
            
            contagem = 0
            for linha in leitor:
                print(f"{linha['Nome']:<20} | {linha['Nota']:<5}")
                contagem += 1
            
            if contagem == 0:
                print("A lista está vazia.")
    except IOError:
        print("❌ Erro ao ler o arquivo CSV.")

def menu_principal():
    """Gerencia as opções do sistema."""
    while True:
        print("\n=== SISTEMA DE NOTAS (CSV) ===")
        print("1. Adicionar Nota")
        print("2. Exibir Notas Salvas")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            adicionar_nota()
        elif opcao == '2':
            exibir_notas()
        elif opcao == '3':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    menu_principal()