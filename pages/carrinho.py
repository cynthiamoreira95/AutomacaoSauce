from pages.browser import Browser
class Carrinho(Browser):

    def visualiza(self):
        self.driver.find_element('xpath', '//*[@id="shopping_cart_container"]/a/span').click()


    def dados_pessoais_nome(self, text):
        self.driver.find_element('xpath','//*[@id="first-name"]').send_keys(text)
        self.driver.find_element('xpath', '//*[@id="last-name"]').send_keys(text)
    def dados_cep(self, text):
        self.driver.find_element('xpath','//*[@id="postal-code"]').send_keys(text)
