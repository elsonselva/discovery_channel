# Author : Selva

from behave import *
import config


@step('I launch the "{web_page}" web-page')
def launch_web_page(context, web_page):
    """
    This method will launch the given url from config file and wait till web page is loaded
    """
    context.driver.get(config.WEB_URL)
    assert "Discovery - Official Site" in context.driver.title


@step('I navigate to "{navigator}"')
def navigate_top_menu(context, navigator):
    """
    A common method which can be re-used for navigating multiple panes from the main web-page
    """
    if navigator.lower() == 'shows':
        context.utilities.wait_till_element_visible('shows')
        context.locators.shows.click()
        context.utilities.wait_till_element_visible('show_all')
    elif navigator.lower() == 'my videos':
        context.locators.hamburger_menu.click()
        context.utilities.wait_till_element_visible('my_video')
        context.utilities.wait_till_element_visible('watch_now')
        context.locators.my_video.click()
        context.utilities.wait_till_element_visible('my_video_page')
    elif navigator.lower() == 'popular shows':
        context.utilities.move_to_element_method('xpath', 'popular_show')
    else:
        raise AssertionError("Invalid argument provided for this step")


@step('Select "{content}"')
def select(context, content):
    """
    Common method which can be re-used to select drop down list contents
    """
    if content.lower() == 'see all shows':
        context.locators.show_all.click()
    elif content.lower() == 'show more':
        context.utilities.move_to_element_method('xpath', 'show_more')
        context.locators.show_more.click()


@step('I select the show "{show_name}"')
def select_episode(context, show_name):
    """
    Reusable method to select Shows from the list, argument is the key from obj_repo
    """
    context.utilities.wait_till_element_visible('tv_shows')
    context.utilities.scroll_find_click('xpath', show_name.lower())
    context.utilities.wait_till_element_visible('full_episodes')


@step('Verify and update the favourite status')
def verify_fav_status(context):
    """
    This method will add/remove movie content based on the status of FAV_ICON for the selected movie
    """
    context.fav_list_add_status = True
    context.utilities.wait_till_element_visible('add_fav')
    status = context.locators.add_fav.get_attribute('class')
    print(status)
    if status == 'flipIconCore__icon icon-plus episodeVideoTile__favoritesButton':
        print("Content is not yet added to favourite hence adding...")
    elif status == 'flipIconCore__icon icon-minus episodeVideoTile__favoritesButton':
        print("Content is already added to favourite hence removing...")
        context.fav_list_add_status = False
    context.locators.add_fav.click()


@step('Verify contents inside Favourite Shows')
def verify_fav_shows(context):
    """
    Method to verify and throw error in case verification fails
    """
    print(context.fav_list_add_status)
    if context.fav_list_add_status:
        # Will throw assertion error of content is not displayed
        assert context.locators.fav_mov.is_displayed()
    else:
        # Will throw assertion error of content is displayed
        assert not(context.locators.fav_mov.is_displayed())
