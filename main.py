import books as b, method as met, menu, customers as cust, log, variables_default as vb # importando modulos

print("Seja Bem vindo(a) a sua Biblioteca Virtual !")
print("Primeiro Vamos fazer seu Cadastro\n")

cliente_one_name = input("Digite seu Nome e Sobrenome:") # criando instâncias
cliente_one_age = input("Digite sua idade:")
cliente_one_library_card = input("Digite o número da sua carteirinha:")

client_one = cust.Client(cliente_one_name,cliente_one_age,cliente_one_library_card) # vinculando as instâncias na class

met.clear_system() # limpando terminal

print(f"\n{client_one.name}, observe o menu abaixo e escolha a opção desejada:\n") # imprimindo mensagem na tela

met.loop_values_enumerate(menu.options.values()) # exibindo o menu de options

response_user = met.validation_int(vb.message_validation_primary, menu.options) # atribuindo input de usuário a function de validação

while response_user != 4: # loop do programa
    met.user_choice(response_user,cliente_one_name) # atribuindo input ao function que faz toda lógica da lista
    met.loop_values_enumerate(menu.options.values()) # exibindo o muni de options
    response_user = met.validation_int(vb.message_validation_primary, menu.options) # atribuindo input de usuário a function de validação
    met.clear_system() # limpando terminal

print("\nAté Mais!\n") # terminando o programa
