from Funções.CapturarDados import selecionar_tabela, selecionar_todos_clientes
from Funções.EnviarEmail import envia_email
from Funções.CriarHtml import criar_html

def execucao_completa():
    """
    junção das funções em uma criando o fluxo da aplicação
    :return: None
    """
    aba = selecionar_tabela()
    linha_pedidos_por_cliente = selecionar_todos_clientes(aba)
    criar_html(linha_pedidos_por_cliente, aba)
