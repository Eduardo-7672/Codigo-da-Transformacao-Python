# =================================================================
# ATIVIDADE 2: Testes para uma Classe Calculadora (unittest)
# =================================================================

import unittest

# --- 1. CLASSE A SER TESTADA ---
class Calculadora:
    """Uma classe simples para demonstrar operações matemáticas."""
    
    def somar(self, a, b):
        return a + b
    
    def dividir(self, a, b):
        # Esta função lançará um ZeroDivisionError se b for 0
        return a / b

# --- 2. CLASSE DE TESTE ---
class TestCalculadora(unittest.TestCase):
    """Testes para a classe 'Calculadora'."""

    # Método executado antes de CADA método de teste
    def setUp(self):
        self.calc = Calculadora()
        print(f"\n[SETUP] Nova instância de Calculadora criada.")

    def test_somar_com_inputs(self):
        """Testa o método somar com números fornecidos pelo usuário."""
        print("\n[Input Teste Soma da Calculadora]")
        a = float(input("Digite o primeiro número para somar: ").replace(',', '.'))
        b = float(input("Digite o segundo número para somar: ").replace(',', '.'))
        
        valor_esperado = a + b
        
        self.assertEqual(self.calc.somar(a, b), valor_esperado)
        print(f"✅ Teste Soma OK: {a} + {b} = {self.calc.somar(a, b)}")

    def test_dividir_com_inputs(self):
        """Testa a divisão com números fornecidos pelo usuário."""
        print("\n[Input Teste Divisão da Calculadora]")
        # Garantindo que o divisor não seja zero para este teste
        while True:
            try:
                a = float(input("Digite o dividendo (ex: 10): ").replace(',', '.'))
                b = float(input("Digite o divisor (NÃO pode ser zero): ").replace(',', '.'))
                if b == 0:
                    print("❌ O divisor não pode ser zero neste teste.")
                    continue
                break
            except ValueError:
                print("❌ Entrada inválida. Digite apenas números.")
        
        valor_esperado = a / b
        
        # Usamos assertAlmostEqual para evitar erros de precisão em ponto flutuante
        self.assertAlmostEqual(self.calc.dividir(a, b), valor_esperado)
        print(f"✅ Teste Divisão OK: {a} / {b} = {self.calc.dividir(a, b)}")

# --- 3. EXECUÇÃO DOS TESTES ---
if __name__ == '__main__':
    print("--- Executando Testes da Atividade 2 (unittest) ---")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)