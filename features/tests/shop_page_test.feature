Feature: Test scenarios for the shop page of Cureskin page

    Scenario: User can click on layaout for three products per row
        Given Open shop page
        Then User can click on layaout for three products

    Scenario: User can sort by selling
        Given Open shop page
        When Click on sort by
        And User can select the option to sort by selling
        Then Veirfy the url contains the text "sort_by=best-selling"