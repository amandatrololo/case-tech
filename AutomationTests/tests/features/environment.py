from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def before_feature(context, feature):
    if "primeiro_desafio_challenging_dom" in feature.filename:
        service = ChromeService(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service)
        context.driver.maximize_window()
        print(f"Driver inicializado para a feature: {feature.name}")

def after_feature(context, feature):
    if "primeiro_desafio_challenging_dom" in feature.filename:
        if context.driver:
            context.driver.quit()
        print(f"Driver finalizado para a feature: {feature.name}")

def before_scenario(context, scenario):
    print(f"Executando o cenário: [{scenario.name}]")

def after_scenario(context, scenario):
    print(f"Cenário finalizado: {scenario.name} [{scenario.status}]")

def after_all_feature(context, feature):
    if feature.status == 'Status.passed':
        print(f"Feature {feature.name} concluída com sucesso:  [{feature.status}]")
