@api
Feature: Testes de CRUD

  #GET
  Scenario Outline: Verificar se o GET retorna a lista de usuários com sucesso
    Given que eu faço uma requisição GET para a lista de usuários
    Then o código de <status_code> esperado retorna
    And o <schema> da resposta deve estar correto
    Examples:
      | status_code | schema                |
      | 200         | get_placeholder_sucess|

  Scenario Outline: Verificar se o GET retorna um usuário específico com sucesso
    Given que eu faço uma requisição GET para a API de usuários com o ID válido <user_id>
    Then o código de <status_code> esperado retorna
    Examples:
      |user_id| status_code |
      |2      | 200         |

  Scenario Outline: Verificar se o GET retorna erro para a lista de usuários
    Given que eu faço uma requisição incorreta GET para a API de usuários <user_id>
    Then o código de <status_code> esperado retorna
    Examples:
      |user_id| status_code  |
      |988    | 404          |


  Scenario Outline: Verificar se o GET retorna erro ao buscar um usuário inexistente
    Given que eu faço uma requisição GET para a API de usuários com o ID <user_id>
    Then o código de <status_code> esperado retorna
    Examples:
      | user_id | status_code |
      | 999     | 404         |

  #POST
  Scenario Outline: Criar um novo usuário com POST
    Given que eu tenho um novo usuário válido
    When eu faço uma requisição POST
    Then o código de <status_code> esperado retorna
    And o usuário deve ser criado corretamente
    And o <schema> da resposta deve estar correto
    Examples:
      | status_code | schema                         |
      | 201         | post_placeholder_sucess        |

  #PUT
  Scenario Outline: Atualizar um usuário com PUT
    Given que eu tenho um usuário válido para atualizar
    When eu faço uma requisição PUT para atualizar o usuário de ID <user_id>
    Then o código de <status_code> esperado retorna
    Examples:
      |user_id| status_code |
      |2    | 200         |

  #DELETE
  Scenario Outline: Deletar um usuário com DELETE
    Given que eu tenho um novo usuário válido
    When eu faço uma requisição DELETE com <user_id> no path param
    Then o código de <status_code> esperado retorna
    Examples:
      | status_code | user_id|
      | 200         | 10     |

  Scenario Outline: Verificar se o DELETE retorna erro ao deletar com parametros incorretos
    Given que eu queira validar o erro do metodo DEL
    When eu faço uma requisição DELETE sem path param
    Then o código de <status_code> esperado retorna
    Examples:
      |status_code  |
      |404          |
