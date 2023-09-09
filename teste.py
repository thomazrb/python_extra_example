from pessoa import Pessoa
import re

lista_de_pessoas = []
continuar = True

while continuar:
    while True:
        nome = input('Digite um nome: ')
        if re.match(r'^[a-zA-Zà-úÀ-Ú\s\.]+$', nome):
            break
        else:
            print('Nome inválido, digite apenas letras e espaço!')

    while True:
        nascimento = input('Digite a data de nascimento (dd/mm/aaaa): ')
        if re.match(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$', nascimento):
            # 01 02 03 04 ... 09 ou 10 11 12... 19... 20 21 22 ... 29 ou 30 31 / 01 02 .. 09 ou 10 11 12 / 0000 0001 0002 ... 9999 $
            break
        else:
            print('Data de nascimento inválida, digite a data no formato dd/mm/aaaa!')

    while True:
        cpf = input('Digite o CPF: ')
        if re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
            cpf = cpf.replace('.', '').replace('-', '')
            break
        elif re.match(r'^\d{11}$', cpf):
            break
        else:
            print('Cpf inválido!')

    pessoa = Pessoa(nome, nascimento, cpf)
    lista_de_pessoas.append(pessoa)

    while True:
        option = input('Deseja cadastrar mais pessoas? (S/N)')
        if re.match(r'^[SsNn]$', option):
            if option == 'N' or option == 'n':
                continuar = False
            break
        else:
            print('Opção invalida!')

print(f"Pessoas cadastradas: {len(lista_de_pessoas)}")
for pessoa in lista_de_pessoas:
    print(f'- {pessoa.nome} que nasceu no dia {pessoa.nascimento} e possui cpf {pessoa.cpf}.')