from pages.browser import Browser
class LoginPage(Browser):
    def preenche_usuario(self,text):

        self.driver.find_element('xpath','//*[@id="user-name"]').send_keys(text)

    def preenche_password(self,text):
        self.driver.find_element('xpath','//*[@id="password"]').send_keys(text)

    def clicar_btn_login(self):
        self.driver.find_element('xpath', '//*[@id="login-button"]').click()
