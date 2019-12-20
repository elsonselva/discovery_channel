# Author : Selva

"""
File includes all the common utilities which can be used
during test automation using Selenium
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Utilities:
    """
    Class which holds all the common utilities
    """

    def __init__(self, context):
        self.driver = context.driver
        self.locator = context.locators

    def wait_for_element(self, element):
        """
        Re-usable common utility to wait for an element instead of keeping hardcoded sleeps
        """
        path = self.locator.obj_repo.get(element)
        WebDriverWait(self.driver, 60).until(
            expected_conditions.presence_of_element_located(path))

    def wait_till_element_visible(self, element):
        """
        Re-usable common utility to wait till an element is present and visible
        """
        path = self.locator.obj_repo.get(element)
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(path))
            return True
        except TimeoutException:
            return False

    def wait_till_element_not_visible(self, element):
        """
        Re-usable common utility to wait till an element is not visible
        Useful in case if you have a loader icon will keeps loading till
        all the contents are available
        """
        path = self.locator.obj_repo.get(element)
        try:
            WebDriverWait(self.driver, 60).until_not(
                expected_conditions.visibility_of_element_located(path))
            return True
        except TimeoutException:
            return False

    def element_displayed(self, locator_type, locator):
        """
            Return True if element is displayed, else return False
        """
        path = self.locator.obj_repo.get(locator)
        try:
            if locator_type.lower() == 'id':
                return_value = self.driver.find_element_by_id(path[1]).is_displayed()
            elif locator_type.lower() == 'xpath':
                return_value = self.driver.find_element_by_xpath(path[1]).is_displayed()
            elif locator_type.lower() == 'classname':
                return_value = self.driver.find_element_by_class_name(path[1]).is_displayed()
            elif locator_type.lower() == 'cssselector':
                return_value = self.driver.find_element_by_css_selector(path[1]).is_displayed()
            else:
                raise AttributeError("locator type not supported,"
                                     " please add the support in utilities")
        except NoSuchElementException:
            return_value = False
        return return_value

    def move_to_element_method(self, locator_type, locator):
        """
        Re-usable common utility which uses Selenium ActionChains to perform navigation
        """
        path = self.locator.obj_repo.get(locator)
        if locator_type.lower() == 'id':
            element = self.driver.find_element_by_id(path[1])
        elif locator_type.lower() == 'xpath':
            element = self.driver.find_element_by_xpath(path[1])
        else:
            raise AttributeError("locator type not supported, please add the support in utilities")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scroll_find_click(self, locator_type, locator):
        """
        Re-usable common utility which scrolls, locates and click on the element passed
        """
        path = self.locator.obj_repo.get(locator)
        counter = 0
        while counter != 10 and not(self.element_displayed(locator_type, locator)):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            counter += 1
        if locator_type.lower() == 'id':
            self.driver.find_element_by_id(path[1]).click()
        elif locator_type.lower() == 'xpath':
            self.driver.find_element_by_xpath(path[1]).click()
        else:
            raise AttributeError("locator type not supported, please add the support in utilities")

    def find_elements(self, locator_type, locator):
        """
        Re-usable common utility which returns a list of
        elements-object located with the given locator type
        """
        path = self.locator.obj_repo.get(locator)
        if locator_type == 'xpath':
            name_of_ele = self.locator.driver.find_elements_by_xpath(path[1])
        elif locator_type == 'class_name':
            name_of_ele = self.locator.driver.find_elements_by_class_name(path[1])
        else:
            raise AttributeError("locator type not supported, please add the support in utilities")
        return name_of_ele
