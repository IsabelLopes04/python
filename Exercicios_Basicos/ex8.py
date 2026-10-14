# Acrescente exceções OverflowError em todos os métodos da classe, tratando erros com  números negativos
import formulas

class matematica:
    def euler(self, n):
        try:
            return formulas.Euler(n)
        except OverflowError:
            return "Erro: Número muito grande."
        except ValueError:
            return "Erro: Número negativo não é permitido."

    def fatorial(self, n):
        try:
            return formulas.fatorial(n)
        except OverflowError:
            return "Erro: Número muito grande."
        except ValueError:
            return "Erro: Número negativo não é permitido."

    def fibonacci(self, n):
        try:
            return formulas.fibonacci(n)
        except OverflowError:
            return "Erro: Número muito grande."
        except ValueError:
            return "Erro: Número negativo não é permitido."