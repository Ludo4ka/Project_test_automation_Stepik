from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    NAME = (By.CSS_SELECTOR, "div.product_main h1") #находим название книги
    COST = (By.CSS_SELECTOR, "p.price_color") #находим цена книги
    MESSAGE = (By.CSS_SELECTOR, ".alertinner strong") #сообщение, что товар добавлен в корзину
    MESSAGE_COST = (By.CSS_SELECTOR, ".alertinner p strong") # сообщ. про стоимость корзины

    BASKET_OPEN_MAIN_PAGE = (By.CSS_SELECTOR, ".btn-group a")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, ".content p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
