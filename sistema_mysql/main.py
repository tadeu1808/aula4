from src.controller import produto_controller
from src.controller import Usuario_controller

def exibir_menu():
    print("\n Marea Toca tudo LTDA")
    print("\n ====== Menu ======")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produto")
    print("3 - Atualizar produto")
    print("4 - Deletar produto")
    print("5 - Buscar Produto unico")
    print("6 - Cadastrar usuario")
    print("7 - Listar usuarios")
    print("8 - Atualizar usuario" )
    print("0 - Sair")
    
def listar_produtos():
    print("\n ---Lista de Produtos ---")
    produtos = produto_controller.listar_produtos()
    if produtos:
        for produto in produtos:
         print(f"\nID: {produto['id']} \nNome: {produto['nome']} \nPreco: {produto['preco']}")
    else:
        print("não existem produtos cadastrados")
    
def cadastrar_produto():
    print("\n ---Cadastar produto--- ")
    nome = input("digite o nome: ")
    preco = input("Digite o preco: ")
    novo_id = produto_controller.cadastrar_produto(nome, preco)
    print(f"Produto cadastrado com sucesso ocm o novo ID {novo_id}.")

def opcao_atualizar():
    print("\n Atualizando o produto")
    produto_id = input("Digite o ID do Produto: ")
    nome = input("Digite o nome do Produto: ")
    preco = input("Digite o Preco: ")
    
    linhas = produto_controller.atualizar_produto(produto_id, nome, preco)
    if linhas > 0: # quantidade de linhas modificadas
        print("Produto atualizado com sucesso!")
    else:
        print("nenhm produto foi atualizado")
        
def cadastrar_usuario():
    print("\n ---Cadastar usuario--- ")
    email = input("Digite seu email: ")
    nome = input("digite o nome: ")
    idade = input("Digite a idade: ")
    novo_id = Usuario_controller.cadastrar_usuario(email, nome, idade)
    print(f"usuario cadastrado com sucesso com o novo ID {novo_id}.")
            
             
def usuario_atualizar():
    print("\n Atualizando o usuario")
    user_id = input("Digite o ID do usuario: ")
    nome = input("Digite o nome do usuario: ")
    idade = input("Digite o idade: ")
    email = input("Digite o email: ")
    
    linhas = Usuario_controller.atualizar_usuario(user_id, nome, idade, email)
    if linhas > 0: # quantidade de linhas modificadas
        print("Usuario atualizado com sucesso!")
    else:
        print("nenhm usuario foi atualizado")
        
def listar_usuarios():
    print("\n ---Lista de Usuarios ---")
    usuarios = Usuario_controller.listar_usuarios()
    if usuarios:
        for usuario in usuarios:
         print(f"\nID: {usuario['id']} \nNome: {usuario['nome']} \nidade: {usuario['idade']}\nEmail: {usuario['email']}")
    else:
        print("não existem usuarios cadastrados")
                
def main():
    #while true para repetir mesmo que a opção esteja errada
    while True:
        exibir_menu()     
        opc = input("Escolha Opção :")
        if opc =="1":
            cadastrar_produto()
        elif opc == "2":
            listar_produtos()
        elif opc == "3":
            opcao_atualizar()
        elif opc == "0":
            print("Saindo do Sistema")
            #sys.exit(0)
        elif opc == "6":
            cadastrar_usuario()
        elif opc == "7":
            listar_usuarios()
        elif opc == "8":
            usuario_atualizar()
        else:
            print("opção Invalida, tente novamente...")
            
if __name__ == '__main__':
    main()
    
 
    
   