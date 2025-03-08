from src.controller import produto_controller

def exibir_menu():
    print("\n Marea Toca tudo LTDA")
    print("\n ====== Menu ======")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produto")
    print("3 - Atualizar produto")
    print("4 - Deletar produto")
    print("5 - Buscar Produto unico")
    print("0 - Sair")
    
def listar_produtos():
    print("\n ---Lista de Produtos ---")
    produtos = produto_controller.listar_produtos()
    if produtos:
        for produto in produtos:
         print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preco: {produto['produto']}")
    else:
        print("não existem produtos cadastrados")
    
def cadastrar_produto():
    print("\n ---Cadastar produto ")
    nome = input("digite o nome:")
    preco = input("Digite o preco")
    novo_id = produto_controller.cadastrar_produto(nome, preco)
    print(f"Produto cadastrado com sucesso ocm o novo ID {novo_id}.")

def main():
    #while true para repetir mesmo que a opção esteja errada
    while True:
        exibir_menu()     
        opc = input("Escolha Opção :")
        if opc =="1":
            cadastrar_produto()
        elif opc == "2":
            listar_produtos()
        elif opc == "0":
            print("Saindo do Sistema")
            #sys.exit(0)
        else:
            print("opção Invalida, tente novamente...")
            
if __name__ == '__main__':
    main()
    
 
    
   