#language:pt
Funcionalidade: Comprar produtos

  @test
  Cenário:Realizar a compra dos produtos
   Dado esteja na pagina inicial de login
   E insira os dados de login
  E filtre produtos do mais barato ao mais caro
  E adiciono os produtos no carrinho
  Quando inserir os dados pessoais
  Então realizo a compra com sucesso