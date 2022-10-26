from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('cadastro/', views.Cadastro.as_view(), name='cadastro'),
    path('sair/', views.sair, name='sair'),
    path('perfil/', views.Perfil.as_view(), name='perfil'),
    path('perfil/editar', views.EditarPerfil.as_view(), name='editar_perfil'),
    path('perfil/atualizar_para_conta_comercial/', views.Planos.as_view(), name='planos'),
    path('perfil/atualizar_para_conta_comercial/plano=<str:plano>', views.AtualizarParaContaComercial.as_view(), name='atualizar'),
    path('perfil_loja/', views.PerfilLoja.as_view(), name='perfil_loja'),
    path('perfil_loja/editar/', views.EditarPerfilLoja.as_view(), name='editar_perfil_loja'),
    path('perfil_loja/colecoes/', views.MinhasColecoes.as_view(), name='minhas_colecoes'),
    path('perfil_loja/colecoes/adicionar/', views.add_colecao, name='add_colecao'),
    path('perfil_loja/colecoes/<int:pk>/', views.VerColecao.as_view(), name='colecao'),
    path('perfil_loja/colecoes/<int:colecaoPk>/<int:roupaPk>/', views.delete, name='deletar_roupa'),
    path('perfil_loja/meus_pedidos', views.MeusPedidos.as_view(), name='meus_pedidos'),    
    path('pesquisa/', views.TelaPesquisa.as_view(), name='tela_pesquisa'),
    path('pesquisar/', views.pesquisar, name='pesquisar'),
    path('lojas_cadastradas/', views.LojasCadastradas.as_view(), name='lojas_cadastradas'),
    path('em_breve/', views.EmBreve.as_view(), name='em_breve'),
    path('meus_pacotes/', views.MeusPacotes.as_view(), name='meus_pacotes'),
    path('lojas_cadastradas/<str:cidade>/', views.LojasCidade.as_view(), name='cidade'),
    path('lojas_cadastradas/<str:cidade>/<str:loja>/', views.LojaVer.as_view(), name='loja'),
    path('lojas_cadastradas/<str:cidade>/<str:loja>/<int:roupa>/', views.RoupaVer.as_view(), name='roupa'),
    path('pedido/<int:pk>', views.VerPedido.as_view(), name='ver_pedido'),
]
