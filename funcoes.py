from datetime import datetime
import textwrap

def depositar(saldo, valor, extrato, /):
    data_hora_atual = datetime.now()
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f} às {data_hora_atual.strftime('%H:%M:%S %d/%m/%Y')}\n"
        print("\n=== Depósito realizado com sucesso! ===")
        print(f"=== Depósito feito às {data_hora_atual.strftime('%H:%M:%S %d/%m/%Y')} no valor R${valor:.2f} ===")
    else:
        print('\n>>> Operação falhou! O valor informado é inválido. <<<')
        print(f'Operação falhou às {data_hora_atual.strftime("%H:%M:%S %d/%m/%Y")}')


    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    data_hora_atual = datetime.now()

    if excedeu_saldo:
        print("\n>>> Operação falhou! Você não tem saldo suficiente. <<<")
        print(f'\n>>> Operação falhou às {data_hora_atual.strftime("%H:%M:%S %d/%m/%Y")} <<<')

    elif excedeu_limite:
        print("\n>>> Operação falhou! O valor do saque excede o limite. <<<")
        print(f'\n>>> Operação falhou às {data_hora_atual.strftime("%H:%M:%S %d/%m/%Y")} <<<')

    elif excedeu_saques:
        print("\n>>> Operação falhou! Número máximo de saques excedido. <<<")
        print(f'\n>>> Operação falhou às {data_hora_atual.strftime("%H:%M:%S %d/%m/%Y")} <<<')

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f} às {data_hora_atual.strftime('%H:%M:%S %d/%m/%Y')}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
        print(f"\n=== Saque realizado às {data_hora_atual.strftime('%H:%M:%S %d/%m/%Y')} ===")

    else:
        print("\n>>> Operação falhou! O valor informado é inválido. <<<")
        print(f'\n>>>Operação falhou às {data_hora_atual.strftime("%H:%M:%S %d/%m/%Y")}<<<')

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    data_hora_atual = datetime.now()
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print(f'\nConsulta realizada às {data_hora_atual.strftime("%H:%M:%S %d/%m/%Y")}')
    print("==========================================")


def criar_usuario(usuarios):
    data_hora_atual = datetime.now()
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n>>> Já existe usuário com esse CPF! <<<")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")
    print(f'=== Usuário {nome}, adicionado ao nosso DB às {data_hora_atual.strftime("%H:%M:%S %d/%m/%Y")} ===')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    data_hora_atual = datetime.now()
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f'\n=== Conta criada com sucesso às {data_hora_atual.strftime("%H:%M:%S %d/%m/%Y")}! ===')
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n>>> Usuário não encontrado, fluxo de criação de conta encerrado! <<<")


def listar_contas(contas):
    if not contas:
        print('>>> Atenção, Sem contas criadas <<<')
        return

    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
