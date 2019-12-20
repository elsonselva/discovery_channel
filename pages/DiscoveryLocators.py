# Author : Selva

from selenium.webdriver.common.by import By
from pages.base_page_object import BasePage


class DiscoveryLocators(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    obj_repo = {

                    # Main Page
                    "shows": (By.XPATH, "//span[starts-with(@class,'dscHeaderMain__topNavText') and text() = 'Shows']"),
                    "show_all": (By.XPATH, "//a[@href='/tv-shows/'][text()='See All Shows']"),
                    "tv_shows": (By.XPATH, "//h1[@class='heading__heading'][text()='TV Shows']"),
                    "apollo": (By.XPATH, "//a[@href='/tv-shows/apollo-the-forgotten-films']"),
                    "full_episodes": (By.XPATH, "//h2[@class='collectionHeading__heading'][text()='Episodes']"),
                    # "add_fav": (By.CSS_SELECTOR, "#react-root > div > div.page-wrapper.app__pageWrapper > main"
                    #                              " > section.layout-section.ShowHero.layoutSection__main >"
                    #                              " div > div.showHero__showImage >"
                    #                              " div.showHero__showBrand.showHero__showLogoNoClips"
                    #                              " > div.my-favorites-button-container > span > i"),

                    "add_fav": (By.XPATH, "//*[@class='flipIconCore__icon "
                                          "icon-plus episodeVideoTile__favoritesButton']"),
                    "hamburger_menu": (By.XPATH, "//li[@class='dscHeaderMain__hideMobile']"),
                    "my_video": (By.XPATH, "//a[@href='/my-videos'][span='My Videos']"),
                    "watch_now": (By.XPATH, "//div[@class='play-button primary-play-button unlocked"
                                            " playButton__primaryPlayButtonAuth primaryPlayButtonAuth']"),
                    "my_video_page": (By.XPATH, "//h1[@class='heading__heading'][text()='My Videos']"),
                    "fav_mov": (By.XPATH, "//div[@class='thumbnailTile__titleLineClamp']"
                                          "[text()='Apollo: The Forgotten Films']"),
                    "popular_show": (By.XPATH, "//h2[@class='collectionHeading__heading'][text()='Popular Shows']"),
                    "right_arrow_list": (By.CLASS_NAME, "icon-arrow-right"),
                    "pop_last_explore_more": (By.XPATH, "//div[@class='popularShowTile__showButtonWrapper']"),
                    "explore_more_page": (By.XPATH, "//h2[@class='collectionHeading__heading'][text()='Full']"),
                    "show_more": (By.XPATH, "//div[@class='episodeList__showMore']"),
                    "episode_tiles": (By.XPATH, "//p[@class='episodeTitle']"),
                    "duration_list": (By.XPATH, "//p[@class='minutes']")
            }
