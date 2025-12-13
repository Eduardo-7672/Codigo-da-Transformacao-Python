# =================================================================
# ATIVIDADE 2: Exceção Personalizada (SaldoInsuficienteError)
# =================================================================

class SaldoInsuficienteError(Exception):
    """Exceção personalizada levantada para saques sem saldo suficiente."""
    def __init__(self, saldo_atual, valor_saque):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        # Mensagem de erro detalhada
        super().__init__(f"Saque de R$ {valor_saque:.2f} falhou. Saldo insuficiente: R$ {saldo_atual:.2f}")

class ContaBancaria:
    """Simula uma conta bancária com método de saque seguro."""
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def sacar(self, valor):
        """Tenta realizar um saque e levanta SaldoInsuficienteError se necessário."""
        if valor <= 0:
            print("❌ Erro: O valor do saque deve ser positivo.")
            return

        if valor > self.saldo:
            # Levanta a exceção personalizada
            raise SaldoInsuficienteError(self.saldo, valor)
        
        # Realiza o saque
        self.saldo -= valor
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso. Novo saldo: R$ {self.saldo:.2f}")

def simular_saque_bancario():
    """Coleta inputs e demonstra a exceção personalizada."""
    print("\n--- 🏦 Simulação de Saque ---")
    
    # Coleta de Saldo Inicial
    while True:
        try:
            saldo_input = input("Defina o Saldo Inicial da conta (ex: 500.00): ").replace(',', '.')
            saldo_inicial = float(saldo_input)
            if saldo_inicial < 0:
                 print("⚠️ O saldo inicial não deve ser negativo.")
                 continue
            break
        except ValueError:
            print("❌ Entrada inválida. Digite um número para o saldo.")
            
    titular_conta = input("Defina o nome do Titular da conta: ").strip() or "Cliente Padrão"
    
    conta = ContaBancaria(titular_conta, saldo_inicial)
    print(f"Conta de {conta.titular} criada com R$ {conta.saldo:.2f}")

    # Coleta Valor do Saque
    while True:
        try:
            valor_saque = float(input("Digite o valor que deseja sacar: ").replace(',', '.'))
            if valor_saque <= 0:
                print("O valor do saque deve ser positivo.")
                continue
            break
        except ValueError:
            print("❌ Entrada inválida. Digite um número para o valor do saque.")

    # Bloco try-except para capturar a exceção personalizada
    try:
        conta.sacar(valor_saque)
    except SaldoInsuficienteError as e:
        # Captura e trata a exceção personalizada
        print(f"\n❗ Falha na Operação: {e}")
        print("A transação foi recusada devido ao saldo insuficiente.")
        
    print(f"\nStatus Final do Saldo: R$ {conta.saldo:.2f}")

if __name__ == "__main__":
    simular_saque_bancario()