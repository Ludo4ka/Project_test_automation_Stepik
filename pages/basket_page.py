from .base_page import BasePage
from .locators import ProductPageLocators

class BasketPage(BasePage):
  def should_not_be_success_message(self):
      assert self.is_not_element_present(*ProductPageLocators.MESSAGE), \
       "Есть сообщение, что добавили в корзину, но не должно быть"

  def should_be_text_about_empty_bucket(self): #прверяем, что есть текст, что корзина пуста.
      assert self.browser.find_element(*ProductPageLocators.MESSAGE_EMPTY_BASKET).text, \
      "Нет сообщения о пустой корзине"

