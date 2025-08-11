def formatar_nome(nome):
    return nome.strip().title()

def cadrastar_produto():
    nome = input("digite o nome do produtos: ")
    preco = float(input("digite o preço do produtos:  "))
    categoria = input("digite a categoria do produto: ")
    return  (formatar_nome(nome),preco,categoria)

def salvar_produto(produto):
    with open("produto.txt", "a",encoding="utf-8") as arquivos:
        linha =f"{produto}[0],{produto}[1],{produto}[2/n]"    