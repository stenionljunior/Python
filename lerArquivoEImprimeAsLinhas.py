# Ler um arquivo com o nome arquivo.txt e imprime todas as linhas contidas no arquivo
arquivo = open('arquivo.txt', 'r')
for linha in arquivo:
  print(linha)
arquivo.close()
