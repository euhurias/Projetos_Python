AGENDA = {}


AGENDA['Hurias']={'telefone': '991890782',
                  'email':'hurias52@gmail.com',
                  'endereco':'cas cha 142',}

AGENDA['Enmilly']={'telefone': '994774041',
                  'email':'enmilly2005@gmail.com',
                  'endereco':'miguel alves',}

def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)


def buscar_contato(contato):
    print("Nome:", contato)
    print("Telefone:", AGENDA[contato]["telefone"])
    print("E-mail:", AGENDA[contato]["email"])
    print("Endereço:", AGENDA[contato]["endereco"])
    print('------------------------------------------------')


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print("Contato {} adicionado/editado com sucesso".format(contato))

def excluir_contato(contato):
    AGENDA.pop(contato)
    print()
    print("Contato {} excluido com sucesso".format(contato))
    print()


def imprimir_menu():
    print('------------------------------------------------')
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('0 - Sair')
    print('------------------------------------------------')

while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3' or opcao == '4':
        contato = input('Digite o nome do contato: ')
        telefone = input('Digite o nome do telefone: ')
        email = input('Digite o nome do email: ')
        endereco = input('Digite o nome do endereço: ')
        incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '0':
        print(">>>>>  Fechando o programa  <<<<<")
        break
    else:
        print('>>>>>  Opção inválida  <<<<<')