from pages.browser import Browser

class Organiza(Browser):

    def filtro(self):

        self.driver.find_element('xpath', '//*[@id="header_container"]/div[2]/div[2]/span/select').click()
        self.driver.find_element('xpath','//*[@id="header_container"]/div[2]/div[2]/span/select/option[3]').click()

