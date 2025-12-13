import re

# =================================================================
# CLASSE BASE (PAI): Carro
# =================================================================

class Carro:
    """
    Classe base que representa qualquer veículo a combustão.
    """
    def __init__(self, marca, modelo, ano, dados_tecnicos=None, combustivel="Gasolina/Etanol"):
        # Atributos básicos (comuns a todos)
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.combustivel = combustivel # Atributo específico do Pai
        self.ficha_tecnica = dados_tecnicos if dados_tecnicos else {}
        
    def exibir_info(self):
        """Exibe as informações básicas e a ficha técnica (padrão para Carro a combustão)."""
        print(f"\n--- 🚗 Ficha Técnica: {self.marca} {self.modelo} ({self.ano}) ---")
        
        print(f"  Marca: {self.marca}")
        print(f"  Modelo: {self.modelo}")
        print(f"  Ano: {self.ano}")
        print(f"  Tipo de Combustível: {self.combustivel}")
        
        if self.ficha_tecnica:
            print("\n📊 ESPECIFICAÇÕES TÉCNICAS:")
            for chave, valor in self.ficha_tecnica.items():
                print(f"  {chave}: {valor}")
        
        print("-" * 50)
        
    def get_valor(self, chave):
        """Retorna um valor da ficha técnica para comparação."""
        return self.ficha_tecnica.get(chave, "N/A")

# =================================================================
# CLASSE HERDEIRA (FILHA): CarroEletrico
# =================================================================

class CarroEletrico(Carro):
    """
    Representa um veículo elétrico, herdando de Carro.
    Adiciona o atributo exclusivo 'autonomia_bateria'.
    """
    def __init__(self, marca, modelo, ano, dados_tecnicos=None, autonomia_bateria_km=0):
        # 1. Chama o construtor da classe base (Carro)
        # Sobrescreve o 'combustivel' para 'Eletricidade'
        super().__init__(marca, modelo, ano, dados_tecnicos, combustivel="Eletricidade")
        
        # 2. Adiciona o novo atributo específico
        self.autonomia_bateria = autonomia_bateria_km

    def exibir_info(self):
        """
        Sobrescreve o método exibir_info() para incluir a autonomia da bateria.
        """
        # Chama a exibição da classe base para aproveitar o código (até o tipo de combustível)
        super().exibir_info()
        
        # Adiciona a informação exclusiva
        print(f"⚡ AUTONOMIA ELÉTRICA: {self.autonomia_bateria} km (Exclusivo para elétricos)")
        print("-" * 50)


# =================================================================
# FUNÇÕES DE INTERAÇÃO (Input do Usuário)
# =================================================================

def coletar_input_carro_base():
    """Coleta dados para um Carro a Combustão (Classe Base)."""
    print("\n--- Cadastro de Carro a Combustão ---")
    
    # 1. Coleta dados básicos
    marca = input("Marca do carro: ").strip().capitalize()
    modelo = input("Modelo do carro: ").strip()
    ano = input("Ano de fabricação: ").strip()
    combustivel = input("Tipo de Combustível (ex: Flex/Diesel): ").strip()
    
    # 2. Coleta ficha técnica (simplificada via input)
    ficha = {}
    ficha['Cilindradas'] = input("Cilindradas do Motor (ex: 1.0L): ").strip()
    ficha['Potencia'] = input("Potência (ex: 100cv): ").strip()

    return Carro(marca, modelo, ano, ficha, combustivel)


def coletar_input_carro_eletrico():
    """Coleta dados para um Carro Elétrico (Classe Herdeira)."""
    print("\n--- Cadastro de Carro ELÉTRICO ---")
    
    # 1. Coleta dados básicos (iguais ao Pai)
    marca = input("Marca do carro: ").strip().capitalize()
    modelo = input("Modelo do carro: ").strip()
    ano = input("Ano de fabricação: ").strip()
    
    # 2. Coleta o atributo exclusivo
    while True:
        try:
            autonomia = int(input("Autonomia da Bateria (em km, ex: 450): ").strip())
            break
        except ValueError:
            print("❌ Por favor, digite um número inteiro para a autonomia.")

    # 3. Coleta ficha técnica (simplificada via input)
    ficha = {}
    ficha['Potencia'] = input("Potência Total (ex: 200cv): ").strip()
    ficha['Tempo_Recarga'] = input("Tempo de Recarga (ex: 6h): ").strip()

    return CarroEletrico(marca, modelo, ano, ficha, autonomia)

# =================================================================
# EXECUÇÃO E DEMONSTRAÇÃO
# =================================================================

def menu_cadastro():
    """Menu principal para demonstração."""
    
    print("=" * 60)
    print("SISTEMA DE CADASTRO DE VEÍCULOS (Com Herança)")
    print("=" * 60)
    
    # Cadastro do Carro a Combustão
    carro_combustao = coletar_input_carro_base()
    
    # Cadastro do Carro Elétrico (usando Herança)
    carro_eletrico = coletar_input_carro_eletrico()
    
    print("\n" + "#" * 30)
    print("RELATÓRIO DE VEÍCULOS CADASTRADOS")
    print("#" * 30)
    
    # Exibição do Carro a Combustão (Classe Base)
    carro_combustao.exibir_info()
    
    # Exibição do Carro Elétrico (Classe Herdeira, método sobrescrito)
    carro_eletrico.exibir_info()

    print("\n--- Demonstração de Herança ---")
    print(f"O carro elétrico '{carro_eletrico.modelo}' usa o método get_valor do Pai? {hasattr(carro_eletrico, 'get_valor')}")
    print(f"O carro elétrico tem o atributo (combustivel)? {carro_eletrico.combustivel}")
    print(f"O carro a combustão tem autonomia_bateria? {hasattr(carro_combustao, 'autonomia_bateria')}")

if __name__ == "__main__":
    menu_cadastro()