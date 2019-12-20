# Author : Selva

from behave import *
from selenium.common.exceptions import *


@step('I navigate to all the episodes of "{index}" content in Popular Show list')
def list_selected_popular_show(context, index):
    """
    A common method which can be used to navigate to Explore More in any Popular Shows
    """
    context.utilities.wait_till_element_visible('popular_show')
    arrow_list = context.utilities.find_elements('class_name', 'right_arrow_list')
    status = True
    arrow_to_use = None
    if index.lower() == 'last':
        arrow_to_use = arrow_list[7]
    while status:
        arrow_to_use.click()
        try:
            status = arrow_to_use.is_displayed()
        except StaleElementReferenceException:
            status = False
            print("Reached the requested element will exit loop now...")
    context.utilities.wait_till_element_visible('pop_last_explore_more')
    exp_more_list = context.utilities.find_elements('xpath', 'pop_last_explore_more')
    exp_more_list[14].click()
    context.utilities.wait_till_element_visible('explore_more_page')


@step('Extract all the data to a text file')
def extract_data(context):
    """
    Method to extract the episode information and write the same to a file.
    """
    titles = context.utilities.find_elements('xpath', 'episode_tiles')
    durations = context.utilities.find_elements('xpath', 'duration_list')
    with open('Movie_list.txt', 'w') as file:
        for x, y in zip(titles, durations):
            file.write('Title: ' + x.text + '\t' + 'Duration: ' + y.text + '\n')
