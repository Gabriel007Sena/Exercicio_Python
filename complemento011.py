class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, preco, quantidade):
        produto = {
            'nome': nome,
            'preco': preco,
            'qtd_prod': quantidade
        }
        self.produtos.append(produto)

    def consultar_valor_total_estoque(self):
        valor_total = 0
        for produto in self.produtos:
            valor_total += produto['qtd_prod'] * produto['preco']
        return valor_total


estoque = Estoque()


estoque.adicionar_produto('Produto 1', 10.0, 5)
estoque.adicionar_produto('Produto 2', 20.0, 3)
estoque.adicionar_produto('Produto 3', 15.0, 8)


total_estoque = estoque.consultar_valor_total_estoque()
print(f'Valor total do estoque: R${total_estoque:.2f}')
