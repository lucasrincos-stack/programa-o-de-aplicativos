
# 1. ENCAPSULAMENTO
# Proteger o salário para que só mude seguindo regras

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    def apresentar(self):
        print(f"Sou {self.nome} e ganho R$ {self.__salario}")

    # @property permite ler o salário como um atributo
    @property
    def salario(self):
        return self.__salario

    def dar_aumento(self, porcentagem):
        if porcentagem <= 0:
            print(f"Aumento inválido para {self.nome}")
        else:
            self.__salario = self.__salario * (1 + porcentagem / 100)
            print(f"{self.nome} recebeu {porcentagem}% de aumento")


Ana = Funcionario("Ana", 3000)

Ana.dar_aumento(10)
print(Ana.salario)
Ana.apresentar()

Ana.dar_aumento(-20)
Ana.apresentar()

# Tentativa de alterar o salário diretamente
try:
    Ana.salario = 10000
except AttributeError:
    print("Não é permitido alterar o salário diretamente.")

try:
    print(Ana.__salario)
except AttributeError:
    print("O atributo __salario não pode ser acessado diretamente.")


# 2. HERANÇA

class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    def mostrar_equipe(self):
        print(f"{self.nome} gerencia {self.equipe} funcionários")


class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso


print("\n======== HERANÇA ========")

bruno = Gerente("Bruno", 8000, 5)
caio = Estagiario("Caio", 1500, "Análise de Sistemas")

bruno.apresentar()
caio.apresentar()
bruno.mostrar_equipe()


# 3. POLIMORFISMO
# O mesmo método pode ter comportamentos diferentes

class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    def bonus(self):
        return self.salario * 0.20 + self.equipe * 100


class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso

    def bonus(self):
        return 200


print("\n======== POLIMORFISMO ========")

# Criando funcionários de diferentes classes
equipe = [
    Funcionario("Ana", 3000),
    Gerente("Bruno", 8000, 5),
    Estagiario("Caio", 1500, "Análise de Sistemas")
]

# Percorrendo a lista de funcionários
for funcionario in equipe:
    if hasattr(funcionario, "bonus"):
        print(f"{funcionario.nome}: R$ {funcionario.bonus():.2f}")
    else:
        print(f"{funcionario.nome}: Sem bônus definido")