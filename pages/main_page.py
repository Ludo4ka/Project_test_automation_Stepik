from .base_page import BasePage
from selenium.webdriver.common.by import By

from .login_page import LoginPage #импорт страницы с логином


class MainPage(BasePage): #Предок в Python указывается в скобках: 
  def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)