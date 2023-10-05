class GerenciadorContainers:
    def __init__(self):
        self.pilhas = [[] for _ in range(4)]  # 4 locais para empilhar containers

    def empilhar_container(self, codigo):
        if self._verificar_codigo_existente(codigo):
            print("Container já armazenado!")
        else:
            for pilha in self.pilhas:
                if len(pilha) < 3:
                    pilha.append(codigo)
                    print(f"Container {codigo} empilhado com sucesso na pilha {self.pilhas.index(pilha) + 1}.")
                    self.mostrar_estado_pilhas()
                    return
            print("Impossível empilhar: todas as pilhas estão cheias.")

    def desempilhar_container(self, codigo):
        for pilha in self.pilhas:
            if pilha and pilha[-1] == codigo:
                pilha.pop()
                print(f"Container {codigo} desempilhado com sucesso da pilha {self.pilhas.index(pilha) + 1}.")
                self.mostrar_estado_pilhas()
                return
        print("Código inválido ou impossível desempilhar: o container não está no topo da pilha!")

    def mostrar_estado_pilhas(self):
        print("\nEstado das pilhas:")
        for i, pilha in enumerate(self.pilhas):
            print(f"Pilha {i + 1}: {pilha}")

    def _verificar_codigo_existente(self, codigo):
        for pilha in self.pilhas:
            if codigo in pilha:
                return True
        return False

# Função para interação com o usuário
def main():
    gerenciador = GerenciadorContainers()

    while True:
        print("\nOpções:")
        print("1 - Empilhar container")
        print("2 - Desempilhar container")
        print("3 - Mostrar estado das pilhas")
        print("4 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            codigo = input("Digite o código do container a ser empilhado: ")
            gerenciador.empilhar_container(codigo)
        elif escolha == "2":
            codigo = input("Digite o código do container a ser desempilhado: ")
            gerenciador.desempilhar_container(codigo)
        elif escolha == "3":
            gerenciador.mostrar_estado_pilhas()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
