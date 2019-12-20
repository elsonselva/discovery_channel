# Author : Selva

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, context, wait=10):
        self.driver = context.driver
        self.wait = wait

    def find_element(self, *loc):
        return WebDriverWait(self.driver, self.wait).until(
            expected_conditions.presence_of_element_located((*loc,)))

    def __getattr__(self, what):
        try:
            if what in self.obj_repo.keys():
                return self.find_element(*self.obj_repo[what])
        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(what)
