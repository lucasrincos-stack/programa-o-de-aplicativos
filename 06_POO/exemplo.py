
# 1. ENCAPSULAMENTO
# Proteger o salário para que só mude seguindo regras

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    def apresentar(self):
        print(f"Sou {self.nome} e ganho R$ {self.__salario}")

    # @property permite ler o salário como se fosse um atributo
    @property
    def salario(self):
        return self.__salario

    def dar_aumento(self, porcentagem):
        if porcentagem <= 0:
            print(f"Aumento inválido para {self.nome}")
            return

        self.__salario = self.__salario * (1 + porcentagem / 100)
        print(f"{self.nome} recebeu {porcentagem}% de aumento")


ana = Funcionario("Ana", 3000)

# Tentativa de alteração direta
# ana.salario = 4000

print(ana.salario)
ana.apresentar()

ana.dar_aumento(10)
ana.apresentar()
