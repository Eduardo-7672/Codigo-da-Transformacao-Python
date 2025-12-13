# =================================================================
# ATIVIDADE 2 & 3: Exibir Informações e Tratar Erros
# (Código Único e Corrigido)
# =================================================================

import requests
import json

def obter_dados_do_tempo():
    """
    CORREÇÃO: Esta função contém a requisição e o tratamento de erros
    (Atividade 1 e 3), tornando o código autônomo.
    """
    print("\n--- ☀️ Consulta de Previsão do Tempo ---")
    
    # 1. Coleta a chave da API do usuário
    api_key = input("1. Digite sua CHAVE API do OpenWeatherMap: ").strip()
    
    # 2. Coleta a localização do usuário
    cidade = input("2. Digite o nome da cidade: ").strip()
    pais = input("3. Digite o código do país (ex: BR, US): ").strip()

    if not api_key or not cidade:
        print("❌ Erro: A chave da API e o nome da cidade são obrigatórios.")
        return None

    # Construção da URL de requisição
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?"
        f"q={cidade},{pais}&"
        f"appid={api_key}&"
        f"units=metric&"
        f"lang=pt_br"
    )

    print(f"\n🌐 Tentando conectar à API para {cidade}/{pais}...")

    # Bloco try-except para tratamento de erros de conexão e HTTP (Atividade 3)
    try:
        resposta = requests.get(url)
        resposta.raise_for_status() # Levanta exceção para status 4xx/5xx
        return resposta.json()
        
    except requests.exceptions.HTTPError as err_http:
        # Trata erros de resposta da API (ex: 401, 404)
        print(f"❌ Erro HTTP (Código {resposta.status_code}): Falha na requisição.")
        print("Verifique se a CHAVE API está correta ou se a cidade/país foram digitados corretamente.")
    
    except requests.exceptions.ConnectionError:
        # Trata erros de conexão (ex: sem internet)
        print("❌ Erro de Conexão: Falha ao conectar à API. Verifique sua conexão com a internet.")
        
    except requests.exceptions.RequestException as e:
        # Trata outros erros gerais da biblioteca requests
        print(f"❌ Erro na Requisição: Um erro inesperado ocorreu: {e}")
        
    return None

def exibir_previsao_detalhada(dados):
    """
    Filtra e exibe informações específicas da API em formato organizado.
    (Cumpre o requisito 2).
    """
    if not dados:
        print("Não foi possível exibir a previsão, dados ausentes.")
        return

    try:
        # Extração dos dados relevantes
        temperatura_atual = dados['main']['temp']
        sensacao_termica = dados['main']['feels_like']
        condicao_climatica = dados['weather'][0]['description'].capitalize()
        umidade = dados['main']['humidity']
        velocidade_vento = dados['wind']['speed']
        cidade_nome = dados['name']

        print("\n" + "="*50)
        print(f"PREVISÃO DO TEMPO PARA: {cidade_nome.upper()}")
        print("="*50)
        
        print(f"🌡️ Temperatura Atual: {temperatura_atual:.1f}°C")
        print(f"🌡️ Sensação Térmica: {sensacao_termica:.1f}°C")
        print(f"☁️ Condição Climática: {condicao_climatica}")
        print(f"💧 Umidade do Ar: {umidade}%")
        print(f"💨 Velocidade do Vento: {velocidade_vento} m/s")
        print("="*50)

    except (KeyError, IndexError) as e:
        print(f"❌ Erro ao processar os dados: Estrutura da API inválida. Chave ausente: {e}")

def executar_previsao_completa():
    """Executa a requisição, trata erros e exibe os resultados."""
    dados = obter_dados_do_tempo()
    if dados:
        exibir_previsao_detalhada(dados)

if __name__ == "__main__":
    executar_previsao_completa()