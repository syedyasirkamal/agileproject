Feature: Purchase
    """
        Purchase feature will test whether user sees the necessary information and buttons to order forms
    """

    Scenario: Test for purchase page
        Given I navigate to purchase page
        Then I see the Order Now text on the page
        And I see an Order Now button

