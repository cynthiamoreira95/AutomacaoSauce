from behave import given, when, then
from pages.organiza import Organiza
from pages.carrinho import Carrinho
from pages.login_page import LoginPage
from pages.produtos import Produtos
from pages.utils import Utils

utils = Utils()
login_page = LoginPage()
organiza = Organiza()
produtos = Produtos()
carrinho = Carrinho()

@given(u"esteja na pagina inicial de login")
def step_impl(context):
    """

    :param context:
    """

utils.navegar('https://www.saucedemo.com/')

@given(u"insira os dados de login")
def step_impl(context):
    """

    :param context:
    """
login_page.preenche_usuario('standard_user')
login_page.preenche_password('secret_sauce')
login_page.clicar_btn_login()

@given(u'filtre produtos do mais barato ao mais caro')
def step_impl(context: object) -> object:

    """

    :param context:
    """

organiza.filtro()

@given(u'adiciono os produtos no carrinho')
def step_impl(context: object):
    """
    :param context:
    """
produtos.adiciona_produto1()
produtos.adiciona_produto2()
@when(u'inserir os dados pessoais')
def step_impl(context: object) -> object:
    """

    :param context:
    """
carrinho.visualiza()
utils.checkout()
carrinho.dados_pessoais_nome('Cynthia')
carrinho.dados_cep('06506045')
utils.continuar()
utils.scroll_down()
utils.finish()
@then(u'realizo a compra com sucesso')
def step_impl(context: object) -> object:
    """

    :param context:
    """
