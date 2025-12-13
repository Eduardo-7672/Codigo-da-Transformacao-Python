import requests
from bs4 import BeautifulSoup
import json
import re # Adicionado para garantir limpeza de strings em números

# =================================================================
# CLASSE PRINCIPAL: Carro (POO)
# =================================================================

class Carro:
    """
    Representa um veículo com atributos básicos e dados técnicos
    obtidos da web.
    """
    def __init__(self, marca, modelo, ano=None, dados_tecnicos=None):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ficha_tecnica = dados_tecnicos if dados_tecnicos else {}
        
    def exibir_info(self):
        """Exibe as informações básicas e a ficha técnica completa."""
        print(f"\n--- 🚗 Ficha Técnica Detalhada: {self.marca} {self.modelo} ({self.ano}) ---")
        
        if not self.ficha_tecnica:
            print("⚠️ Dados técnicos não encontrados na web.")
            return

        print("\n⚙️ DADOS GERAIS:")
        print(f"  Marca: {self.marca}")
        print(f"  Modelo: {self.modelo}")
        print(f"  Ano: {self.ano}")
        
        print("\n📊 ESPECIFICAÇÕES TÉCNICAS (Obtidas da Web):")
        
        for chave, valor in self.ficha_tecnica.items():
            print(f"  {chave}: {valor}")
        
        print("-" * 50)
        
    def get_valor_numerico(self, chave):
        """
        Tenta extrair o primeiro número de uma string da ficha técnica.
        Ex: "9.2 segundos" -> 9.2
        """
        valor_str = str(self.ficha_tecnica.get(chave, "N/A")).replace(',', '.')
        
        # Encontra o primeiro padrão de número (inteiro ou decimal) na string
        match = re.search(r'\d+(\.\d+)?', valor_str)
        if match:
            try:
                return float(match.group(0))
            except ValueError:
                return None
        return None

# =================================================================
# FUNÇÕES DE BUSCA E SIMULAÇÃO DE WEB SCRAPING
# =================================================================

def buscar_ficha_tecnica_na_web(termo_busca):
    """
    Simula a busca por dados técnicos de um carro na internet.
    (Base de dados SIMULADA para demonstração executável).
    """
    print(f"\n🌐 Tentando buscar dados para: '{termo_busca}'...")
    
    base_simulada = {
        "corolla 2024": {
            "Potência (cv)": "139",
            "Torque (kgfm)": "17.7",
            "Câmbio": "CVT de 10 marchas",
            "Consumo Urbano (km/l)": "11.6",
            "0 a 100 km/h (s)": "9.2"
        },
        "onix plus 2024": {
            "Potência (cv)": "116",
            "Torque (kgfm)": "16.8",
            "Câmbio": "Automático de 6 marchas",
            "Consumo Urbano (km/l)": "10.1",
            "0 a 100 km/h (s)": "10.4"
        },
        "fusion 2018": {
            "Potência (cv)": "248",
            "Torque (kgfm)": "38",
            "Câmbio": "Automático de 6 marchas",
            "Consumo Urbano (km/l)": "8.6",
            "0 a 100 km/h (s)": "7.3"
        }
    }
    
    # Busca por palavra-chave na base simulada
    chave = termo_busca.lower().replace(" ", "")
    for k, v in base_simulada.items():
        if all(w in chave for w in k.split()):
             print("✅ Dados encontrados na base simulada.")
             return v
             
    print("❌ Dados técnicos detalhados não encontrados.")
    return {}

# =================================================================
# FUNÇÕES DE INTERAÇÃO E COMPARAÇÃO
# =================================================================

def coletar_dados_carro():
    """Coleta as informações básicas do carro e busca a ficha técnica."""
    print("\n--- Coleta de Dados ---")
    marca = input("   Marca do carro (ex: Toyota): ").strip()
    modelo = input("   Modelo (ex: Corolla): ").strip()
    ano = input("   Ano (ex: 2024): ").strip()
    
    termo_busca = f"{marca} {modelo} {ano}"
    
    dados_tecnicos = buscar_ficha_tecnica_na_web(termo_busca)
    
    return Carro(marca, modelo, ano, dados_tecnicos)

def realizar_comparacao(carros_cadastrados):
    """Permite ao usuário selecionar e comparar dois carros cadastrados."""
    print("\n" + "="*50)
    print("⚔️ MODO DE COMPARAÇÃO DE CARROS")
    print("="*50)
    
    if len(carros_cadastrados) < 2:
        print("❌ Você precisa de pelo menos 2 carros com fichas técnicas para comparar.")
        return

    # Exibe carros disponíveis
    print("\nCarros disponíveis (ID):")
    carros_validos = []
    
    for i, carro in enumerate(carros_cadastrados):
        if carro.ficha_tecnica:
            carros_validos.append(carro)
            print(f"  [ID {len(carros_validos)}] {carro.marca} {carro.modelo}")

    if len(carros_validos) < 2:
        print("❌ Não há carros suficientes com fichas técnicas completas para comparação.")
        return

    try:
        id1 = int(input("Digite o ID do PRIMEIRO carro (para comparação): "))
        id2 = int(input("Digite o ID do SEGUNDO carro (para comparação): "))
        
        # Ajusta ID para índice base 0
        idx1, idx2 = id1 - 1, id2 - 1
        
        if 0 <= idx1 < len(carros_validos) and 0 <= idx2 < len(carros_validos) and idx1 != idx2:
            carro1 = carros_validos[idx1]
            carro2 = carros_validos[idx2]
            
            # --- Inicia a Comparação ---
            print("\nParâmetros disponíveis (exemplos): Potência (cv), 0 a 100 km/h (s), Torque (kgfm)")
            chave_comparacao = input("Digite o parâmetro que deseja comparar: ").strip()
            
            valor1 = carro1.get_valor(chave_comparacao)
            valor2 = carro2.get_valor(chave_comparacao)
            
            print("\n--- Resultado da Comparação ---")
            print(f"Parâmetro: {chave_comparacao.upper()}")
            print(f"1. {carro1.modelo} ({carro1.ano}): {valor1}")
            print(f"2. {carro2.modelo} ({carro2.ano}): {valor2}")
            
            # Tentativa de comparação numérica inteligente (se aplicável)
            num1 = carro1.get_valor_numerico(chave_comparacao)
            num2 = carro2.get_valor_numerico(chave_comparacao)
            
            if num1 is not None and num2 is not None:
                if '0 a 100' in chave_comparacao.lower():
                    melhor = carro1.modelo if num1 < num2 else carro2.modelo
                    print(f"\n🏆 Conclusão: O {melhor} é o mais rápido (menor tempo de 0-100).")
                elif 'potência' in chave_comparacao.lower() or 'torque' in chave_comparacao.lower():
                    melhor = carro1.modelo if num1 > num2 else carro2.modelo
                    print(f"\n🏆 Conclusão: O {melhor} tem maior {chave_comparacao.lower()}.")
            
            print("-" * 35)

        else:
            print("❌ IDs inválidos, iguais ou fora do intervalo. Tente novamente.")
            
    except ValueError:
        print("❌ Por favor, digite um número inteiro para o ID.")

# =================================================================
# FUNÇÃO PRINCIPAL
# =================================================================

def menu_principal():
    """Função principal para orquestrar o programa."""
    carros_cadastrados = []
    
    while True:
        print("\n" + "="*60)
        print("SISTEMA DE FICHA TÉCNICA E COMPARAÇÃO DE VEÍCULOS (POO + WEB SIMULADA)")
        print("="*60)
        print("1. Cadastrar e Buscar Ficha Técnica de um Carro")
        print("2. Exibir Carros Cadastrados e Fichas")
        print("3. Comparar Dois Carros Cadastrados")
        print("4. Sair")
        print("-" * 60)
        
        opcao = input("Escolha a opção (1-4): ").strip()

        if opcao == '1':
            novo_carro = coletar_dados_carro()
            carros_cadastrados.append(novo_carro)

        elif opcao == '2':
            if not carros_cadastrados:
                print("Nenhum carro cadastrado ainda.")
                continue
            for i, carro in enumerate(carros_cadastrados):
                print(f"\n[Carro ID: {i+1}]")
                carro.exibir_info()
        
        elif opcao == '3':
            realizar_comparacao(carros_cadastrados)

        elif opcao == '4':
            print("Encerrando o sistema de veículos. Até logo!")
            break

        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    menu_principal()