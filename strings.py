
curso = "pYtHoN"
print(curso.upper())
print(curso.lower())
print(curso.title())

curso = "   Python "
print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())

curso = "Python"
print(curso.center(10, '#'))
print(".".join(curso))


#INTERPOLAÇÃO
nome = "Bianca"
idade = 22
profissao = "Desenvolvedora Web"
linguagem = "HTML5 e CSS3"

print(f"Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} utilizando {linguagem}.")

#FATIAMENTO
nome = "Bianca Castanha Vieira de Mello"
print(nome[0])
print(nome[-1])
print(nome[:6])
print(nome[7:])
print(nome[7:15])
print(nome[7:15:2])
print(nome[:])
print(nome[::-1])

#STRING MÚLTIPLAS LINHAS
nome = "Bianca"

mensagem = f"""
    Olá meu nome é {nome},
Eu estou aprendendo Python
    Essa mensagem tem diferentes recuos"""

print(mensagem)