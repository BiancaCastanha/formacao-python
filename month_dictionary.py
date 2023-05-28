N = int(input())

while(N > 0):
  A, B = input("Digite os valores de A e B separados por espaço: ").split()
  if len(B) > len(A):
    print("nao encaixa")
  posicao_inicial = len(A) - len(B)
  if A[posicao_inicial:] == B:
    print("encaixa")
  else:
    print("nao encaixa")
  N -= 1