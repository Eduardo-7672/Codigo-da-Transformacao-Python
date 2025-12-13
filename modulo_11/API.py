# =================================================================
# ATIVIDADE: Consumir API do OpenWeatherMap com Inputs e Try-Except
# =================================================================

import requests

def obter_previsao_do_tempo():
    """
    Coleta a chave API, cidade e país do usuário, realiza a requisição
    à API do OpenWeatherMap e exibe a temperatura e condições.
    """
    print("\n--- ☀️ Consulta de Previsão do Tempo ---")
    
    # 1. Coleta a chave da API do usuário (sem dados prontos)
    api_key = input("1. Digite sua CHAVE API do OpenWeatherMap: ").strip()
    
    # 2. Coleta a localização do usuário (sem dados prontos)
    cidade = input("2. Digite o nome da cidade: ").strip()
    pais = input("3. Digite o código do país (ex: BR, US): ").strip()

    if not api_key or not cidade:
        print("❌ Erro: A chave da API e o nome da cidade são obrigatórios.")
        return

    # Construção da URL de requisição
    # Usando unidades métricas (Celsius) e linguagem Português (pt_br)
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?"
        f"q={cidade},{pais}&"
        f"appid={api_key}&"
        f"units=metric&"
        f"lang=pt_br"
    )

    print(f"\n🌐 Tentando conectar à API para {cidade}/{pais}...")

    # Bloco try-except para tratamento de erros de conexão e HTTP
    try:
        # 1. Faz a requisição HTTP usando a biblioteca requests
        resposta = requests.get(url)
        
        # 2. Levanta uma exceção para códigos de status HTTP 4XX/5XX
        resposta.raise_for_status()

        # Converte a resposta JSON para um dicionário Python
        dados = resposta.json()
        
        # 3. Extrai e exibe as informações solicitadas (Temperatura e Condição)
        temperatura_atual = dados['main']['temp']
        condicao_climatica = dados['weather'][0]['description'].capitalize()
        nome_local = dados['name']

        print("\n" + "="*50)
        print(f"PREVISÃO DO TEMPO PARA: {nome_local.upper()}")
        print("="*50)
        print(f"🌡️ Temperatura Atual: {temperatura_atual:.1f}°C")
        print(f"☁️ Condição Climática: {condicao_climatica}")
        print("="*50)
        
    except requests.exceptions.HTTPError as err_http:
        # Trata erros de resposta da API (ex: 401 Chave Inválida, 404 Cidade Não Encontrada)
        print(f"❌ Erro HTTP (Código {resposta.status_code}): Falha na requisição.")
        print("Verifique se a CHAVE API está correta ou se a cidade/país foram digitados corretamente.")
    
    except requests.exceptions.ConnectionError:
        # Trata erros de conexão (ex: sem internet)
        print("❌ Erro de Conexão: Falha ao conectar à API. Verifique sua conexão com a internet.")
        
    except requests.exceptions.RequestException as e:
        # Trata outros erros gerais da biblioteca requests
        print(f"❌ Erro na Requisição: Um erro inesperado ocorreu durante a conexão: {e}")
        
    except (KeyError, IndexError) as e:
        # Trata erros na estrutura dos dados recebidos
        print(f"❌ Erro ao processar os dados recebidos: Estrutura da API inválida. Chave ausente: {e}")

if __name__ == "__main__":
    obter_previsao_do_tempo()