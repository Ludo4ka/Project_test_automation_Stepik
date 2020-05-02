from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
#метод для добавления в корзину, ищем кнопку корзины и кликаем
    def go_to_basket_page(self):
      product_page = self.browser.find_element(*ProductPageLocators.BASKET)
      product_page.click()
      self.solve_quiz_and_get_code()
      time.sleep(0)
      #находим текст/название товара
      product_name = self.browser.find_element(*ProductPageLocators.NAME).text
      #находим сообщение о том, что товар добавлен в корзину 
      message_name = self.browser.find_element(*ProductPageLocators.MESSEGE).text
      #Сравниваем, есть ли название товара в сообщении
      assert product_name == message_name, "No product name in the message"

      #находим стоимость товара и в сообщении стоимость товара
      product_price = self.browser.find_element(*ProductPageLocators.COST).text
      message_price = self.browser.find_element(*ProductPageLocators.MESSEGE_COST).text
      #сравниваем/ проверяем есть ли такой же текст
      assert product_price == message_price, "No product price in the message"