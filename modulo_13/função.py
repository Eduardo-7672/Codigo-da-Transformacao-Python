# =================================================================
# ATIVIDADE 1: Teste de uma Função de Soma usando unittest
# =================================================================

import unittest

# --- 1. FUNÇÃO A SER TESTADA ---
def somar_numeros(a, b):
    """Retorna a soma de dois números."""
    return a + b

# --- 2. CLASSE DE TESTE ---
class TestSoma(unittest.TestCase):
    """Testes para a função 'somar_numeros'."""

    def test_soma_positivos(self):
        """Testa a soma de dois números positivos."""
        # Solicitando os números para o teste (para cumprir o requisito de input)
        print("\n[Input Teste 1: Soma de Positivos]")
        a = float(input("Digite o primeiro número para somar (ex: 5): ").replace(',', '.'))
        b = float(input("Digite o segundo número para somar (ex: 3): ").replace(',', '.'))
        
        # O valor esperado deve ser a soma dos inputs
        valor_esperado = a + b
        
        # unittest.TestCase.assertEqual(valor_esperado, valor_real)
        self.assertEqual(somar_numeros(a, b), valor_esperado)
        print(f"✅ Teste Passou: {a} + {b} = {somar_numeros(a, b)}")

    def test_soma_negativos(self):
        """Testa a soma envolvendo números negativos."""
        print("\n[Input Teste 2: Soma de Negativos]")
        a = float(input("Digite um número negativo para somar (ex: -10): ").replace(',', '.'))
        b = float(input("Digite outro número para somar (ex: 5): ").replace(',', '.'))
        
        valor_esperado = a + b
        
        self.assertEqual(somar_numeros(a, b), valor_esperado)
        print(f"✅ Teste Passou: {a} + {b} = {somar_numeros(a, b)}")

# --- 3. EXECUÇÃO DOS TESTES ---
if __name__ == '__main__':
    print("--- Executando Testes da Atividade 1 (unittest) ---")
    # Utilizamos exit=False para permitir que o programa continue após os testes
    unittest.main(argv=['first-arg-is-ignored'], exit=False)