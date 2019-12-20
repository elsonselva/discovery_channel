# Author : Selva

from behave import *
from selenium import webdriver
from utilities import Utilities
from pages.DiscoveryLocators import DiscoveryLocators


def before_all(context):
    """
    This function is executed first when you call the runner.py
    Specify here all functions/steps which need to be initialized before start of any test
    In below case I am initialising Safari web-driver and assigning it to context so that its available
    across my test run
    """
    context.driver = webdriver.Chrome('Dependencies/chromedriver')
    context.driver.implicitly_wait(3)
    context.locators = DiscoveryLocators(context)
    context.utilities = Utilities(context)


def before_feature(context, feature):
    """
    Specify here any function/step which need to be executed before a feature is started
    """
    pass


def before_scenario(context, scenario):
    """
    Specify here any function/step which need to be executed before a scenario is started
    """
    pass


def after_feature(context, feature):
    """
    Specify here any function/step which need to be executed after a feature is started
    """
    pass


def after_scenario(context, scenario):
    """
    Specify here any function/step which need to be executed after a scenario is started
    """
    pass


def after_all(context):
    """
    Specify here any function/step which need to be executed after a execution is completed
    """
    context.driver.quit()
