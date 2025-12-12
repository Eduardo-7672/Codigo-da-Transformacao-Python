from faker import Faker
from datetime import datetime
import re

# --- FUNÇÕES DE VALIDAÇÃO ---

def validar_cpf(cpf_bruto):
    """Valida um CPF usando o algoritmo de dígitos verificadores."""
    cpf = re.sub(r'\D', '', cpf_bruto)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calcular_dv(cpf_base, peso_inicial):
        soma = sum(int(cpf_base[i]) * peso for i, peso in enumerate(range(peso_inicial, 1, -1)))
        dv = 11 - (soma % 11)
        return '0' if dv >= 10 else str(dv)

    dv1 = calcular_dv(cpf[:9], 10)
    dv2 = calcular_dv(cpf[:10], 11)
    return dv1 == cpf[9] and dv2 == cpf[10]

def validar_ssn(ssn_bruto):
    """
    Valida um SSN americano baseado nas regras da SSA:
    1. Formato AAA-GG-SSSS (9 dígitos).
    2. Área (AAA) não pode ser 000, 666 ou entre 900-999.
    3. Grupo (GG) não pode ser 00.
    4. Serial (SSSS) não pode ser 0000.
    """
    ssn = re.sub(r'\D', '', ssn_bruto)
    if len(ssn) != 9:
        return False
    
    area = int(ssn[0:3])
    grupo = int(ssn[3:5])
    serial = int(ssn[5:9])

    if area == 0 or area == 666 or 900 <= area <= 999:
        return False
    if grupo == 0:
        return False
    if serial == 0:
        return False
    
    return True

# --- PROGRAMA PRINCIPAL ---

def gerador_de_perfis_internacional():
    print("="*65)
    print("🌍 GERADOR DE PERFIS COM VALIDAÇÃO INTERNACIONAL (CPF/SSN)")
    print("="*65)

    try:
        quantidade = int(input("Quantos perfis deseja gerar? "))
        print("\nEscolha a localidade:")
        print("1 - Brasil (pt_BR) [Valida CPF]")
        print("2 - EUA (en_US) [Valida SSN]")
        
        opcao = input("Opção (1 ou 2): ").strip()
        idioma = 'pt_BR' if opcao == '1' else 'en_US'
        fake = Faker(idioma)
        
        ano_atual = datetime.now().year
        perfis = []

        print(f"\n⏳ Processando {quantidade} registros...")
        print("-" * 65)

        for _ in range(quantidade):
            data_nasc = fake.date_of_birth(minimum_age=18, maximum_age=85)
            doc = fake.cpf() if idioma == 'pt_BR' else fake.ssn()
            
            # Validação dinâmica conforme o idioma
            if idioma == 'pt_BR':
                valido = validar_cpf(doc)
                tipo_doc = "CPF"
            else:
                valido = validar_ssn(doc)
                tipo_doc = "SSN"

            perfil = {
                "nome": fake.name(),
                "documento": doc,
                "tipo_doc": tipo_doc,
                "status": "✅ VÁLIDO" if valido else "❌ INVÁLIDO",
                "nascimento": data_nasc.strftime("%d/%m/%Y"),
                "idade": ano_atual - data_nasc.year,
                "cidade": fake.city(),
                "empresa": fake.company(),
                "telefone": fake.phone_number(),
                "email": fake.email()
            }
            perfis.append(perfil)

        # Exibição dos dados
        for i, p in enumerate(perfis, 1):
            print(f"🆔 PERFIL #{i} | {p['status']}")
            print(f"   👤 Nome: {p['nome']} ({p['idade']} anos)")
            print(f"   📅 Nasc: {p['nascimento']} | 📍 Cidade: {p['cidade']}")
            print(f"   🏢 Empresa: {p['empresa']}")
            print(f"   💳 {p['tipo_doc']}: {p['documento']}")
            print(f"   📞 Tel: {p['telefone']} | 📧 {p['email']}")
            print("-" * 50)

        print(f"✅ Concluído em: {datetime.now().strftime('%H:%M:%S')}")

    except ValueError:
        print("❌ Erro: Digite um número válido.")

if __name__ == "__main__":
    gerador_de_perfis_internacional()