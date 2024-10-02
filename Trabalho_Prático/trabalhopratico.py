import csv

# Função para carregar usuários do arquivo CSV
def carregar_usuarios(arquivo):
    usuarios = {}
    with open(arquivo, mode='r') as file:
        reader = csv.reader(file)
        for linha in reader:
            username, nome_completo, senha, tipo = linha
            usuarios[username] = (nome_completo, senha, tipo)
    return usuarios

# Função para salvar usuários no arquivo CSV
def salvar_usuarios(arquivo, usuarios):
    with open(arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        for username, dados in usuarios.items():
            writer.writerow([username] + list(dados))

# Função para carregar produtos do arquivo CSV
def carregar_produtos(arquivo):
    produtos = {}
    with open(arquivo, mode='r') as file:
        reader = csv.reader(file)
        for linha in reader:
            codigo, nome, descricao, preco, quantidade = linha
            produtos[codigo] = (nome, descricao, float(preco), int(quantidade))
    return produtos

# Função para salvar produtos no arquivo CSV
def salvar_produtos(arquivo, produtos):
    with open(arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        for codigo, dados in produtos.items():
            writer.writerow([codigo] + list(dados))

# Função para criar um novo usuário
def criar_usuario(usuarios):
    username = input("Digite o nome de usuário: ")
    if username in usuarios:
        print("Usuário já existe!")
        return
    
    nome_completo = input("Digite o nome completo: ")
    senha = input("Digite a senha: ")
    tipo = input("Digite o tipo de usuário (Admin, Funcionário, Cliente, Estagiário): ")
    
    usuarios[username] = (nome_completo, senha, tipo)
    print(f"Usuário {username} criado com sucesso!")

# Função para buscar e mostrar um usuário específico
def ler_usuario(usuarios):
    username = input("Digite o nome de usuário para buscar: ")
    if username in usuarios:
        print(f"Nome Completo: {usuarios[username][0]}")
        print(f"Tipo: {usuarios[username][2]}")
    else:
        print("Usuário não encontrado!")

# Função para atualizar um usuário existente
def atualizar_usuario(usuarios):
    username = input("Digite o nome de usuário a ser atualizado: ")
    if username in usuarios:
        nome_completo = input("Digite o novo nome completo: ")
        senha = input("Digite a nova senha: ")
        tipo = input("Digite o novo tipo de usuário (Admin, Funcionário, Cliente, Estagiário): ")
        
        usuarios[username] = (nome_completo, senha, tipo)
        print(f"Usuário {username} atualizado com sucesso!")
    else:
        print("Usuário não encontrado!")

# Função para deletar um usuário
def deletar_usuario(usuarios):
    username = input("Digite o nome de usuário a ser deletado: ")
    if username in usuarios:
        del usuarios[username]
        print(f"Usuário {username} deletado com sucesso!")
    else:
        print("Usuário não encontrado!")

# Função para criar um novo produto ou serviço
def criar_produto(produtos):
    codigo = input("Digite o código do produto/serviço: ")
    if codigo in produtos:
        print("Produto ou serviço já existe!")
        return
    
    nome = input("Digite o nome: ")
    descricao = input("Digite a descrição: ")
    preco = float(input("Digite o preço: "))
    quantidade = int(input("Digite a quantidade (0 para serviços): "))
    
    produtos[codigo] = (nome, descricao, preco, quantidade)
    print(f"Produto/Serviço {nome} criado com sucesso!")

# Função para buscar e mostrar um produto ou serviço específico
def ler_produto(produtos):
    codigo = input("Digite o código do produto/serviço para buscar: ")
    if codigo in produtos:
        print(f"Nome: {produtos[codigo][0]}")
        print(f"Descrição: {produtos[codigo][1]}")
        print(f"Preço: R$ {produtos[codigo][2]:.2f}")
        print(f"Quantidade: {produtos[codigo][3]}")
    else:
        print("Produto ou serviço não encontrado!")

# Função para atualizar um produto ou serviço existente
def atualizar_produto(produtos):
    codigo = input("Digite o código do produto/serviço a ser atualizado: ")
    if codigo in produtos:
        nome = input("Digite o novo nome: ")
        descricao = input("Digite a nova descrição: ")
        preco = float(input("Digite o novo preço: "))
        quantidade = int(input("Digite a nova quantidade (0 para serviços): "))
        
        produtos[codigo] = (nome, descricao, preco, quantidade)
        print(f"Produto/Serviço {nome} atualizado com sucesso!")
    else:
        print("Produto ou serviço não encontrado!")

# Função para deletar um produto ou serviço
def deletar_produto(produtos):
    codigo = input("Digite o código do produto/serviço a ser deletado: ")
    if codigo in produtos:
        del produtos[codigo]
        print(f"Produto/Serviço {codigo} deletado com sucesso!")
    else:
        print("Produto ou serviço não encontrado!")

# Função para imprimir os produtos ordenados por nome
def imprimir_produtos_por_nome(produtos):
    produtos_ordenados = sorted(produtos.items(), key=lambda x: x[1][0])
    for codigo, dados in produtos_ordenados:
        print(f"Codigo: {codigo} | Nome: {dados[0]} | Preço: R$ {dados[2]:.2f}")

# Função para imprimir os produtos ordenados por preço
def imprimir_produtos_por_preco(produtos):
    produtos_ordenados = sorted(produtos.items(), key=lambda x: x[1][2])
    for codigo, dados in produtos_ordenados:
        print(f"Codigo: {codigo} | Nome: {dados[0]} | Preço: R$ {dados[2]:.2f}")

# Função principal
def main():
    arquivo_usuarios = 'usuarios.csv'
    arquivo_produtos = 'produtos.csv'
    
    # Carregar dados dos arquivos
    usuarios = carregar_usuarios(arquivo_usuarios)
    produtos = carregar_produtos(arquivo_produtos)
    
    while True:
        print("\nSistema de Gerenciamento EcoSol")
        print("1. Gerenciar Usuários")
        print("2. Gerenciar Produtos/Serviços")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("\n1. Criar Usuário")
            print("2. Ler Usuário")
            print("3. Atualizar Usuário")
            print("4. Deletar Usuário")
            sub_opcao = input("Escolha uma opção: ")
            
            if sub_opcao == '1':
                criar_usuario(usuarios)
            elif sub_opcao == '2':
                ler_usuario(usuarios)
            elif sub_opcao == '3':
                atualizar_usuario(usuarios)
            elif sub_opcao == '4':
                deletar_usuario(usuarios)
            else:
                print("Opção inválida!")
            
            salvar_usuarios(arquivo_usuarios, usuarios)
        
        elif opcao == '2':
            print("\n1. Criar Produto/Serviço")
            print("2. Ler Produto/Serviço")
            print("3. Atualizar Produto/Serviço")
            print("4. Deletar Produto/Serviço")
            print("5. Imprimir Produtos/Serviços por Nome")
            print("6. Imprimir Produtos/Serviços por Preço")
            sub_opcao = input("Escolha uma opção: ")
            
            if sub_opcao == '1':
                criar_produto(produtos)
            elif sub_opcao == '2':
                ler_produto(produtos)
            elif sub_opcao == '3':
                atualizar_produto(produtos)
            elif sub_opcao == '4':
                deletar_produto(produtos)
            elif sub_opcao == '5':
                imprimir_produtos_por_nome(produtos)
            elif sub_opcao == '6':
                imprimir_produtos_por_preco(produtos)
            else:
                print("Opção inválida!")
            
            salvar_produtos(arquivo_produtos, produtos)
        
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
