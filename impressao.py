class Impressao:

    def visita_soma(self, soma):
        output = f"({soma.expressao_esquerda.aceita(self)}+{soma.expressao_direita.aceita(self)})"
        return output

    def visita_subtracao(self, subtracao):
        output = f"({subtracao.expressao_esquerda.aceita(self)}-{subtracao.expressao_direita.aceita(self)})"
        return output

    def visita_numero(self, numero):
        output = numero.avalia()
        return output
