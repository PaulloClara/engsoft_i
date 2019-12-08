from src.controller.navbar import Navbar
from src.controller.home import Home
from src.controller.aluno import Aluno
from src.controller.grupo import Grupo
from src.controller.atividade import Atividade
from src.controller.sobre import Sobre


class Controller:

    def __init__(self):
        self.view = None
        self.model = None

        self.navbar = None
        self.home = None
        self.aluno = None
        self.grupo = None
        self.atividade = None
        self.sobre = None

    def segundo_init(self, model, view):
        self.view = view
        self.model = model

    def iniciar(self):
        self.navbar = Navbar(controller=self)
        self.home = Home(controller=self)
        self.aluno = Aluno(controller=self)
        self.atividade = Atividade(controller=self)
        self.grupo = Grupo(controller=self)
        self.sobre = Sobre(controller=self)

        self.model.iniciar()
        self.view.iniciar()

    def sortear(self, defs={}):
        erro, aluno, atividade = self.model.sortear(defs=defs)

        if erro:
            self.view.criar_janela_de_erro(erro=erro)
            return

        self.view.criar_janela_de_sorteio(
            aluno=aluno, atividade=atividade['titulo'])
