class ordenha:

    def busca_binaria (self, lista, x):
        primeiro = 0
        ultimo = len(lista)-1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio-1
                else:
                    primeiro = meio +1
        return -1

vaca = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print (vaca)

b = ordenha()

b.busca_binaria(vaca,5)
print(b.busca_binaria(vaca,5))

b.busca_binaria(vaca,17)
print(b.busca_binaria(vaca,17))




