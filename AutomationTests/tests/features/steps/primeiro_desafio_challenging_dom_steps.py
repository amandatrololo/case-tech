from behave import *
from AutomationTests.tests.features.pages.primeiro_desafio_challenging_dom import DesafioDom

@given("eu acesso a webpage do Challenge")
def step_acesso_a_webpage_do_challenge(context):
        context.page = DesafioDom(context.driver)
        context.page.open()

@when("clico em todos os botoes de acao")
def step_clico_todos_botoes_acao(context):
        context.page.clica_todos_action_buttons()

@then("todos os botoes da tela devem ser clicados com sucesso")
def step_assegura_clique_todos_action_buttons(context):
        action_buttons = context.page.get_botoes_acao()
        contagem_esperada_botao_acao = 3
        if len(action_buttons) != contagem_esperada_botao_acao:
            raise AssertionError(
                f"Erro: Esperado {contagem_esperada_botao_acao} botões de ação, mas encontrado {len(action_buttons)}")

        botoes_clicados = context.page.clica_todos_action_buttons()
        contagem_esperada_de_cliques = 3
        if len(botoes_clicados) != contagem_esperada_de_cliques:
            raise AssertionError(
                f"Erro: Esperado {contagem_esperada_de_cliques} cliques (1 por botão), mas encontrado {len(botoes_clicados)}")
        print(
            f"a)Sua automação efetuou {len(botoes_clicados)} cliques nos {len(action_buttons)} botões de ação com sucesso.")


@when("clico em todos os botoes no grid")
def step_clica_todos_edit_e_del_buttons(context):
    context.page.clica_todos_edit_e_del_buttons()
    qtd_botoes_grid = context.page.get_botoes_grid()
    qtd_botoes_esperados_grid = 20
    if len(qtd_botoes_grid) != qtd_botoes_esperados_grid:
        raise AssertionError(f"Erro: quantidade de botões não foi o esperado {len(qtd_botoes_grid)}")
    print(f"{len(qtd_botoes_grid)} botões edit e delete")

@then("todos os botoes da grid devem ser clicados com sucesso")
def step_assegura_clique_todos_grid_buttons(context):
    contagem_esperada_de_cliques = 20
    cliques_por_botao_edit = context.page.botoes_edit()
    cliques_por_botao_del = context.page.botoes_del()

    total_cliques_realizados = len(cliques_por_botao_edit) + len(cliques_por_botao_del)

    if total_cliques_realizados != contagem_esperada_de_cliques:
        raise AssertionError(
            f"Erro: Esperado {contagem_esperada_de_cliques} cliques, mas encontrado {total_cliques_realizados}")
    print(
        f"b) Sua automação clicou com sucesso em todos os {total_cliques_realizados} botões da grid sendo {len(cliques_por_botao_edit)} no edit e {len(cliques_por_botao_del)} no delete.")
