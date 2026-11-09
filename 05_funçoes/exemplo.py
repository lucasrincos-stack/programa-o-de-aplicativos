#o que é uma função:
from multiprocessing.forkserver import read_signed


#uma função é um bloco de código criado para realizar
#uma determinada tarefa.
# la permite organizar e reutilizar código

#1. Criando uma funçao
#utilizar a palavra def para uma função

def saudacao():
    print("olá seja bem vindo!")

saudacao()

    #2. Criando uma função ccom parâmetro

    #parâmetros permitem enviar informçõess para a funçao

def saudacao(nome):
    print(f"Olá {nome}!")

saudacao("Ana")
saudacao("João")

#3. Mais de um parãmetro
def apresentar(nome , idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")

apresentar("Maria", 17)
apresentar("João", 20)

#4 função com calculo

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"resultado {resultado}")

somar(10 , 20)
somar(10, 90)

#5. retornando um valor
#return devolve um valor par ao local onde a função foi chamada

def somar2(numero1, numero2):
    return numero1 + numero2

print(somar(10 , 5))

#6. Função com condição
def verificariddade(idade):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"

    print(verificariddade(20))

#7. Parametro com valor padrao
def saudacao(nome="Aluno"):
    print(f"ola {nome}")

    saudacao("Joao")
    saudacao()

#8. Função utilizando lista
def calcularmMedia(nota):
    soma = 0
    for nota in nota:
        soma += nota

    return soma / len(nota)

nota = [8, 7, 9, 10]
media = calcularmMedia(nota)
print(f"media: {media}")


#9.
