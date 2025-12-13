# =================================================================
# ATIVIDADE 3: Validar Entradas Inválidas (Divisão por Zero)
# =================================================================

import unittest
from unittest import TestCase

# --- 1. CLASSE A SER TESTADA (Reutilizada) ---
class Calculadora:
    """Uma classe simples para demonstrar operações matemáticas."""
    
    def somar(self, a, b):
        return a + b
    
    def dividir(self, a, b):
        # Esta função lançará um ZeroDivisionError se b for 0
        return a / b

# --- 2. CLASSE DE TESTE (Adicionando a validação de erro) ---
class TestValidacaoCalculadora(TestCase):
    """Testes focados em cenários de entradas inválidas."""

    def setUp(self):
        self.calc = Calculadora()

    def test_divisao_por_zero_lanca_excecao_com_inputs(self):
        """
        Valida que a divisão por zero LANCE a exceção ZeroDivisionError.
        """
        print("\n[Input Teste Divisão por Zero]")
        a = float(input("Digite o dividendo (qualquer número): ").replace(',', '.'))
        
        # O divisor é fixado como zero para forçar o erro
        b = 0
        
        # O Context Manager 'assertRaises' verifica se o erro esperado é levantado
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(a, b)
            
        print(f"✅ Teste Passou: A divisão de {a} por {b} lançou a exceção esperada (ZeroDivisionError).")

# --- 3. EXECUÇÃO DOS TESTES ---
if __name__ == '__main__':
    print("--- Executando Testes da Atividade 3 (Validação de Erros) ---")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)