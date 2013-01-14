__author__ = 'hugohenley'

numero = input("Informe o numero que deseja converter para binario\n")

binary = bin(numero)
binary_list = list(binary)
del binary_list[0]
del binary_list[0]
print "".join(binary_list)