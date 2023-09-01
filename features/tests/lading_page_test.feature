Feature: Test scenarios for the lading page of Cureskin page

    Scenario: User can open the lading page and see the UI components
        Given Open landing page
        Then UI components are visible
   
    Scenario: User can click on Download option on the landing page
        Given Open landing page
        When Click on Download option
        And Switch to the new window
        Then User is redirected to the right page
