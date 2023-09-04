Feature: Test scenarios for the shop page of Cureskin page

    Scenario: User can click on layaout for three products per row
        Given Open shop page
        Then User can click on layaout for three products

    Scenario: User can sort by selling
        Given Open shop page
        When Click on sort by
        And User can select the option to sort by selling
        Then Veirfy the url contains the text "sort_by=best-selling"

    Scenario: User can sort alphabetically A-Z
        Given Open shop page
        When Click on sort by
        And User can select the option to sort by selling
        And User can select the option to sort alphabetically A-Z
        Then Veirfy the url contains the text "sort_by=title-ascending"
    
    Scenario: User can sort alphabetically Z-A
        Given Open shop page
        When Click on sort by
        And User can select the option to sort alphabetically Z-A
        Then Veirfy the url contains the text "sort_by=title-descending"
