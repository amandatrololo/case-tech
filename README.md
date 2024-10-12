# case-tech

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada para implementação do projeto.
- **Selenium**: Automação de navegadores para testes dos endpoints.
- **Behave**: Ferramenta utilizada para testes de comportamento (BDD).
- **Factory Boy & Faker**: Ferramentas para criar dados fictícios para os testes.

## Dependências

Segue a lista de dependências para rodar o projeto, conforme especificado no arquivo `requirements.txt`:

```text
behave~=1.2.6
selenium~=4.25.0
jsonschema~=4.23.0
schema~=0.7.7
webdriver-manager~=4.0.2
requests~=2.32.3
factory_boy~=3.3.1
Faker~=30.3.0
```

Você pode instalar todas as dependências utilizando o seguinte comando:

```sh
pip install -r requirements.txt
```

## Tutorial para Execução dos Testes

Certifique-se que todas as dependências estejam instaladas.

Execute o cenário de teste:

```sh
$ behave
```
