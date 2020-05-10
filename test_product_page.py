from .pages.product_page import ProductPage
from .pages.main_page import MainPage
import pytest
import time
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

class TestUserAddToBasketFromProductPage():

  @pytest.fixture(scope="function", autouse=True)
  def setup(self, browser):
      link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login"
      self.page = LoginPage(browser, link)
      self.page.open()
      email = str(time.time()) + "@fakemail.org"
      password = str(time.time())
      self.page.register_new_user(email, password) #регистрируем пользователя
      self.page.should_be_authorized_user()#проверяем, что пользователь залогинен

     

  def test_user_cant_see_success_message(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
    page = ProductPage(browser, link)   
    page.open()
    page.should_not_be_success_message()

 
  def test_user_can_add_product_to_basket(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    #находим кнопку карзинки и нажимаем ее
    page.go_to_basket_page()

#def test_guest_cant_see_success_message(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
    #page = ProductPage(browser, link)   
    #page.open()
    #page.should_not_be_success_message()

  
#@pytest.mark.parametrize('offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
  #def test_guest_can_add_product_to_basket(browser, offer):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    #page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    #page.open()                      # открываем страницу
    #находим кнопку карзинки и нажимаем ее
    #page.go_to_basket_page()

#@pytest.mark.xfail    
#def test_user_cant_see_success_message_after_adding_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
    #page = ProductPage(browser, link)   
    #page.open()                      
    #page.go_to_basket_page()
    #page.should_not_be_success_message()#Проверяем, что нет сообщения об успехе с помощью is_not_element_present



#@pytest.mark.xfail
#def test_message_disappeared_after_adding_product_to_basket(browser): 
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
    #page = ProductPage(browser, link)   
    #page.open()
    #page.go_to_basket_page()
    #page.should_is_disappeared_success_message()

#def test_guest_should_see_login_link_on_product_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    #page = ProductPage(browser, link)
    #page.open()
    #page.should_be_login_link()

#def test_guest_can_go_to_login_page_from_product_page (browser):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    #page = ProductPage(browser, link)
    #page.open()
    #page.go_to_login_page()

    
#def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
   #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
   #page = ProductPage(browser, link)   
   #page.open()
   #page.go_to_basketmini()#переход в корзину по кнопке в шапке сайта
   #basket_page = BasketPage(browser, browser.current_url) #инициализируем новую страницу
   #basket_page.should_not_be_success_message()
   #basket_page.should_be_text_about_empty_bucket()

