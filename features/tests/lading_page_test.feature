Feature: Test scenarios for the lading page of Cureskin page

    Scenario: User can open the lading page and see the UI components
        Given Open landing page
        Then UI components are visible
   
    Scenario: User can click on Download option on the landing page
        Given Open landing page
        When Click on Download option
        And Switch to the new window
        Then User is redirected to the right page

    Scenario: User can click on About Us and the right page opens
        Given Open landing page
        When Click on About Us option
        Then User is redirected to About Us page

    Scenario: User can click on Testimonials link and the right page opens
        Given Open landing page
        When Click on Testimonials option
        Then User is redirected to Testimonials page

    Scenario: User can click on Expertise link and the right page opens
        Given Open landing page
        When Click on Expertise option
        Then User is redirected to Expertise page

    Scenario: User can click on Shop link and the right page opens
        Given Open landing page
        When Click on Shop option
        Then User is redirected to Shop page
