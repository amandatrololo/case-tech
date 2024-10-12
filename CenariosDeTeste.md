# Cenários de Teste

1. **Iniciaria a estratégia de teste** com uma reunião com o P.O e cliente, com a intenção de levantar requisitos funcionais e não-funcionais. Faria perguntas específicas sobre como o sistema deve se comportar em cenários de carga alta e baixa, como o cliente espera que os diferentes tipos de usuários interajam.
   A partir dos critérios de aceite redigidos pelo P.O, já construiria cenários, seguindo a boa prática de shift-left testing. Focando principalmente na interação de bancos, clientes e imobiliárias.

2. Focaria em **testes de caixa preta**, **testes de API** e **testes de contrato** (para garantir os tipos esperados).

3. Com base na **pirâmide de testes**, e já contando com os testes unitários feitos pelos devs:
   - **Testes de Integração** para validar os microsserviços e suas interações entre o banco e imobiliária.
   - **Teste de UI**, caso seja necessário (se tivermos uma web page ou app).
   - **Teste de Carga**, levando em consideração o alto volume de requisições, bem como a sua performance.

4. **Ferramentas**:
   - Para automações de testes funcionais: no Python, usaria o **Selenium** (para testes de UI), **Behave**, e **schema validators**. Sempre focando em respeitar as boas práticas de BDD.
   - **Testes de API**: **Postman** (para validações manuais) e automações de testes API no Python.
   - **Testes de Carga**: **JMeter**.

5. Me imagino atuando de forma bastante colaborativa desde o início do projeto, garantindo que as práticas de qualidade estejam alinhadas com o desenvolvimento ágil. Trabalharia em parceria com os desenvolvedores para definir estratégias de testes em conjunto, garantindo que tanto os testes unitários quanto os de integração estejam em conformidade com as expectativas do negócio.
