#atividade 1

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"{self.marca} {self.modelo} ligado.")

    def mostrar_info(self):
        estado = "ligado" if self.ligado else "desligado"
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Estado: {estado}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def abrir_porta_malas(self):
        print(f"Porta-malas do {self.marca} {self.modelo} aberto.")


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def empinar(self):
        if self.ligado:
            print(f"A {self.marca} {self.modelo} está empinando!")
        else:
            print(f"Não é possível empinar: a {self.marca} {self.modelo} está desligada.")


def main():
    carro = Carro("Toyota", "Corolla", 4)
    moto = Moto("Honda", "CB 500", 500)

    print("\n=== Carro ===")
    carro.mostrar_info()
    carro.ligar()
    carro.mostrar_info()
    carro.abrir_porta_malas()

    print("\n=== Moto ===")
    moto.mostrar_info()
    moto.empinar()
    moto.ligar()
    moto.mostrar_info()
    moto.empinar()


if __name__ == "__main__":
    main()

#atividade 2


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos.")


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def media(self):
        if not self.notas:
            return 0

        return sum(self.notas) / len(self.notas)


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def dar_aula(self):
        print(f"Prof. {self.nome} está dando aula de {self.disciplina}.")


def main():
    aluno = Aluno("Lucas", 17, "2026001")
    professor = Professor("Helena", 35, "Python")

    print("\n=== Aluno ===")
    aluno.apresentar()

    aluno.adicionar_nota(8.5)
    aluno.adicionar_nota(9.0)
    aluno.adicionar_nota(7.5)

    print(f"Média das notas: {aluno.media():.2f}")

    print("\n=== Professor ===")
    professor.apresentar()
    professor.dar_aula()


if __name__ == "__main__":
    main()
