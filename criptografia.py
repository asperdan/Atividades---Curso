import base64
# chave = int(7352)
# texto = ("I am your father.")
# texto = secrets.randbits(32)
# print(texto)
# texto = secrets.randbits(32)
class Criptografia:

    def __init__(self, mensagemOriginal="", mensagemCriptografada=""):
        self.mensagemOriginal = mensagemOriginal
        self.mensagemCriptografada = mensagemCriptografada

    def criptografarMensagem(self):
        mensagem_bytes = self.mensagemOriginal.encode("ascii")
        base64_bytes = base64.b64encode(mensagem_bytes)
        base64_mensagem = base64_bytes.decode("ascii")
        self.mensagemCriptografada = base64_mensagem
        print(f"Frase decriptografada: {base64_mensagem}")

    def descriptografarMensagem(self):
        Dbase64_bytes = self.mensagemCriptografada.encode("ascii")
        msg_decrito_bytes = base64.b64decode(Dbase64_bytes)
        self.mensagemdescriptografada = msg_decrito_bytes.decode("ascii")
        print(f"Mensagem descriptografada: {self.mensagemdescriptografada}")

if __name__ == '__main__':
    primeiraMensagem = Criptografia("Criptografado aqui")
    primeiraMensagem.criptografarMensagem()
    primeiraMensagem.descriptografarMensagem()