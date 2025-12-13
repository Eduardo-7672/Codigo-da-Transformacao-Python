# =================================================================
# DESAFIO EXTRA: Buscar Dados de Filmes (TMDB API)
# =================================================================

import requests
import json

def buscar_filmes_tmdb():
    """
    Busca dados de filmes na API do TMDB (Título, Gênero, Sinopse).
    """
    print("\n--- 🎬 Busca de Filmes (TMDB) ---")
    
    # Coleta a chave da API e o termo de busca do usuário
    api_key = input("1. Digite sua CHAVE API do TMDB: ").strip()
    termo_busca = input("2. Digite o título do filme que deseja buscar: ").strip()

    if not api_key or not termo_busca:
        print("❌ Erro: A chave da API e o termo de busca são obrigatórios.")
        return

    # Endpoint de busca (Search Movie)
    url = (
        f"https://api.themoviedb.org/3/search/movie?"
        f"api_key={api_key}&"
        f"query={termo_busca}&"
        f"language=pt-BR"
    )

    print(f"\n🌐 Buscando filmes por: '{termo_busca}'...")

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        
        resultados = dados.get('results', [])
        
        if not resultados:
            print(f"⚠️ Nenhum filme encontrado com o título '{termo_busca}'.")
            return
            
        # Pega o primeiro resultado mais relevante
        filme_encontrado = resultados[0]
        
        # O TMDB fornece IDs de gênero, precisamos do endpoint de gêneros para mapear
        # Para simplificar a execução, vamos buscar os nomes dos gêneros separadamente:
        genero_ids = filme_encontrado.get('genre_ids', [])
        nomes_generos = obter_nomes_generos(api_key, genero_ids)
        
        # Exibição organizada
        print("\n" + "="*50)
        print("FICHA TÉCNICA DO FILME MAIS RELEVANTE")
        print("="*50)
        print(f"Título: {filme_encontrado.get('title', 'N/A')}")
        print(f"Gênero(s): {nomes_generos}")
        print("-" * 50)
        print("Sinopse:")
        print(filme_encontrado.get('overview', 'Sinopse não disponível em português.'))
        print("="*50)

    except requests.exceptions.HTTPError as err_http:
        print(f"❌ Erro HTTP (Código {resposta.status_code}): Verifique se a CHAVE API está correta ou se o termo de busca é válido.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na Conexão/Requisição: {e}")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

def obter_nomes_generos(api_key, genero_ids):
    """Auxiliar: Mapeia IDs de gênero para nomes usando a API do TMDB."""
    if not genero_ids:
        return "N/A"
        
    url_generos = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=pt-BR"
    
    try:
        resposta = requests.get(url_generos)
        resposta.raise_for_status()
        dados_generos = resposta.json()
        
        mapeamento = {g['id']: g['name'] for g in dados_generos.get('genres', [])}
        
        nomes = [mapeamento.get(id, "Desconhecido") for id in genero_ids]
        return ", ".join(nomes)
        
    except requests.exceptions.RequestException:
        return "Erro ao carregar gêneros"
        
if __name__ == "__main__":
    buscar_filmes_tmdb()