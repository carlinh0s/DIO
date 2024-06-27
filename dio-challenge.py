from datetime import datetime

class Sistema_Bancario:
    
    def __init__(self, saldo=0.0):
        self.saldo = saldo
        self.historico_transacoes = []
        self.qtdsaque = 0

    def Deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self._adicionar_transacao(valor, "Depósito")
            print(f'Depósito no valor de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('O valor de depósito deve ser positivo!')

    def _adicionar_transacao(self, valor, tipo):
        transacao = {
            'data': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'valor': valor,
            'tipo': tipo
        }
        self.historico_transacoes.append(transacao)

    def Saque(self, valor):
        if valor > 0 and valor <= 500 and self.qtdsaque != 3:
            self.qtdsaque += 1
            if self.saldo >= valor:
                self.saldo -= valor
                self._adicionar_transacao(-valor, "Saque")
                print(f'Um saque no valor de R$ {valor:.2f} realizado com sucesso!')
            else:
                print('Não foi possível realizar o saque por falta de saldo!')
        else:
            print('(ERRO) O Sistema só permite realizar 3 saques diários, com limite máximo de R$ 500,00 por saque e apenas valores positivos.')

    def Extrato(self):
        print("Extrato de Transações:")
        for transacao in self.historico_transacoes:
            print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def Saldo(self):
        print(f'Atualmente o saldo em conta é de R$ {self.saldo:.2f}')

sistema = Sistema_Bancario()
opcao = ''

while opcao != 'sair':
    print('OPÇÕES DO SISTEMA: saque - deposito - extrato - saldo - sair.')
    opcao = input('Por favor, selecione uma das opções disponíveis: ').lower()

    if opcao == 'deposito':
        valor = float(input('Insira o valor de depósito: '))
        sistema.Deposito(valor)

    elif opcao == 'saque':
        valor = float(input('Insira o valor de saque: '))
        sistema.Saque(valor)

    elif opcao == 'extrato':
        sistema.Extrato()

    elif opcao == 'saldo':
        sistema.Saldo()

    elif opcao == 'sair':
        print('Programa finalizado, obrigado por utilizar!')
    else:
        print('Opção inválida! Por favor, selecione uma opção válida.')
