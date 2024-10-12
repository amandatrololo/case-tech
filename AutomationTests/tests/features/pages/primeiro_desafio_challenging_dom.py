from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class DesafioDom:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/challenging_dom"

    def get_botoes_acao(self):
        try:
            return self.driver.find_elements(By.CSS_SELECTOR, ".button")
        except NoSuchElementException:
            raise NoSuchElementException("Erro: Não foi possível encontrar os botões de ação na página.")

    def blue_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".button")

    def red_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".button.alert")

    def green_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".button.success")

    def get_botoes_grid(self):
        try:
            return self.botoes_edit() + self.botoes_del()
        except NoSuchElementException:
            raise NoSuchElementException("Erro: Não foi possível encontrar os botões no grid.")

    def botoes_edit(self):
        return self.driver.find_elements(By.XPATH, "//a[text()='edit']")

    def botoes_del(self):
        return self.driver.find_elements(By.XPATH, "//a[text()='delete']")

    def open(self):
        self.driver.get(self.url)

    def clica_todos_action_buttons(self):
        botoes_clicados = []
        self.blue_button().click()
        botoes_clicados.append("blue_button_clicado")
        self.red_button().click()
        botoes_clicados.append("red_button_clicado")
        self.green_button().click()
        botoes_clicados.append("green_button_clicado")
        return botoes_clicados

    def clica_todos_edit_e_del_buttons(self):

        botoes_grid_clicados = []
        for edit_button in self.botoes_edit():
            edit_button.click()
            botoes_grid_clicados.append("edit_button_clicado")

        for delete_button in self.botoes_del():
            delete_button.click()
            botoes_grid_clicados.append("delete_button_clicado")
        return botoes_grid_clicados
