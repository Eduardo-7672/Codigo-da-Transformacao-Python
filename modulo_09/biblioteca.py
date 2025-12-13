# =================================================================
# CLASSE 1: Livro
# =================================================================

class Livro:
    """
    Representa um livro individual na biblioteca.
    """
    def __init__(self, titulo, autor, isbn, ano_publicacao):
        # Usamos __init__ para inicializar os atributos do livro
        self.titulo = titulo.strip().title()
        self.autor = autor.strip().title()
        self.isbn = isbn.strip()
        self.ano_publicacao = ano_publicacao.strip()
        self.disponivel = True  # Status inicial: disponível
        
    def __str__(self):
        """Método mágico para exibir a representação do livro."""
        status = "✅ Disponível" if self.disponivel else "❌ Emprestado"
        return f"'{self.titulo}' por {self.autor} ({self.ano_publicacao}) | ISBN: {self.isbn} | Status: {status}"

# =================================================================
# CLASSE 2: Biblioteca
# =================================================================

class Biblioteca:
    """
    Gerencia a coleção de livros e as operações de empréstimo/devolução.
    """
    def __init__(self, nome):
        self.nome = nome
        self.colecao_livros = {}  # {ISBN: Livro_Objeto}
        self.emprestimos = {}     # {ISBN: nome_do_leitor}
        
    def adicionar_livro(self, livro):
        """Adiciona um objeto Livro à coleção."""
        if livro.isbn in self.colecao_livros:
            print(f"⚠️ Livro com ISBN {livro.isbn} já cadastrado.")
            return False
        
        self.colecao_livros[livro.isbn] = livro
        print(f"✅ Livro '{livro.titulo}' adicionado com sucesso.")
        return True

    def emprestar_livro(self, isbn, nome_leitor):
        """Registra o empréstimo de um livro."""
        livro = self.colecao_livros.get(isbn)
        
        if not livro:
            print(f"❌ Erro: Livro com ISBN {isbn} não encontrado na coleção.")
            return
            
        if not livro.disponivel:
            leitor_atual = self.emprestimos.get(isbn, "desconhecido")
            print(f"❌ Erro: '{livro.titulo}' já está emprestado para {leitor_atual}.")
            return
            
        # Atualiza o estado
        livro.disponivel = False
        self.emprestimos[isbn] = nome_leitor.strip().title()
        print(f"✅ Livro '{livro.titulo}' emprestado para {nome_leitor}.")

    def devolver_livro(self, isbn):
        """Registra a devolução de um livro."""
        livro = self.colecao_livros.get(isbn)
        
        if not livro:
            print(f"❌ Erro: Livro com ISBN {isbn} não encontrado.")
            return
            
        if livro.disponivel:
            print(f"⚠️ Aviso: '{livro.titulo}' não estava registrado como emprestado.")
            return
            
        # Atualiza o estado
        livro.disponivel = True
        self.emprestimos.pop(isbn, None)  # Remove o registro de empréstimo
        print(f"✅ Livro '{livro.titulo}' devolvido com sucesso.")

    def exibir_status(self):
        """Exibe todos os livros e empréstimos ativos."""
        print("\n" + "="*50)
        print(f"STATUS ATUAL DA BIBLIOTECA: {self.nome.upper()}")
        print("="*50)
        
        # 1. Lista de Livros (Usando __str__ do objeto Livro)
        print("\n📚 LIVROS CADASTRADOS:")
        if not self.colecao_livros:
            print("  Nenhum livro cadastrado.")
        
        for livro in self.colecao_livros.values():
            print(f"  > {livro}")

        # 2. Lista de Empréstimos Ativos
        print("\n👥 EMPRÉSTIMOS ATIVOS:")
        if not self.emprestimos:
            print("  Nenhum empréstimo ativo.")
        
        for isbn, leitor in self.emprestimos.items():
            livro = self.colecao_livros.get(isbn)
            titulo = livro.titulo if livro else "Título Desconhecido"
            print(f"  - Livro: '{titulo}' (ISBN: {isbn}) | Leitor: {leitor}")
        print("="*50)

# =================================================================
# FUNÇÕES DE INTERAÇÃO (Input do Usuário)
# =================================================================

def coletar_dados_livro():
    """Coleta dados para criar um novo objeto Livro."""
    print("\n--- 📖 Cadastro de Novo Livro ---")
    titulo = input("Título do livro: ").strip()
    autor = input("Autor do livro: ").strip()
    isbn = input("ISBN (Identificador Único): ").strip()
    ano = input("Ano de publicação: ").strip()
    
    if not titulo or not autor or not isbn:
        print("❌ Título, Autor e ISBN são obrigatórios.")
        return None
    
    return Livro(titulo, autor, isbn, ano)

def menu_principal(biblioteca):
    """Orquestra as ações do usuário."""
    
    while True:
        print("\n" + "#"*40)
        print(f"SISTEMA {biblioteca.nome.upper()}")
        print("#"*40)
        print("1. Cadastrar Novo Livro")
        print("2. Emprestar Livro")
        print("3. Devolver Livro")
        print("4. Exibir Status da Biblioteca")
        print("5. Sair")
        print("-" * 40)
        
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == '1':
            livro = coletar_dados_livro()
            if livro:
                biblioteca.adicionar_livro(livro)
                
        elif opcao == '2':
            isbn = input("Digite o ISBN do livro a emprestar: ").strip()
            leitor = input("Nome do leitor: ").strip()
            if isbn and leitor:
                biblioteca.emprestar_livro(isbn, leitor)
            else:
                print("❌ ISBN e Nome do leitor são necessários.")
                
        elif opcao == '3':
            isbn = input("Digite o ISBN do livro a devolver: ").strip()
            if isbn:
                biblioteca.devolver_livro(isbn)
            else:
                print("❌ O ISBN do livro é necessário.")
                
        elif opcao == '4':
            biblioteca.exibir_status()
            
        elif opcao == '5':
            print(f"\nEncerrando o sistema da {biblioteca.nome}. Até logo!")
            break
            
        else:
            print("❌ Opção inválida. Tente novamente.")

# =================================================================
# INÍCIO DO PROGRAMA
# =================================================================

if __name__ == "__main__":
    
    # Coletar nome da biblioteca do usuário (sem dados prontos)
    nome_biblioteca = input("Digite o nome da sua Biblioteca: ").strip().title()
    
    if not nome_biblioteca:
        nome_biblioteca = "Biblioteca Municipal" # Valor padrão se vazio
        
    # Criação do objeto Biblioteca
    minha_biblioteca = Biblioteca(nome_biblioteca)
    
    # Inicia o loop do menu
    menu_principal(minha_biblioteca)