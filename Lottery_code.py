from random import sample

def sorteio_sem_repeticoes(n, i, f):
    return sorted(sample(range(i, f+1), n))

num = int(input("Deseja sortear quantos números? "))
ini = int(input("Digite o limite inicial do range: "))
fin = int(input("Digite o limite final do range: "))

print(sorteio_sem_repeticoes(num, ini, fin))
