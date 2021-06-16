# peso = 0
# # p1 = float(input("Insira o peso: "))
# # p2 = float(input("Insira o peso: "))
# # p3 = float(input("Insira o peso: "))
# # p4 = float(input("Insira o peso: "))
# # p5 = float(input("Insira o peso: "))

# for c in range(1,5):
#   peso = float(input("Insira o peso: ")

peso = 0
maior = None
menor = None
for i in range(peso,5):
   x = float(input("Digite um peso: "))
   maior = maior if maior != None and maior >  x else x
   menor = menor if menor != None and menor < x else x

print ('O maior peso digitado foi {} e o menor foi {}'.format(maior,menor))