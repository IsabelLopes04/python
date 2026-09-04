# Crie um script que exiba o nome do Brasil
# Qual o ano da ultima copa que o pais ganhou
# A rend per capita em dólares 2316,57
# V ou F para se o Brasil é um pais legal
# Use F-string

pais = "Brasil"
ano = 2002
renda_per_capita = 2316.57
pais_legal = True

print(f"O {pais} gannhou a ultima copa em {ano}, tem renda per capita de {renda_per_capita} e é um país{pais_legal} ")

pais = "isabel lopes"
print(pais.capitalize()) #Pega primeira letra e coloca em maiusculo

nome = "isabel" 
print(nome.upper()) #Coloca todas as letras em maiusculo

# capitalize(), upper(), lower()
#rjust(), ljust() - justifica a string a direita ou esquerda
# isalnum, isalpha(), isnumeric() - Testa se a string é alfanumerica, alfabetica ou numerica
# len() - Retorna o tamanho da string
#  strip(), rstrip(), lstrip() - remove espaços em branco

texto = "Olá, meu nome é Felipe"
sub = "meu"
print(texto.find(sub)) 

sub2 = "José"
print(texto.find(sub2)) #Resultado -1, pois não encontrou a substring
