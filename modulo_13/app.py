# =================================================================
# SISTEMA COMPLETO: POO, Exceções, SQLite e APIs (OpenWeatherMap)
# Nome do arquivo: sistema_completo.py
# =================================================================

import sqlite3
import requests
import re
import sys
import unittest
import os
from unittest import TestCase
from datetime import datetime

# =================================================================
# 1. FUNÇÕES AUXILIARES E CLASSES DE ERRO
# =================================================================

# --- Validação de Entrada (Atividade 3 - Bloco 2) ---
def validar_numero_positivo(prompt, tipo=float):
    """Garante que a entrada do usuário seja um número positivo."""
    while True:
        try:
            entrada = input(prompt).strip().replace(',', '.')
            if not entrada:
                raise ValueError("A entrada não pode ser vazia.")
                
            valor = tipo(entrada)
            
            if valor > 0:
                return valor
            else:
                print("❌ Erro de Validação: O valor deve ser um número positivo (> 0).")
                
        except ValueError:
            print("❌ Erro de Entrada: Entrada inválida. Tente novamente.")

# --- Exceções Personalizadas (Atividade 2 - Bloco 2) ---
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_saque):
        super().__init__(f"Saque de R$ {valor_saque:.2f} falhou. Saldo insuficiente: R$ {saldo_atual:.2f}")

class CredenciaisInvalidasError(Exception):
    pass

# --- Conexão SQLite ---
def conectar_db(nome_db):
    try:
        conn = sqlite3.connect(nome_db)
        return conn
    except sqlite3.Error as e:
        print(f"❌ Erro de conexão com o banco de dados: {e}")
        return None

# =================================================================
# 2. CLASSES POO (Herança e Métodos Mágicos) - Bloco 1
# =================================================================

class Carro:
    """Classe base que representa um veículo a combustão."""
    def __init__(self, marca, modelo, ano, dados_tecnicos, combustivel="Gasolina/Etanol"):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.combustivel = combustivel
        self.ficha_tecnica = dados_tecnicos
        
    def __str__(self):
        ficha_str = "\n".join([f"  - {k}: {v}" for k, v in self.ficha_tecnica.items()])
        return (
            f"\n--- 🚗 Relatório do Veículo ---"
            f"\n  Tipo: Carro a Combustão"
            f"\n  Marca e Modelo: {self.marca} {self.modelo} ({self.ano})"
            f"\n  Combustível Principal: {self.combustivel}"
            f"\n  Especificações Técnicas:\n{ficha_str}"
        )

class CarroEletrico(Carro):
    """Representa um veículo elétrico, herda de Carro e adiciona autonomia_bateria."""
    def __init__(self, marca, modelo, ano, dados_tecnicos=None, autonomia_bateria_km=0):
        super().__init__(marca, modelo, ano, dados_tecnicos, combustivel="Eletricidade")
        self.autonomia_bateria = autonomia_bateria_km

    def __str__(self):
        # Sobrescreve __str__ para incluir a autonomia da bateria
        base_str = super().__str__().replace("Carro a Combustão", "Carro ELÉTRICO")
        return base_str + f"\n⚡ Autonomia da Bateria: {self.autonomia_bateria} km"

# =================================================================
# 3. MÓDULOS DE ATIVIDADES
# =================================================================

# --- A. POO (Herança e __str__) ---
def modulo_poo():
    """Implementa a criação de Carro e CarroEletrico via input."""
    print("\n" + "="*50)
    print("MÓDULO 1: POO - HERANÇA E MÉTODOS MÁGICOS")
    print("="*50)

    # 1. Cadastro Carro Combustão (Classe Base)
    print("\n--- Cadastro de Carro a Combustão ---")
    marca_c = input("   Marca do carro: ").strip().capitalize()
    modelo_c = input("   Modelo do carro: ").strip()
    ano_c = input("   Ano de fabricação: ").strip()
    combustivel_c = input("   Tipo de Combustível (ex: Flex/Diesel): ").strip() or "Flex"
    ficha_c = {'Potencia': input("   Potência (ex: 100cv): ").strip(), 'Combustivel': combustivel_c}
    
    carro_combustao = Carro(marca_c, modelo_c, ano_c, ficha_c, combustivel_c)

    # 2. Cadastro Carro Elétrico (Classe Herdeira)
    print("\n--- Cadastro de Carro ELÉTRICO ---")
    marca_e = input("   Marca do carro: ").strip().capitalize()
    modelo_e = input("   Modelo do carro: ").strip()
    ano_e = input("   Ano de fabricação: ").strip()
    autonomia_e = validar_numero_positivo("   Autonomia da Bateria (em km): ", tipo=int)
    ficha_e = {'Potencia': input("   Potência Total (ex: 200cv): ").strip(), 'Tempo_Recarga': input("   Tempo de Recarga (ex: 6h): ").strip()}

    carro_eletrico = CarroEletrico(marca_e, modelo_e, ano_e, ficha_e, autonomia_e)

    # 3. Exibição usando __str__
    print("\n" + "#"*40)
    print("RELATÓRIO DE VEÍCULOS CADASTRADOS (Via __str__)")
    print("#"*40)
    print(carro_combustao)
    print(carro_eletrico)

# --- B. EXCEÇÕES (Calculadora, Bancário, Login) ---
def modulo_excecoes():
    """Implementa a calculadora com try-except, exceção bancária e login."""
    print("\n" + "="*50)
    print("MÓDULO 2: EXCEÇÕES E VALIDAÇÕES")
    print("="*50)

    # 1. Calculadora Segura (Atividade 1 - Bloco 2)
    print("\n--- 🧮 Calculadora de Divisão (Try-Except) ---")
    try:
        num1 = validar_numero_positivo("Digite o dividendo: ", tipo=float)
        num2 = validar_numero_positivo("Digite o divisor: ", tipo=float)
        
        resultado = num1 / num2
        print(f"✅ Resultado da Divisão: {num1} / {num2} = {resultado:.4f}")
        
    except ZeroDivisionError:
        print("❌ Erro: Não é possível dividir por zero (ZeroDivisionError capturado).")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

    # 2. Conta Bancária (Atividade 2 - Bloco 2)
    class ContaBancaria:
        def __init__(self, titular, saldo_inicial):
            self.titular = titular
            self.saldo = saldo_inicial
        def sacar(self, valor):
            if valor > self.saldo:
                raise SaldoInsuficienteError(self.saldo, valor)
            self.saldo -= valor
            print(f"✅ Saque de R$ {valor:.2f} realizado. Saldo: R$ {self.saldo:.2f}")

    print("\n--- 🏦 Simulação de Saque (Exceção Personalizada) ---")
    saldo_inicial = validar_numero_positivo("Defina o Saldo Inicial: ", tipo=float)
    titular_conta = input("Defina o Titular: ").strip() or "Padrão"
    conta = ContaBancaria(titular_conta, saldo_inicial)

    valor_saque = validar_numero_positivo("Digite o valor que deseja sacar: ", tipo=float)
    
    try:
        conta.sacar(valor_saque)
    except SaldoInsuficienteError as e:
        print(f"\n❗ Falha na Operação: {e}")

    # 3. Sistema de Login (Desafio Extra - Bloco 2)
    def sistema_login():
        print("\n--- 🔐 Sistema de Login ---")
        USUARIO_CORRETO = input("Defina o nome de usuário CORRETO: ").strip()
        SENHA_CORRETA = input("Defina a senha CORRETA: ").strip()
        MAX_TENTATIVAS = 3
        
        tentativas = 0
        while tentativas < MAX_TENTATIVAS:
            print(f"\nTentativa {tentativas + 1} de {MAX_TENTATIVAS}:")
            usuario_digitado = input("Usuário: ").strip()
            senha_digitada = input("Senha: ").strip()
            
            try:
                if usuario_digitado != USUARIO_CORRETO or senha_digitada != SENHA_CORRETA:
                    raise CredenciaisInvalidasError("Usuário ou senha incorretos.")
                
                print(f"\n🎉 Login bem-sucedido! Bem-vindo(a), {USUARIO_CORRETO}!")
                return
            except CredenciaisInvalidasError as e:
                tentativas += 1
                print(f"❌ Erro de Login: {e}. Tente novamente.")
            
        print(f"\n🛑 Número máximo de tentativas excedido. Acesso bloqueado.")
    
    sistema_login()

# --- C. SQLite (CRUD Clientes e Tarefas) ---
def modulo_sqlite():
    """Implementa o CRUD de clientes e o sistema de tarefas."""
    print("\n" + "="*50)
    print("MÓDULO 3: BANCO DE DADOS (SQLITE) - CRUD")
    print("="*50)

    nome_db = input("Digite o nome do arquivo do banco de dados (ex: dados.db): ").strip()
    if not nome_db.endswith('.db'):
        nome_db += '.db'
    
    conn = conectar_db(nome_db)
    if not conn: return

    # 1. Configurar Tabela Clientes (Atividade 1 - Bloco 4)
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        """)
        conn.commit()
        print(f"✅ Tabela 'Clientes' configurada em '{nome_db}'.")
    except sqlite3.Error as e:
        print(f"❌ Erro ao configurar tabelas: {e}")
        conn.close()
        return

    # 2. CRUD Clientes (Atividade 2 e 3 - Bloco 4)
    print("\n--- CRUD Clientes ---")
    
    # Inserir
    nome = input("Cliente 1: Nome para inserção: ").strip()
    email = input("Cliente 1: Email para inserção: ").strip()
    try:
        cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        print(f"✅ Cliente '{nome}' inserido.")
    except sqlite3.Error as e:
        print(f"❌ Erro ao inserir cliente: {e}")
    
    # Consultar
    condicao = input("Condição WHERE para filtro (ex: nome LIKE 'A%'): ").strip()
    if condicao:
        try:
            cursor.execute(f"SELECT id, nome, email FROM Clientes WHERE {condicao}")
            clientes = cursor.fetchall()
            print(f"\n✅ Consulta Filtrada (WHERE {condicao}): {clientes}")
        except sqlite3.OperationalError as e:
            print(f"❌ Erro SQL: {e}. Verifique a sintaxe.")
    
    # 3. Desafio Extra: Gerenciamento de Tarefas
    print("\n--- Gerenciamento de Tarefas ---")
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Pendente'
            );
        """)
        conn.commit()
        tarefa = input("Descrição da nova tarefa: ").strip()
        cursor.execute("INSERT INTO Tarefas (descricao) VALUES (?)", (tarefa,))
        conn.commit()
        
        cursor.execute("SELECT id, descricao, status FROM Tarefas")
        print(f"✅ Tarefas Atuais: {cursor.fetchall()}")
        
    except sqlite3.Error as e:
        print(f"❌ Erro nas tarefas: {e}")
    
    conn.close()

# --- D. API (OpenWeatherMap) ---
def modulo_api_open_weather():
    """Implementa a requisição, tratamento de erros e exibição de dados do OpenWeatherMap."""
    print("\n" + "="*50)
    print("MÓDULO 4: CONSUMO DE API (OpenWeatherMap)")
    print("="*50)
    
    api_key = input("1. Digite sua CHAVE API do OpenWeatherMap: ").strip()
    cidade = input("2. Digite o nome da cidade: ").strip()
    pais = input("3. Digite o código do país (ex: BR): ").strip()

    if not api_key or not cidade:
        print("❌ Erro: Chave e cidade são obrigatórias.")
        return

    url = (
        f"http://api.openweathermap.org/data/2.5/weather?"
        f"q={cidade},{pais}&"
        f"appid={api_key}&"
        f"units=metric&"
        f"lang=pt_br"
    )

    print(f"\n🌐 Tentando conectar à API para {cidade}/{pais}...")

    # Tratamento de Erros de Conexão e HTTP (Atividade 3 - Bloco 3)
    try:
        resposta = requests.get(url)
        resposta.raise_for_status() # Lança exceção para status 4xx/5xx

        dados = resposta.json()
        
        # Exibir Informações Específicas (Atividade 2 - Bloco 3)
        temperatura_atual = dados['main']['temp']
        condicao_climatica = dados['weather'][0]['description'].capitalize()
        nome_local = dados['name']

        print("\n" + "#"*40)
        print(f"PREVISÃO DO TEMPO PARA: {nome_local.upper()}")
        print("#"*40)
        print(f"🌡️ Temperatura Atual: {temperatura_atual:.1f}°C")
        print(f"☁️ Condição Climática: {condicao_climatica}")
        print("------------------------------------------")
        
    except requests.exceptions.HTTPError as err_http:
        print(f"❌ Erro HTTP (Código {resposta.status_code}): Verifique a CHAVE API ou a cidade/país.")
    except requests.exceptions.ConnectionError:
        print("❌ Erro de Conexão: Verifique sua internet.")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")


# =================================================================
# 4. MENU PRINCIPAL
# =================================================================

def menu_principal():
    """Menu principal para executar todos os módulos."""
    while True:
        print("\n\n" + "*"*60)
        print("SISTEMA DE DEMONSTRAÇÃO COMPLETO")
        print("*"*60)
        print("Selecione um Módulo:")
        print("1. POO (Herança, __str__) - Carros")
        print("2. Exceções e Validações (Calculadora, Bancário, Login)")
        print("3. Banco de Dados (SQLite - CRUD Clientes/Tarefas)")
        print("4. API Externa (OpenWeatherMap)")
        print("5. Testes Automatizados (unittest - Soma/Calculadora)")
        print("6. Executar Desafio Extra: Teste de API Flask (Requer Pytest/Separação de Arquivos)")
        print("7. Sair")
        print("-" * 60)
        
        opcao = input("Escolha uma opção (1-7): ").strip()

        if opcao == '1':
            modulo_poo()
        elif opcao == '2':
            modulo_excecoes()
        elif opcao == '3':
            modulo_sqlite()
        elif opcao == '4':
            modulo_api_open_weather()
        elif opcao == '5':
            # Executa os testes unitários (unittest)
            print("\n--- Executando Testes Unitários (Módulo unittest) ---")
            unittest.main(module='sistema_completo', exit=False)
        elif opcao == '6':
            print("\n" + "="*60)
            print("❗ INSTRUÇÕES PARA TESTE DE API FLASK (PYTEST) ❗")
            print("="*60)
            print("Este teste DEVE ser executado separadamente.")
            print("1. Crie os arquivos 'app.py' e 'test_api_flask.py' na mesma pasta (veja a próxima seção).")
            print("2. Responda aos inputs de configuração (USUÁRIO/ERRO/SAUDAÇÃO).")
            print("3. Execute no terminal: 'pytest'")
        elif opcao == '7':
            print("Sistema encerrado.")
            break
        else:
            print("❌ Opção inválida.")

# --- Execução dos Módulos unitest (Necessário para a Opção 5) ---
# Adiciona as classes de teste de volta no script principal para o unittest encontrá-las.

class Calculadora:
    def somar(self, a, b): return a + b
    def dividir(self, a, b): return a / b

class TestSomaSimples(TestCase):
    def test_soma_simples(self): self.assertEqual(Calculadora().somar(2, 2), 4)
    def test_divisao_por_zero(self): 
        with self.assertRaises(ZeroDivisionError): Calculadora().dividir(1, 0)

if __name__ == '__main__':
    menu_principal()