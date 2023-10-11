import sys

if sys.argv.__len__() != 8:
    print("A entrada deve conter 7 argumentos, sendo o primeiro a sequência e os demais as posições dos nucleotídeos onde começa e termina cada CDS do gene") 
    exit(1)

## Variáveis de entrada
sequencia = sys.argv[1]
n1 = sys.argv[2]
n2 = sys.argv[3]
n3 = sys.argv[4]
n4 = sys.argv[5]
n5 = sys.argv[6]
n6 = sys.argv[7]

sequencia = sequencia.upper()

## Testes de entrada de dados
if n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit() and n5.isdigit() and n6.isdigit():
    # Como as posições são contadas a partir de 1, é necessário subtrair 1 para que a posição seja correta na sequência
    n1 = int(n1)-1
    n2 = int(n2)-1
    n3 = int(n3)-1
    n4 = int(n4)-1
    n5 = int(n5)-1
    n6 = int(n6)-1
else:
    print("As posições devem ser números inteiros")
    exit(1)

# Criar uma lista com as posições para facilitar a ordenação
posicoes = [n1, n2, n3, n4, n5, n6]
# Se a lista não estiver ordenada, poderia acontecer erros na hora de pegar os CDSs
posicoes.sort()

# Testar se as posições estão dentro do tamanho da sequência
if not (0 < posicoes[0]):
    print("Erro: posições devem ser positivas")
    exit(1)
elif not (posicoes[5] < len(sequencia)):
    print("Erro: posições devem ser menores que o tamanho da sequência")
    exit(1)

cdss = []
ncs = []

# Pegar os CDSs, lembrando que a posição final é o último nucleotídeo do CDS (por isso o +1)
cdss.append(sequencia[posicoes[0]:(posicoes[1]+1)])
cdss.append(sequencia[posicoes[2]:posicoes[3]+1])
cdss.append(sequencia[posicoes[4]:posicoes[5]+1])

# Pegar as regiões não codificantes, lembrando que a posição inicial é onde termina o CDS anterior (portanto não deve ser incluído)
ncs.append(sequencia[:posicoes[0]])
ncs.append(sequencia[posicoes[1]+1:posicoes[2]]) ## ncs[1] é o intron 1
ncs.append(sequencia[posicoes[3]+1:posicoes[4]]) ## ncs[2] é o intron 2
ncs.append(sequencia[posicoes[5]+1:])

intron1 = ncs[1]
intron2 = ncs[2]

# verificar se o introns estão corretos, ou seja, se começam com GT e terminam com AG
if intron1[:2] != "GT" or intron1[-2:] != "AG":
    print("Erro: intron 1 não começa/termina com GT/AG")
    exit(1)
elif intron2[:2] != "GT" or intron2[-2:] != "AG":
    print("Erro: intron 2 não começa/termina com GT/AG")
    exit(1)

# Imprimir o cDNA resultante
print(f"cDNA resultante:\n{cdss[0]}{cdss[1]}{cdss[2]}\n")