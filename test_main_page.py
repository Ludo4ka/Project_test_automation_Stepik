from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self                       
    def test_guest_can_go_to_login_page(self, browser):     
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      
        page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина

        login_page = LoginPage(browser, browser.current_url) #инициализация новой страницы, переход м/у стр.
        login_page.should_be_login_page()       #browser.current_url - возвращает текущий урл

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
  link = "http://selenium1py.pythonanywhere.com"
  page = BasePage(browser, link)
  page.open()
  page.go_to_basketmini()#переход в корзину по кнопке в шапке сайта
  basket_page = BasketPage(browser, browser.current_url) 
  basket_page.should_not_be_success_message()
  basket_page.should_be_text_about_empty_bucket()


