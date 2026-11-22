# SENAC - Modulo 2
# Sistema de Controle de Compras

# 1. Adicionar itens ao carrinho
carrinho_compras = []

carrinho_compras.append("Camiseta")
carrinho_compras.append("Jeans")
carrinho_compras.append("Tenis")

print("Carrinho de compras:", carrinho_compras)

# 2. Desfazer adicao
acoes_desfeitas = []

item_removido = carrinho_compras.pop()
acoes_desfeitas.append(item_removido)

print("Carrinho apos desfazer:", carrinho_compras)
print("Acoes desfeitas:", acoes_desfeitas)

# 3. Refazer adicao
item_refeito = acoes_desfeitas.pop()
carrinho_compras.append(item_refeito)

print("Carrinho apos refazer:", carrinho_compras)

# 4. Finalizar compra
itens_comprados = []

while carrinho_compras:
    item = carrinho_compras.pop(0)
    itens_comprados.append(item)

print("Itens comprados:", itens_comprados)
