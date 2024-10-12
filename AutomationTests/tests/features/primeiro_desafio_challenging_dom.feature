@ui
Feature: Teste nos botões e grid da pagina Challenge


  Scenario: Clica em todos os botões apresentados na tela
    Given eu acesso a webpage do Challenge
    When clico em todos os botoes de acao
    Then todos os botoes da tela devem ser clicados com sucesso

  Scenario: Clico em todos os botoes DEL e EDIT no grid
    Given eu acesso a webpage do Challenge
    When clico em todos os botoes no grid
    Then todos os botoes da grid devem ser clicados com sucesso