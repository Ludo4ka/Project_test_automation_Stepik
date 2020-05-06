from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
#метод для добавления в корзину, ищем кнопку корзины и кликаем
    def go_to_basket_page(self):
      product_page = self.browser.find_element(*ProductPageLocators.BASKET)
      product_page.click()
      #self.solve_quiz_and_get_code()
      
      #находим текст/название товара
      product_name = self.browser.find_element(*ProductPageLocators.NAME).text
      #находим сообщение о том, что товар добавлен в корзину 
     # message_name = self.browser.find_element(*ProductPageLocators.MESSEGE).text
      #Сравниваем, есть ли название товара в сообщении
      #assert product_name == message_name, "No product name in the message"

      #находим стоимость товара и в сообщении стоимость товара
      #product_price = self.browser.find_element(*ProductPageLocators.COST).text
      #message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_COST).text
      #сравниваем/ проверяем есть ли такой же текст
      #assert product_price == message_price, "No product price in the message"

     #упадет, как только увидит искомый элемент. Не появился элемент: успех, тест зеленый. 
     #проверяет, что элемент не появляется на странице в течение заданного времени: 
    def should_not_be_success_message(self):
      assert self.is_not_element_present(*ProductPageLocators.MESSAGE), \
       "Success message is presented, but should not be"

    #проверить, что какой-то элемент исчезает, чз опред.t
    #будет ждать до тех пор, пока элемент не исчезнет. Упадет, если не исчезает
    def should_is_disappeared_success_message(self):
      assert self.is_disappeared(*ProductPageLocators.MESSAGE), \
       "Success message is presented, but should not be"

    

    def should_be_text_about_empty_bucket(self): #прверяем, что есть текст, что корзина пуста.
      assert self.browser.find_element(*ProductPageLocators.MESSAGE_EMPTY_BASKET).text, \
      "Нет сообщения о пустой корзине"


       
    
    

