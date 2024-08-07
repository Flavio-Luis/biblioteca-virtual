import books as b, variables_default as vb, menu, os, log # importando modulos

def add_book(new_book): # function para adicionar novos livros
    b.book_registration.append(new_book)

def loop_values(one_value): # function que faz um loop normal e imprime na tela
    for i in one_value:
        print(*i)
    
def loop_values_enumerate(one_value): # loop enumerados desde o número 1
    cont = 1
    for i in one_value:
        print(f"{cont})  {i}")
        cont += 1

def validation_int(message, variable_comparation): # function para validar inputs de usuários
    while True: # loop para aceitar digitos válidos
        try:
            response_user = int(input(message))
            while response_user not in variable_comparation: # verificação se o input está nas opções proporcionadas pelo sistema
                print(vb.message_error)
                response_user = int(input(f"\n{vb.message_new_value}"))
                continue
            break
        except ValueError:
            print(vb.message_error)
            continue
    return response_user # retorno da function

def validation_int_match_tree(message, variable_comparation): # function para validar inputs de usuários na case 3, de agregação na function user_choice
    while True: # loop para aceitar digitos válidos
        try:
            response_user = int(input(message))
            while response_user not in range(variable_comparation + 1): # verificação se o input está nas opções proporcionadas pelo sistema
                print(vb.message_error)
                response_user = int(input(f"\n{vb.message_new_value}"))
                continue
            break
        except ValueError:
            print(vb.message_error)
            continue
    return response_user # retorno da function

def clear_system(): # function para limpar o terminal
    os.system("cls")

def user_choice(response_user,name_user): # function que faz a lógica da lista
    match response_user:
        case 1: # caso a resposta seja == 1
            clear_system()
            print("\nVocê escolheu a opção 'Listar'")
            print("\nLivros:\n")
            loop_values_enumerate(b.book_registration)
            print("\nObserve o menu abaixo e escolha a opção desejada:\n")
        case 2: # caso a resposta seja == 2
            clear_system()
            print("Você escolheu a opção 'Empréstimo:'\n")
            loop_values_enumerate(b.book_registration)
            print()
            return_user = validation_int_match_tree(vb.message_validation_second, len(b.book_registration))
            return_screen = (f"{name_user}, você escolheu o livro de nome, '{b.book_registration[return_user - 1]}'")
            log.insert_log(return_screen)
            print(f"{return_screen}\n")
            print("     Menu\n")
        case 3: # caso a resposta seja == 3
            print("Você escolheu a opção 'Adicionar:'\n")
            return_add_book = input(vb.message_add_book)
            add_book(return_add_book)
            print(f"\nProntinho, o livro de nome '{return_add_book}' foi adicionado na lista!\n")
            print("     Menu\n")