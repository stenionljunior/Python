## Lista com nomes sem padrão, com espaço no inicio do nome. A ideia é ter uma saida com o padrão da primeira letra maiuscula e o restante minuscula.

pessoas = [' Ana', 'breno', 'FELIPE', 'StEnIo ', ' JUNior']

pessoas_formatadas = [pessoa.strip().capitalize() for pessoa in pessoas]

print(pessoas_formatadas)
