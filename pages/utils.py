from pages.browser import Browser


class Utils(Browser):

    def navegar(self, url: object) -> object:
        self.driver.get(url)

    def continuar(self):
        self.driver.find_element('xpath', '//*[@id="continue"]').click()

    def checkout(self):
        self.driver.find_element('xpath', '//*[@id="checkout"]').click()

    def scroll_down(self):
        self.driver.execute_script('window.scroll(0, 250)')

    def scroll_up(self):
        self.driver.execute_script('window.scroll(0,0)')

    def finish(self):
        self.driver.find_element('xpath','//*[@id="finish"]').click()

