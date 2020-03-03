# Nome do projeto: Multiplicação Russa
# Linguagem: Python
# Utilizações: Variáveis e Funções(Recursão)
# Autor: Rafael Lua - rafaellua13



# Descrição:

#-----------------------------------#
# Uma multiplicação de dois numeros (A e B) utilizada por antigos camponeses Russos. 
# Se consistia em sempre dividir por dois um dos valores (A/2), enquanto multiplica por dois o outro valor (B*2). 
# O processo deve se repetir até que não seja mais possivel dividir A (Quando encontrar o resultado 1)
# Em caso de numeros não inteiros, sempre arredondar para o mesmo numero sem as casas decimais. (6,5 = 6)
# O resultado final será a soma de todos os valores encontrados em B que tiveram um resultado impar em A.

# Exemplo: 
# 13 * 5 = ?

# 13 -- 5
# 6 -- 10
# 3 -- 20
# 1 -- 40

# 13 * 5 = 40 + 20 + 5 = 65
#-----------------------------------#

# Código:

def mult(a,  b,  soma):
  print(a,"--",b) # Mostrar resultados
  
  if a % 2 == 1:  # Somar os números ímpares
    soma += b

  if a == 1:      # Finalizar recursão quando o valor for 1
    return soma
  
  return mult(a // 2, b * 2, soma)  # Fazer operações por parâmetro na recursão


soma = 0
a = 13 # Multiplicar 13 * 5
b = 5
print(mult(a,b,soma))  




