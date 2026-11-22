# Sistema de Controle de Compras

## Sobre o projeto

Exercicio desenvolvido no Modulo 2 do curso de
Desenvolvimento Web Back-End do SENAC.

O programa simula operacoes basicas de um carrinho de
compras de e-commerce, utilizando listas e pilhas em Python.

## Objetivos

- Adicionar produtos ao carrinho.
- Desfazer a ultima adicao.
- Refazer uma adicao desfeita.
- Finalizar a compra transferindo os produtos para outra lista.

## Conceitos aplicados

| Conceito | Aplicacao |
|---|---|
| Listas | Armazenamento dos produtos |
| Pilha (LIFO) | Controle das acoes desfeitas |
| append() | Adicionar elementos |
| pop() | Remover e retornar elementos |
| while | Repetir a transferencia de produtos |
| print() | Exibir resultados no terminal |

## Estruturas utilizadas

- `carrinho_compras`: produtos selecionados.
- `acoes_desfeitas`: itens removidos temporariamente.
- `itens_comprados`: produtos transferidos ao finalizar.

## Como executar

Requisito: Python 3 instalado.

No terminal, dentro da pasta deste exercicio:

```powershell
python modulo_2_exercicio.py
```

No Windows, tambem e possivel utilizar:

```powershell
py -3.12 modulo_2_exercicio.py
```

## Resultado esperado

```text
Carrinho de compras: ['Camiseta', 'Jeans', 'Tenis']
Carrinho apos desfazer: ['Camiseta', 'Jeans']
Acoes desfeitas: ['Tenis']
Carrinho apos refazer: ['Camiseta', 'Jeans', 'Tenis']
Itens comprados: ['Camiseta', 'Jeans', 'Tenis']
```

## Limitacoes

Este projeto e uma simulacao educacional executada
no terminal. Nao possui interface web, banco de dados,
pagamentos ou integracao com sistemas externos.

## Contexto academico

Atividade pratica do Modulo 2 do SENAC,
desenvolvida para exercitar estruturas de dados em Python.
