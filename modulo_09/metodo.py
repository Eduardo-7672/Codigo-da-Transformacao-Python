import re

# =================================================================
# CLASSE BASE: Carro
# =================================================================

class Carro:
    """
    Classe base que representa qualquer veículo a combustão.
    Utiliza __init__ para inicialização e __str__ para representação.
    """
    def __init__(self, marca, modelo, ano, dados_tecnicos, combustivel="Gasolina/Etanol"):
        """Método Mágico de Inicialização (Construtor)."""
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.combustivel = combustivel
        self.ficha_tecnica = dados_tecnicos if dados_tecnicos else {}
        
    def __str__(self):
        """
        Método Mágico de Representação (String).
        Define como o objeto deve ser exibido quando print() é chamado.
        """
        ficha_str = "\n".join([f"  - {k}: {v}" for k, v in self.ficha_tecnica.items()])
        
        return (
            f"\n--- 🚗 Relatório do Veículo ---"
            f"\n  Tipo: Carro a Combustão"
            f"\n  Marca e Modelo: {self.marca} {self.modelo}"
            f"\n  Ano: {self.ano}"
            f"\n  Combustível Principal: {self.combustivel}"
            f"\n  Especificações Técnicas:\n{ficha_str}"
        )

# =================================================================
# CLASSE HERDEIRA: CarroEletrico
# =================================================================

class CarroEletrico(Carro):
    """
    Representa um veículo elétrico, herdando de Carro.
    Adiciona o atributo exclusivo 'autonomia_bateria' e sobrescreve __str__.
    """
    def __init__(self, marca, modelo, ano, dados_tecnicos=None, autonomia_bateria_km=0):
        """Método Mágico de Inicialização (Construtor Estendido)."""
        # Chama o construtor da classe base, definindo o combustível como Eletricidade
        super().__init__(marca, modelo, ano, dados_tecnicos, combustivel="Eletricidade")
        
        # Adiciona o novo atributo específico
        self.autonomia_bateria = autonomia_bateria_km

    def __str__(self):
        """
        Sobrescreve o método __str__ para incluir a autonomia da bateria.
        """
        # Pega a representação básica do pai
        base_str = super().__str__()
        
        # Adiciona a informação exclusiva e corrige o tipo
        return base_str.replace("Carro a Combustão", "Carro ELÉTRICO") + \
               f"\n⚡ Autonomia da Bateria: {self.autonomia_bateria} km"

# =================================================================
# FUNÇÕES DE INTERAÇÃO (Input do Usuário)
# =================================================================

def coletar_input_carro_base():
    """Coleta dados para um Carro a Combustão (Classe Base)."""
    print("\n" + "="*40)
    print("CADASTRO DE CARRO A COMBUSTÃO")
    print("="*40)
    
    marca = input("   Marca do carro: ").strip().capitalize()
    modelo = input("   Modelo do carro: ").strip()
    ano = input("   Ano de fabricação: ").strip()
    combustivel = input("   Tipo de Combustível (ex: Flex/Diesel): ").strip()
    
    # Coleta ficha técnica (simplificada via input)
    ficha = {}
    ficha['Cilindradas'] = input("   Cilindradas do Motor (ex: 1.0L): ").strip()
    ficha['Potencia'] = input("   Potência (ex: 100cv): ").strip()

    return Carro(marca, modelo, ano, ficha, combustivel)


def coletar_input_carro_eletrico():
    """Coleta dados para um Carro Elétrico (Classe Herdeira)."""
    print("\n" + "="*40)
    print("CADASTRO DE CARRO ELÉTRICO")
    print("="*40)
    
    marca = input("   Marca do carro: ").strip().capitalize()
    modelo = input("   Modelo do carro: ").strip()
    ano = input("   Ano de fabricação: ").strip()
    
    # Coleta o atributo exclusivo
    while True:
        try:
            autonomia = int(input("   Autonomia da Bateria (em km, ex: 450): ").strip())
            break
        except ValueError:
            print("❌ Por favor, digite um número inteiro para a autonomia.")

    # Coleta ficha técnica (simplificada via input)
    ficha = {}
    ficha['Potencia'] = input("   Potência Total (ex: 200cv): ").strip()
    ficha['Tempo_Recarga'] = input("   Tempo de Recarga Rápida (ex: 30min): ").strip()

    return CarroEletrico(marca, modelo, ano, ficha, autonomia)

# =================================================================
# EXECUÇÃO E DEMONSTRAÇÃO
# =================================================================

def menu_cadastro():
    """Menu principal para demonstração dos métodos mágicos."""
    
    # Cadastro do Carro a Combustão
    carro_combustao = coletar_input_carro_base()
    
    # Cadastro do Carro Elétrico (usando Herança)
    carro_eletrico = coletar_input_carro_eletrico()
    
    print("\n" + "#" * 50)
    print("RELATÓRIO DE VEÍCULOS (USANDO MÉTODO __STR__)")
    print("#" * 50)
    
    # 1. Demonstração do __str__ da Classe Base
    # O comando print() automaticamente chama o método __str__()
    print("RELATÓRIO DE COMBUSTÃO:")
    print(carro_combustao) # Chama Carro.__str__()
    
    print("\n-------------------------------\n")
    
    # 2. Demonstração do __str__ da Classe Herdeira
    print("RELATÓRIO DE ELÉTRICO:")
    print(carro_eletrico) # Chama CarroEletrico.__str__()

if __name__ == "__main__":
    menu_cadastro()