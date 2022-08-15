from pages.browser import Browser
class Produtos(Browser):

    def adiciona_produto1(self):
        self.driver.find_element('xpath','//*[@id="add-to-cart-sauce-labs-onesie"]').click()

    def adiciona_produto2(self):
        self.driver.find_element('xpath', '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()