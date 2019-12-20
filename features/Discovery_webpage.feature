# Author : Selva

Feature: This feature file contain the test-cases which validates the Favourites and Video contents available in Discovery channel web page "https://go.discovery.com"

  @MockTest
  Scenario: Verify Favourites functionality in Discovery Channel web-page
    Given I launch the "discovery_url" web-page
    Then I navigate to "Shows"
    And  Select "See All Shows"
    And I select the show "APOLLO"
    And Verify and update the favourite status
    Then I navigate to "My Videos"
    And Verify contents inside Favourite Shows

  @MockTest
  Scenario: Verify Show more functionality in Discovery Channel web-page
    Given I launch the "discovery_url" web-page
    Then I navigate to "Popular Shows"
    And I navigate to all the episodes of "last" content in Popular Show list
    And Select "Show More"
    And Extract all the data to a text file

