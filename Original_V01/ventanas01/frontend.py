from ventanas01.frontTela.frontend_aba1 import *
from ventanas01.frontTela.frontend_aba2 import *
from ventanas01.frontTela.frontend_aba4 import *
from ventanas01.frontTela.frontend_busca_cliente import *
from ventanas01.frontTela.frontend_busca_servico import *
from ventanas01.frontTela.frontend_tecnico import *
from ventanas01.frontTela.frontend_buscaOrc import *
from ventanas01.frontTela.frontend_Calendario import *
from ventanas01.frontTela.frontend_Containers import *
from ventanas01.frontTela.frontend_Logo import *
from ventanas01.frontTela.frontend_Menus import *
from ventanas01.frontTela.frontend_Molduras import *
from ventanas01.frontTela.frontend_PrimeiroFrame import *
from ventanas01.frontTela.frontend_QuartoFrame import *
from ventanas01.frontTela.frontend_QuintoFrame import *
from ventanas01.frontTela.frontend_SegundoFrame import *
from ventanas01.frontTela.frontend_TerceiroFrame import *

from funciones01.backUtiles.ValidaEntradas import *
from funciones01.backUtiles.imagensBase64 import *
from funciones01.backUtiles.multilang import *
from funciones01.backUtiles import relatorios
from funciones01.modulos import *

plataforma = platform.system()
if plataforma == "Linux":
    janela = tix.Tk()
else:
    janela = Tk()

class Tela(relatorios.PrintReal)

