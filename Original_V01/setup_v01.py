from funciones01.backUtiles import imagensBase64, multilang, validadores, uteis
from funciones01.backUtiles import colors, conector, license, editItem
from funciones01.backUtiles import backAba2Front, backSegundoFrame
from ventanas01 import frontend
from ventanas01.frontCads import cadAuto, cadClientes, cadEmpresa
from ventanas01.frontCads import cadEstoque, cadFornec, cadMarcaProd
from ventanas01.frontCads import cadPagamento, cadProd, cadServ
from ventanas01.frontCads import cadTec, atualizaMaodeObra, consFinan

class Application(uteis.Functions, imagensBase64.ImagensBase64,
                  conector.Conector, frontend.Tela, cadAuto.Automoveis,
                  cadClientes.Clientes, multilang.Lang, colors.Colors,
                  cadFornec.Fornecedores, cadTec.Tecnicos,
                  validadores.Validadores, cadProd.Produtos,
                  cadServ.Servicos, license.Data_company,
                  cadMarcaProd.MarcaProdutos, atualizaMaodeObra.MaodeObra,
                  cadEmpresa.Empresa, cadEstoque.Estoque,
                  consFinan.Financeiro, cadPagamento.PagamentoOrc,
                  editItem.EditItens, backAba2Front.Aba2,
                  backSegundoFrame.SegundoFrame):
    def __init__(self):
        self.montaTabelas(); self.cores()
        self.dados(); self.multiGlacx()
        self.images_base64(); self.tela()
        self.janela.mainloop()

Application()