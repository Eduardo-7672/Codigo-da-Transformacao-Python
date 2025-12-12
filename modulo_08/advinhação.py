import random
import math

def iniciar_jogo():
    print("="*40)
    print("🎲 DESAFIO DE ADIVINHAÇÃO DINÂMICO")
    print("="*40)

    # 1. Coleta de informações do jogador (Nenhum dado pronto)
    nome = input("Digite seu nome, jogador(a): ").strip().capitalize()
    
    print(f"\nOlá, {nome}! Vamos configurar o seu desafio.")
    try:
        minimo = int(input("Digite o valor mínimo do intervalo (ex: 1): "))
        maximo = int(input("Digite o valor máximo do intervalo (ex: 100): "))
        
        if minimo >= maximo:
            print("❌ Erro: O valor máximo deve ser maior que o mínimo. Reiniciando...")
            return iniciar_jogo()

        # 2. Gerando o número secreto e cálculos matemáticos
        numero_secreto = random.randint(minimo, maximo)
        intervalo = maximo - minimo + 1
        
        # Cálculo matemático: O número máximo de tentativas ideais é log2 do intervalo
        tentativas_ideais = math.ceil(math.log2(intervalo))
        
        print(f"\n🔢 O número foi sorteado entre {minimo} e {maximo}!")
        print(f"💡 Dica matemática: Teoricamente, você consegue vencer em {tentativas_ideais} tentativas.")
        
        tentativas = 0
        acertou = False

        # 3. Loop do Jogo
        while not acertou:
            palpite = int(input(f"\n[Tentativa {tentativas + 1}] Qual o seu palpite? "))
            tentativas += 1

            if palpite < numero_secreto:
                print("🔼 Mais alto! Tente novamente.")
            elif palpite > numero_secreto:
                print("🔽 Mais baixo! Tente novamente.")
            else:
                acertou = True
                
        # 4. Cálculo da Pontuação usando Math
        # Fórmula: Pontuação = 100 / sqrt(tentativas)
        pontuacao = (100 / math.sqrt(tentativas)) * 10
        
        print("\n" + "⭐"*15)
        print(f"PARABÉNS, {nome.upper()}!")
        print(f"Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        print(f"Sua pontuação final foi: {pontuacao:.2f}")
        print("⭐"*15)

    except ValueError:
        print("❌ Erro: Por favor, insira apenas números inteiros válidos.")

if __name__ == "__main__":
    iniciar_jogo()