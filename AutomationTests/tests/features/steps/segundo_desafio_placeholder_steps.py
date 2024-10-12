import os
import json
from jsonschema import validate, ValidationError
from behave import given, when, then
from AutomationTests.tests.features.pages.segundo_desafio_placeholder import APIClient
from AutomationTests.factories.cria_novo_user_placeholder_factory import CriaUsuarioNovo

api_client = APIClient()

# GET: Listar usuários
@given('que eu faço uma requisição GET para a lista de usuários')
def step_impl(context):
    response = api_client.get_users()
    context.response_json = response.json()
    context.status_code = response.status_code

@then('o código de {status_code} esperado retorna')
def step_impl(context, status_code):
    assert context.status_code == int(status_code), f"Atenção: era esperado código {status_code}, mas obtido {context.status_code}"

@then('o {schema} da resposta deve estar correto')
def step_impl(context, schema):
    schema_file_name = f"{schema}.json"
    schema_path = os.path.join('AutomationTests', 'schemas', schema_file_name)

    with open(schema_path, 'r') as schema_file:
        schema_data = json.load(schema_file)
    try:
        validate(instance=context.response_json, schema=schema_data)
    except ValidationError as e:
        raise AssertionError(f"Erro de validação do schema: {e}")

# POST: Criar usuário válido
@given('que eu tenho um novo usuário válido')
def step_impl(context):
    context.new_user = CriaUsuarioNovo()

@when('eu faço uma requisição POST')
def step_impl(context):
    response = api_client.create_user(context.new_user)
    context.status_code = response.status_code
    context.response = response
    context.response_json = response.json()

@then('o usuário deve ser criado corretamente')
def step_impl(context):
    assert context.response_json['name'] == context.new_user['name'], "O usuário não foi criado corretamente."

# PUT: Atualizar usuário válido
@given('que eu tenho um usuário válido para atualizar')
def step_impl(context):
    context.user_update = {
        "name": "Usuário Alterado"
    }

@when('eu faço uma requisição PUT para atualizar o usuário de ID {user_id}')
def step_impl(context, user_id):
    response = api_client.update_user(user_id, context.user_update)
    context.response_json = response.json()
    context.status_code = response.status_code

@then('o usuário deve ser atualizado corretamente')
def step_impl(context):
    assert context.response_json['name'] == context.user_update['name'], "O usuário não foi atualizado corretamente."

# DELETE: Remover usuário
@when('eu faço uma requisição DELETE com {user_id} no path param')
def step_impl(context, user_id):
    response = api_client.delete_user(user_id)
    context.status_code = response.status_code

# GET: Obter usuário por ID
@given("que eu faço uma requisição GET para a API de usuários com o ID válido {user_id}")
def step_impl(context, user_id):
    response = api_client.get_user(int(user_id))
    context.response_json = response.json()
    context.status_code = response.status_code

# GET: Obter usuário com erro
@given("que eu faço uma requisição incorreta GET para a API de usuários {user_id}")
def step_impl(context, user_id):
    response = api_client.get_user(user_id)
    context.response_json = response.json()
    context.status_code = response.status_code


@given("que eu faço uma requisição GET para a API de usuários com o ID {user_id}")
def step_impl(context, user_id):
    response = api_client.get_user(user_id)
    context.response_json = response.json()
    context.status_code = response.status_code


@given("que eu queira validar o erro do metodo DEL")
def step_impl(context):
    pass

@when("eu faço uma requisição DELETE sem path param")
def step_impl(context):
    response = api_client.delete_invalid_user()
    context.status_code = response.status_code
