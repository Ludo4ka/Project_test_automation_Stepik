from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес 
        assert 'login' in self.browser.current_url, "Нет подстроки"
   
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Form of Login is not presented"
         

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Form of Register is not presented"
    

    def register_new_user(self, email, password): #метод регистрация нового пользователя
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password1_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password1_field.send_keys(password)
        password2_field = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
        password2_field.send_keys(password)
        register = self.browser.find_element_by_name("registration_submit")
        register.click()

         #email_field = self.browser.find_element(*LoginPageLocators.register_email_loc)
    # email_field.send_keys(email)
    #непосредственно в setup генерируешь email и password и передаешь в register_new_user()
    # Переменные эмэйла и пароля должны быть внутри фикстуры.
    #browser.find_elements_by_css_selector("input#id_registration-email").send_keys(email)
